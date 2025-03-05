# What is it about ?
Build generative AI applications on Amazon Bedrock with the AWS SDK for Python (Boto3)

# Requirements
AWS account with access to bedrock models in us-east-1

IAM user with appropriate permissions to access models

The IAM user access key and secret key to configure the AWS CLI and permissions

AWS CLI installed and configured 

Python version 3.8 with IDE

The latest Boto3 library


# Steps/Actions

## Creat a python file
create  python file named main.py or any other name

## Creating virtual environment in python

Use virtual environment to maintain packages across different projects

```bash
python -m venv venv
```

Activate virtual Enviroment

```bash
venv\Script\activate
```

## Installation of Boto3

Installing boto3 on our virtual environment

```bash
pip install boto3
```

## Code

```python
# Import the required libraries:
import json
import boto3

def getResponse():
# Set up the Amazon Bedrock client
    bedrock_client = boto3.client(
        	service_name="bedrock-runtime",
            region_name="us-east-1"
    )
# Define the model ID
    model_id = "anthropic.claude-3-sonnet-20240229-v1:0"
# Prepare the input prompt.
    prompt = "Hello, how are you?"
    payload = {
        "anthropic_version": "bedrock-2023-05-31",
        "max_tokens": 200,
        "temperature": 0.9,
        "top_k": 250,
        "top_p": 1,
        "messages": [
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": prompt
                    }
                ]
            }
        ]
    }
    # Invoke the Amazon Bedrock model
    response = bedrock_client.invoke_model(
        modelId=model_id,
        body=json.dumps(payload)
    )
    # Process the response
    result = json.loads(response["body"].read())
    generated_text = "".join([output["text"] for output in result["content"]])
    print(f"Response: {generated_text}")

if __name__ == "__main__":
    getResponse()
```

## Run File 

```bash
python [NAME_OF_FILE].py
```

## OUTPUT
```bash
"Hello! As an AI language model, I don't have subjective experiences or emotions, but I'm operating properly and ready to assist you with any questions or tasks you might have. How can I help you today?"
```
