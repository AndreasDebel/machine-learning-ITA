from openai import OpenAI

# Her "snyder" vi biblioteket til at pege på din egen computer i stedet for OpenAI
client = OpenAI(base_url="http://localhost:1234/v1", api_key="lm-studio")

response = client.chat.completions.create(
  model="gemma-3-1b-it",
  messages=[
    {"role": "system", "content": "Du er en dansk ekspert."},
    {"role": "user", "content": "Fortæl en kort joke."}
  ]
)

print(response.choices[0].message.content)


