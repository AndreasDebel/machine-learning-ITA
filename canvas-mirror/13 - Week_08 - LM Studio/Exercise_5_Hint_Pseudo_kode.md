# Exercise_5_Hint_Pseudo_kode.txt (Danish pseudocode)

Pseudocode for the book-chat agent (Exercise 5):

1. Initialise the LM Studio connection (OpenAI-compatible) and an empty chat history.
2. Loop until the user says "stop":
   - Read user input, send chat history plus input to the LLM, and show the reply.
   - Agreement check: send the last 2 messages to the LLM with a system prompt such as "Have the user and the assistant agreed on a specific book title? Answer ONLY with the title if yes, otherwise answer NEJ."
   - If the answer is not "NEJ", the answer is the book title: print that agreement was found, run the download-book function with the title, then stop or continue.

The code hints are `Exercise_5_Hint.py` and `Exercise_5_Solution_Hint.py`; the download helpers are `download_books.py` and `download_texts.py`.
