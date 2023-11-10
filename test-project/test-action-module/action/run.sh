python3 -m venv env
source env/bin/activate
pip install requests
pip install f_one_core_utilities

from main import process_payload

payload = ...  # Define your payload here
result = process_payload(payload)
print(result)

python run.py
