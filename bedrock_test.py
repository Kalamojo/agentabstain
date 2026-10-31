import boto3
import os
from dotenv import load_dotenv

load_dotenv()

# Set the API key as an environment variable
# os.environ['AWS_BEARER_TOKEN_BEDROCK'] = "${api-key}"
print("region:", os.getenv("AWS_REGION", "us-east-1"))

# Create the Bedrock client
client = boto3.client(
    service_name="bedrock-runtime",
    region_name=os.getenv("AWS_REGION", "us-east-1")
)

# Define the model and message
model_id = "us.anthropic.claude-sonnet-4-6"
messages = [{"role": "user", "content": [{"text": "Howdy. Can you tell me about Amazon Bedrock?"}]}]

# Make the API call
response = client.converse(
    modelId=model_id,
    messages=messages,
)

# Print the response
print(response['output']['message']['content'][0]['text'])
