#!/usr/bin/env python3
"""
Create an AgentCore Harness for the customer support chatbot.
"""

import json
import boto3

bedrock = boto3.client('bedrock', region_name='us-east-1')

def create_harness():
    print("Creating AgentCore Harness...")
    
    # Read the system prompt
    with open('system_prompt.txt', 'r') as f:
        system_prompt = f.read()
    
    # Read the FAQ content
    with open('online_shop_faq.md', 'r') as f:
        faq_content = f.read()
    
    # Replace {{FAQ}} with actual content
    system_prompt = system_prompt.replace('{{FAQ}}', faq_content)
    
    # Save the config for the chat script
    config = {
        'systemPrompt': system_prompt,
        'modelId': 'us.amazon.nova-pro-v1:0'
    }
    with open('agentcore_config.json', 'w') as f:
        json.dump(config, f, indent=2)
    
    print("✅ Config saved to agentcore_config.json")
    print("ℹ️  Use 'python chat.py' to chat with the bot")
    return None

if __name__ == '__main__':
    create_harness()
