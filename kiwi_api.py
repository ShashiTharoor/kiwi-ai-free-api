import sys
sys.path.insert(0, '/opt/')
import requests,json
from  config import KIWI_headers,KIWI_cookies


def create_chat_session():
    url = "https://kimi.ai/api/chat"
    
    data = {
        "name": "Unnamed Chat",
        "born_from": "chat",
        "kimiplus_id": "kimi",
        "is_example": False,
        "source": "web",
        "tags": []
    }

    response = requests.post(url,cookies=KIWI_cookies, headers=KIWI_headers, json=data)
    return response.json()['id']

def get_chat_completion_stream(messages,session_id=None):
    if session_id==None:
        print('creating session')
        session_id=create_chat_session()
        print(f'session_id {session_id}')
    url = f"https://kimi.ai/api/chat/{session_id}/completion/stream"
    #append only user role messages
    messages=[message for message in messages if message['role'] == 'user']
    data = {
        "kimiplus_id": "kimi",
        "extend": {"sidebar": True},
        "model": "kimi",
        "use_research": False,
        "use_search": False,
        "messages": messages,
        "refs": [],
        "history": [],
        "scene_labels": []
    }

    try:
        # Send an HTTP POST request to the URL with streaming enabled
        with requests.post(url, headers=KIWI_headers,cookies=KIWI_cookies, json=data, stream=True) as response:
            # Check the status code of the response
            if response.status_code == 200:
                # Initialize an empty string to store the text from the response
                kiwi_json_text = ""
                
                # Read the response content line by line
                for line in response.iter_lines():
                    # Filter out keep-alive frames
                    line=line.decode('utf-8').replace("b'","").replace("data: ","").replace("'","")
                    if line:
                        # Decode and load the JSON object
                        kiwi_json_object = json.loads(line)
                        # Extract the 'text' field and append to the result string
                        kiwi_json_text += kiwi_json_object.get('text', '')
                return open_ai_resp(kiwi_json_text)
            else:
                response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None



def open_ai_resp(response):
    resp={
        "id": "chatcmpl-1234567890",
        "object": "chat.completion",
        "created": 1672531188,
        "model": "kiwi",
        "choices": [
            {
            "index": 0,
            "message": {
                "role": "assistant",
                "content": response
            },
            "finish_reason": "stop"
            }
        ],
        "usage": {
            "prompt_tokens": 9,
            "completion_tokens": 12,
            "total_tokens": 21
        }
    }
    return resp



