#!/usr/bin/env python3
"""
Simple chatbot using Amazon Nova Pro directly.
"""

import json
import boto3

bedrock_runtime = boto3.client('bedrock-runtime', region_name='us-east-1')

def chat():
    print("🤖 Customer Support Chatbot")
    print("Type 'exit' to quit")
    print("-" * 50)
    
    # Load the config
    with open('agentcore_config.json', 'r') as f:
        config = json.load(f)
    
    system_prompt = config['systemPrompt']
    
    # Initialize conversation with system prompt
    messages = []
    
    while True:
        user_input = input("\nYou: ")
        if user_input.lower() in ['exit', 'quit']:
            break
        
        # Add user message to conversation
        messages.append({
            "role": "user",
            "content": [{"text": user_input}]
        })
        
        try:
            # Use Nova Pro via the Converse API
            response = bedrock_runtime.converse(
                modelId="us.amazon.nova-pro-v1:0",
                messages=messages,
                system=[{"text": system_prompt}],
                inferenceConfig={
                    "maxTokens": 1000,
                    "temperature": 0.7
                }
            )
            
            # Extract the response
            bot_response = response['output']['message']['content'][0]['text']
            
            # Add assistant response to conversation
            messages.append({
                "role": "assistant",
                "content": [{"text": bot_response}]
            })
            
            print(f"\nBot: {bot_response}")
            
        except Exception as e:
            print(f"\nBot: Error: {str(e)}")

if __name__ == '__main__':
    chat()
