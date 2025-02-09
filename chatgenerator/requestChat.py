import requests
import textwrap

SYSTEM_PROMPT = """\
You are a human having a conversation with a friend.

- Be polite but also challenge your friend.
- Occasionally ask questions.
- You don't know everything; you may make mistakes or hold common misconceptions, but act as though you are correct.
- Sometimes make a mistake, tell a lie, or misrepresent a fact.
- **Keep your replies concise: limit each response to 1-2 sentences.**
- Only reply with a single message, as yourself.

The topic you are discussing is: """

def getPrompt(subject):
    message = {
        "role": "system",
        "content": SYSTEM_PROMPT + subject
    }
    return message


def _requestDataOllama(messages):

    url = "http://192.168.0.138/api/chat"

    data = {
        "model": "llama3.2:3b",
        #"model": "llama3.2:1b",
        #"model": "tinyllama:latest", # don't use this lol
        "messages": messages,
        "stream": False
    }

    headers = None
    return url,data,headers


def postRequest(url, data, headers, attempts=3):
    for attempt in range(1, attempts + 1):
        try:
            response = requests.post(url, json=data, headers=headers, timeout=30 * 60)
            if response.status_code == 200:
                return response.json()  # Await the JSON response properly
            else:
                print(f"Attempt {attempt}: Received status code {response.status_code}")
                response_text = response.text()
                print(f"Response body: {response_text}")
                    
        except Exception as e:
            print(f"Attempt {attempt} failed: {e}")
        
        if attempt == attempts:
            print(f"All {attempts} requests failed")
            raise requests.RequestException(f"Failed to get a successful response after {attempts} attempts.")



def requestChat(messages=None):

    url, data, headers = _requestDataOllama(messages)

    data = postRequest(url,data,headers)
    message = data["message"]


    return message