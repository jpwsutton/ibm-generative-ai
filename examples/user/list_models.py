import os

from dotenv import load_dotenv

from genai.credentials import Credentials
from genai.model import Metadata

# make sure you have a .env file under genai root with
# GENAI_KEY=<your-genai-key>
# GENAI_API=<genai-api-endpoint>
load_dotenv()
api_key = os.getenv("GENAI_KEY", None)
api_endpoint = os.getenv("GENAI_API", None)

print("\n------------- Example List models -------------\n")

# This Example queries the API for a list of models that are
# available for inferencing. You can use the model ID for your
# generate and tokenize requests.

creds = Credentials(api_key, api_endpoint)

metadata = Metadata(credentials=creds)

available_models = metadata.get_models()

for model in available_models:
    print(f"Model: {model.name}")
    print(f"    ID: {model.id}")
    print(f"    Size: {model.size}")
    print(f"    Source Model: {model.source_model_id}")
    print(f"    Token limit: {model.token_limit}\n")
