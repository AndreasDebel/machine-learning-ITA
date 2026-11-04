# Exercises. ITA-ØK. Week 8. LM Studio (Sila, 8 April 2026)

Source: `Exercises_Week_08_LmStudio.pdf`. Code files for the exercises sit next to this note (`Exercise_4_*.py`, `Exercise_5_*.py`, `download_books.py`, `download_texts.py`).

1. Download LM Studio and try it with a reasonably sized model (e.g. a Gemma model).
2. Run the model as a server and verify it works in the browser: http://localhost:1234/v1/models
3. Call the LLM from a command prompt and verify it works (see `Exercise_3_Hint.md`).
4. Use the local LLM in an agent workflow. Build a user-friendly interface for experiments. Get one of two example programs working:
   - Gradio: `OpenAI(base_url="http://localhost:1234/v1", api_key="lm-studio")`, a `predict(message, history)` function that calls `client.chat.completions.create(model="local-model", messages=..., temperature=0.7)`, launched with `gr.ChatInterface(predict).launch()`.
   - Plain `requests.post` to `http://localhost:1234/v1/chat/completions` with a system and a user message, printing `response.json()['choices'][0]['message']['content']`.
5. Write a program that chats with the LLM about books. When you and the LLM agree on a specific book (you decide how, based on LLM output), download the book (download code on Canvas; see `Exercise_5_Hint_Pseudo_kode.md`).
6. Code challenge from "Agents in Action" (Michael Lanham): Edabit "Exit the Maze", `can_exit(maze)` returns True if there is a path of 0s from the top-left to the bottom-right cell (maze of 0 = path, 1 = wall). Four test mazes are given (True, False, False, True). Start with a simpler Edabit challenge if needed. The program takes a maze, asks the LM Studio agent for Python code that solves it, then runs the returned code on the maze, so the problem is solved without writing the solution by hand. The example answer is a BFS with `deque` over the 4 neighbours. To execute the LLM's code saved to `min_kode.txt`, use `runpy.run_path('min_kode.txt')` or read the file and `exec(kode)`.
