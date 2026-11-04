from lmstudio import LMStudioClient

client = LMStudioClient() # Forbinder automatisk til localhost:1234

# Hent den model der er loadet
model = client.llm.model("gemma-3-1b-it")

# Lav en forudsigelse (streaming er indbygget nemt her)
prediction = model.respond("Hvad er hovedstaden i Danmark?")

for chunk in prediction:
    print(chunk.content, end="", flush=True)


### 

