Here is the code with the identified issues fixed:


import json
import boto3

def get_response():
    bedrock_client = boto3.client(
        service_name="bedrock-runtime",
        region_name="us-east-1"
    )
    model_id = "anthropic.claude-3-sonnet-20240229-v1:0"
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
    response = bedrock_client.invoke_model(
        modelId=model_id,
        body=json.dumps(payload)
    )
    result = json.loads(response["body"].read())
    print(result)
    generated_text = "".join([output["text"] for output in result["content"]])
    print(f"Response: {generated_text}")

if __name__ == "__main__":
    get_response()