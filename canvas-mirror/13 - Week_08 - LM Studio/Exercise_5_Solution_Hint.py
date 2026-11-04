import openai
import requests
import sys

# Konfiguration af LM Studio forbindelse
client = openai.OpenAI(base_url="http://localhost:1234/v1", api_key="lm-studio")

def download_book_from_gutenberg(title):
    print(f"\n[System] Søger efter '{title}' på Project Gutenberg...")
    # Bruger Gutenberg's søge-API (via gutendex)
    search_url = f"https://gutendex.com{title}"
    
    try:
        response = requests.get(search_url).json()
        if response['results']:
            book = response['results'][0]
            # Find download link til tekst-format
            download_url = book['formats'].get('text/plain; charset=utf-8') or book['formats'].get('text/plain')
            
            if download_url:
                book_content = requests.get(download_url).text
                filename = f"{title.replace(' ', '_')}.txt"
                with open(filename, "w", encoding="utf-8") as f:
                    f.write(book_content)
                print(f"[Succes] Bogen er gemt som: {filename}\n")
                return True
        print("[Fejl] Kunne ikke finde en download-kilde til den specifikke titel.\n")
    except Exception as e:
        print(f"[Fejl] Der opstod en fejl under download: {e}")
    return False

def check_for_agreement(history):
    # System prompt til at tjekke for enighed (Beslutnings-logik)
    decision_context = history[-2:] # De sidste to beskeder
    prompt = "Er brugeren og assistenten blevet enige om en specifik bogtitel? Svar KUN med titlen hvis ja, ellers svar NEJ."
    
    response = client.chat.completions.create(
        model="local-model",
        messages=[{"role": "system", "content": prompt}] + decision_context,
        temperature=0.0 # Vi vil have et præcist svar
    )
    
    answer = response.choices[0].message.content.strip().replace(".", "")
    return None if "NEJ" in answer.upper() else answer

def start_chat():
    chat_history = [{"role": "system", "content": "Du er en bog-ekspert. Hjælp brugeren med at finde en klassisk bog fra Project Gutenberg."}]
    print("Chat startet! Skriv 'stop' for at afslutte.\n")

    while True:
        user_input = input("Dig: ")
        if user_input.lower() == 'stop':
            break

        chat_history.append({"role": "user", "content": user_input})

        # Hent svar fra LLM
        completion = client.chat.completions.create(
            model="local-model",
            messages=chat_history,
            temperature=0.7,
        )
        
        assistant_res = completion.choices[0].message.content
        print(f"\nAssistent: {assistant_res}\n")
        chat_history.append({"role": "assistant", "content": assistant_res})

        # Check for enighed
        bogtitel = check_for_agreement(chat_history)
        
        if bogtitel:
            print(f"*** Enighed fundet! Downloader: {bogtitel} ***")
            if download_book_from_gutenberg(bogtitel):
                print("Programmet afsluttes efter succesfuld download.")
                break

if __name__ == "__main__":
    start_chat()
