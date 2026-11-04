# Exercise_3_Hint.txt (Danish)

Hints for calling the LM Studio server from a command prompt (Windows cmd):
- List models: `curl http://localhost:1234/v1/models`. The example output shows `gemma-3-1b-it` and `text-embedding-nomic-embed-text-v1.5`.
- Chat via the native endpoint: `POST http://localhost:1234/api/v1/chat` with JSON `{"model": "gemma-3-1b-it", "input": "Write a short haiku about sunrise."}`.
- Windows cmd version of the OpenAI-compatible call (quotes escaped as `\"`): `POST /v1/chat/completions` with `model`, `messages: [{role: user, content: ...}]` and `temperature: 0.7`. The example response is an OpenAI-style `chat.completion` object whose reply is in `choices[0].message.content`, plus `usage` token counts.
