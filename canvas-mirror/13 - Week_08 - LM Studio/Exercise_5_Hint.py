from openai import OpenAI
import time

# Opsætning til LM Studio
client = OpenAI(base_url="http://localhost:1234/v1", api_key="lm-studio")
MODEL = "gemma-3-1b-it"

def download_book(title):
    """Her indsætter du din kode fra Canvas til at downloade bogen."""
    print(f"\n--- SYSTEM: Downloader nu '{title}'... ---")
    time.sleep(2) # Simulerer download
    print(f"--- SYSTEM: '{title}' er hentet! ---\n")

def check_for_agreement(history):
    """Spørger modellen i baggrunden om der er enighed om en bog."""
    check_prompt = (
        "Analyser den korte samtale herunder. Er brugeren og assistenten blevet enige om "
        "en specifik bog, som de anbefaler eller vil downloade? "
        "Hvis ja: Svar KUN med bogens titel. Hvis nej: Svar KUN med ordet 'NEJ'."
    )
    
    # Vi sender kun de sidste par beskeder for at spare tid
    context = history[-2:]
    
    response = client.chat.completions.create(
        model=MODEL,
        messages=[{"role": "system", "content": check_prompt}] + context,
        temperature=0.0 # Vi vil have et præcist ja/nej svar
    )
    
    answer = response.choices[0].message.content.strip()
    return None if "NEJ" in answer.upper() else answer

def chat_loop():
    print("--- Bog-Chat startet (skriv 'exit' for at slutte) ---")
    history = [{"role": "system", "content": "Du er en bog-ekspert. Snak med brugeren om bøger."}]

    while True:
        user_input = input("Dig: ")
        if user_input.lower() in ["exit", "quit", "stop"]:
            break

        history.append({"role": "user", "content": user_input})

        # 1. Generer svar til brugeren
        response = client.chat.completions.create(
            model=MODEL,
            messages=history,
            temperature=0.7
        )
        bot_answer = response.choices[0].message.content
        print(f"\nGemma: {bot_answer}\n")
        history.append({"role": "assistant", "content": bot_answer})

        # 2. Check for enighed (baggrunds-check)
        agreed_book = check_for_agreement(history)
        
        if agreed_book:
            print(f"DEBUG: Detekterede enighed om: {agreed_book}")
            download_book(agreed_book)
            print("Vi har fundet en bog! Vil du tale om en anden? (eller skriv 'stop')")

if __name__ == "__main__":
    chat_loop()

