FROM python:3.9


WORKDIR /app
ARG GIT_TOKEN
RUN git config --global url."https://${GIT_TOKEN}@github.com".insteadOf "ssh://git@github.com"

# install requirements
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt


COPY ./action ./action
COPY config.yml config.yml
COPY run.py run.py

