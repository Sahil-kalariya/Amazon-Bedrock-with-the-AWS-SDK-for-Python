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
    print(result)
    generated_text = "".join([output["text"] for output in result["content"]])
    print(f"Response: {generated_text}")

if __name__ == "__main__":
    getResponse()



# {'id': 'msg_bdrk_01GNeNzo4ZjAguvfqGkkVV9M', 'type': 'message', 'role': 'assistant', 'model': 'claude-3-sonnet-20240229', 
# 'content': [{'type': 'text', 'text': "Hello! As an AI language model, I don't have subjective experiences or emotions, but I'm operating properly and ready to assist you with any questions or tasks you might have. How can I help you today?"}], 
# 'stop_reason': 'end_turn', 'stop_sequence': None, 'usage': {'input_tokens': 13, 'output_tokens': 47}}