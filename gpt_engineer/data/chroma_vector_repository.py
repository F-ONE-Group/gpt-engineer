from typing import List

import chromadb
from llama_index import Document, VectorStoreIndex
from llama_index.retrievers import BM25Retriever
from llama_index.schema import NodeWithScore
from llama_index.vector_stores import ChromaVectorStore

from gpt_engineer.data.document_chunker import DocumentChunker


class ChromaVectorRepository:
    def __init__(self):
        self._index = None
        self._query_engine = None
        self._retriever = None

    def load_from_chroma_collection(
        self, collection_name: str, chroma_host: str, chroma_port: int = 8000
    ):
        chroma_client = chromadb.HttpClient(host="localhost", port=8003)
        collection = chroma_client.get_collection(name="test")
        collection_details = collection.get(
            include=["embeddings", "documents", "metadatas"]
        )
        documents: List[Document] = []
        for doc, emb, metadata in zip(
            collection_details["documents"],
            collection_details["embeddings"],
            collection_details["metadatas"],
        ):
            documents.append(Document(text=doc, embedding=emb, metadata=metadata))

        chunked_documents = [
            Document.from_langchain_format(doc.to_langchain_format()) for doc in documents
        ]

        self._index = VectorStoreIndex.from_documents(chunked_documents)
        # vector_store = ChromaVectorStore(
        #     chroma_collection=collection, host=chroma_host, port=chroma_port
        # )
        # self._index = VectorStoreIndex.from_vector_store(vector_store)

    def query(self, query_string: str):
        """
        Ask a plain english question about the code base and retrieve a plain english answer
        """

        if self._index is None:
            raise ValueError("Index has not been loaded yet.")

        if self._query_engine is None:
            self._query_engine = self._index.as_query_engine(
                response_mode="tree_summarize"
            )

        return self._query_engine.query(query_string)

    def relevent_code_chunks(
        self, query_string: str, llm: str = "default"
    ) -> List[NodeWithScore]:
        """
        Retrieve code chunks relevant to a prompt
        """

        if self._index is None:
            raise ValueError("Index has not been loaded yet.")

        if self._retriever is None:
            self._retriever = BM25Retriever.from_defaults(
                self._index, similarity_top_k=10
            )

        return self._retriever.retrieve(query_string)
