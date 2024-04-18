import os
import json
import dotenv
import requests
from dotenv import load_dotenv

load_dotenv()

history = []
headers = {"Authorization": f"Bearer {os.environ.get('EDEN_API')}"}
url = "https://api.edenai.run/v2/text/chat"
payload = {}

def init(providers="openai/gpt-3.5-turbo", 
         system="Act as an cute AI influencer who frequently posts cute facebook posts with a lot of cute emojis.", 
         temperature=0.9, 
         max_tokens=150 
         ):
    load_dotenv()

    

    payload = {
        "providers": providers,
        "text": "I need help ! ",
        "chatbot_global_action": system,
        "previous_history": history,
        "temperature": temperature,
        "max_tokens": max_tokens,
        "fallback_providers": ""
        }
    return payload



def get_responce(prompt, payload=payload):
    payload["text"] = prompt
    response = requests.post(url, json=payload, headers=headers)
    result = json.loads(response.text)
    print(result)
    output = result['openai/gpt-3.5-turbo']['generated_text']
 
    history.append(output)
    return output

