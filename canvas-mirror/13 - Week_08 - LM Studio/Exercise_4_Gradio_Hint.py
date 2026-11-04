''' Ide:

    Start LM Studio: Sørg for at "Local Server" kører på port 1234.
    Kør scriptet: Kør din Python-fil (f.eks. python min_app.py).
    Åbn browseren: Gradio vil give dig et link (typisk http://127.0.0.1:7860). Her kan du nu chatte direkte med Gemma i et pænt design.  '''


import gradio as gr
import requests
import json

# Konfiguration til LM Studio
LM_STUDIO_URL = "http://localhost:1234/v1/chat/completions"

def respond(message, history):
    # Forbered beskederne (inklusiv tidligere historik for sammenhæng)
    messages = []
    for user_msg, assistant_msg in history:
        messages.append({"role": "user", "content": user_msg})
        messages.append({"role": "assistant", "content": assistant_msg})
    
    # Tilføj den aktuelle besked fra brugeren
    messages.append({"role": "user", "content": message})

    payload = {
        "model": "gemma-3-1b-it", # Sørg for at navnet matcher din loadede model
        "messages": messages,
        "temperature": 0.7,
    }

    try:
        response = requests.post(LM_STUDIO_URL, json=payload)
        response.raise_for_status()
        
        # Hent svaret ud fra JSON
        result = response.json()
        bot_message = result['choices'][0]['message']['content']
        return bot_message

    except Exception as e:
        return f"Fejl: Kunne ikke forbinde til LM Studio. Er serveren tændt? ({e})"

# Opret Gradio ChatInterface
demo = gr.ChatInterface(
    fn=respond, 
    title="Gemma Lokal Chat",
    description="Spørg løs til din lokale Gemma model via LM Studio.",
    examples=["Hvad er en kvantecomputer?", "Skriv et haiku om kaffe."],
    theme="soft"
)

if __name__ == "__main__":
    # Start webserveren (den åbner typisk på http://127.0.0.1:7860)
    demo.launch()
