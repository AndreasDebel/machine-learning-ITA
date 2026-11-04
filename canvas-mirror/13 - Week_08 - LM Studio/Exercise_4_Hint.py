import requests
import json

# Opsætning af URL og data
url = "http://localhost:1234/v1/chat/completions"
headers = {"Content-Type": "application/json"}

data = {
    "model": "gemma-3-1b-it",
    "messages": [
        {"role": "user", "content": "Write a short haiku about sunrise."}
    ],
    "temperature": 0.7
}

# Send forespørgslen
try:
    response = requests.post(url, headers=headers, data=json.dumps(data))
    response.raise_for_status()  # Tjekker for fejl
    
    # Udpak svaret
    result = response.json()
    answer = result['choices'][0]['message']['content']
    
    print("Gemma svarer:\n")
    print(answer)

except requests.exceptions.RequestException as e:
    print(f"Fejl i forbindelsen til LM Studio: {e}")


# -----------


