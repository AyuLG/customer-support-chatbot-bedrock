#!/usr/bin/env python3
"""
Evaluate the harness with test cases.
"""

import json
import boto3

bedrock_runtime = boto3.client('bedrock-runtime', region_name='us-east-1')

def run_tests(tests_json_file='harness-tests.json'):
    # Load the config
    with open('agentcore_config.json', 'r') as f:
        config = json.load(f)
    
    system_prompt = config['systemPrompt']
    
    # Load tests
    with open(tests_json_file, 'r') as f:
        data = json.load(f)
    
    tests = data.get('tests', [])
    results = []
    
    for i, test in enumerate(tests):
        print(f"[{i+1}/{len(tests)}] Running test: {test['id']}")
        
        messages = [
            {
                "role": "user",
                "content": [{"text": test['prompt']}]
            }
        ]
        
        try:
            response = bedrock_runtime.converse(
                modelId="us.amazon.nova-pro-v1:0",
                messages=messages,
                system=[{"text": system_prompt}],
                inferenceConfig={
                    "maxTokens": 1000,
                    "temperature": 0.7
                }
            )
            
            bot_response = response['output']['message']['content'][0]['text']
            
            results.append({
                'prompt': test['prompt'],
                'referenceResponse': test['expected'],
                'modelResponses': [
                    {
                        'response': bot_response,
                        'modelIdentifier': 'support-chatbot'
                    }
                ]
            })
            
            print(f"  ✅ Response received")
            
        except Exception as e:
            print(f"  ❌ Error: {str(e)}")
            results.append({
                'prompt': test['prompt'],
                'referenceResponse': test['expected'],
                'modelResponses': [
                    {
                        'response': f"[ERROR] {str(e)}",
                        'modelIdentifier': 'support-chatbot'
                    }
                ]
            })
    
    output_file = 'output_eval_dataset.jsonl'
    with open(output_file, 'w') as f:
        for result in results:
            f.write(json.dumps(result) + '\n')
    
    print(f"\n✅ Results written to {output_file}")
    print(f"Total tests: {len(results)}")

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--tests-json', default='harness-tests.json')
    args = parser.parse_args()
    run_tests(args.tests_json)
EOFcat > eval_harness.py << 'EOF'
#!/usr/bin/env python3
"""
Evaluate the harness with test cases.
"""

import json
import boto3

bedrock_runtime = boto3.client('bedrock-runtime', region_name='us-east-1')

def run_tests(tests_json_file='harness-tests.json'):
    # Load the config
    with open('agentcore_config.json', 'r') as f:
        config = json.load(f)
    
    system_prompt = config['systemPrompt']
    
    # Load tests
    with open(tests_json_file, 'r') as f:
        data = json.load(f)
    
    tests = data.get('tests', [])
    results = []
    
    for i, test in enumerate(tests):
        print(f"[{i+1}/{len(tests)}] Running test: {test['id']}")
        
        messages = [
            {
                "role": "user",
                "content": [{"text": test['prompt']}]
            }
        ]
        
        try:
            response = bedrock_runtime.converse(
                modelId="us.amazon.nova-pro-v1:0",
                messages=messages,
                system=[{"text": system_prompt}],
                inferenceConfig={
                    "maxTokens": 1000,
                    "temperature": 0.7
                }
            )
            
            bot_response = response['output']['message']['content'][0]['text']
            
            results.append({
                'prompt': test['prompt'],
                'referenceResponse': test['expected'],
                'modelResponses': [
                    {
                        'response': bot_response,
                        'modelIdentifier': 'support-chatbot'
                    }
                ]
            })
            
            print(f"  ✅ Response received")
            
        except Exception as e:
            print(f"  ❌ Error: {str(e)}")
            results.append({
                'prompt': test['prompt'],
                'referenceResponse': test['expected'],
                'modelResponses': [
                    {
                        'response': f"[ERROR] {str(e)}",
                        'modelIdentifier': 'support-chatbot'
                    }
                ]
            })
    
    output_file = 'output_eval_dataset.jsonl'
    with open(output_file, 'w') as f:
        for result in results:
            f.write(json.dumps(result) + '\n')
    
    print(f"\n✅ Results written to {output_file}")
    print(f"Total tests: {len(results)}")

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--tests-json', default='harness-tests.json')
    args = parser.parse_args()
    run_tests(args.tests_json)
