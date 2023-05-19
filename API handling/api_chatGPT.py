import requests
import json
import time

API_URL = 'https://api.openai.com/v1/engines/davinci-codex/completions'

def query_chatgpt(prompt):
    headers = {
        'Authorization': 'Bearer my_private_KEY',
        'Content-Type': 'application/json'
    }
    data = {
        'prompt': prompt,
        'max_tokens': 50,
        'temperature': 0.7
    }

    retries = 3
    timeout = 10
    backoff_factor = 2

    while retries > 0:
        try:
            response = requests.post(API_URL, headers=headers, json=data, timeout=timeout)
            response.raise_for_status()
            return response.json()['choices'][0]['text'].strip()
        except requests.exceptions.RequestException as err:
            print(f'Request Exception: {err}')
        except (KeyError, IndexError) as err:
            print(f'Error parsing response: {err}')
        except Exception as err:
            print(f'Unexpected error occurred: {err}')

        # Retry after a delay using exponential backoff strategy
        retries -= 1
        if retries > 0:
            delay = backoff_factor**(3 - retries)
            print(f'Retrying after {delay} seconds...')
            time.sleep(delay)

    print('API request failed after retries.')
    return None

# Example usage
prompt = 'What is the capital of France?'
response = query_chatgpt(prompt)

if response:
    print(f'ChatGPT: {response}')
else:
    print('Failed to get a response from ChatGPT.')
