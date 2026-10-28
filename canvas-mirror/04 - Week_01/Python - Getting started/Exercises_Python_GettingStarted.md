# Exercises - Python Getting Started

Source: `Python - Getting started/Exercises_Python_GettingStarted.pdf` (6 pages, Danish; UI screenshots in the tkinter exercise not viewed). Faithful English rendering.

## Exercise 1 - Hello world

Write a program that prints "Hello World" when a variable you have read in is greater than 3. Run it from PyCharm **and** directly from the cmd prompt.

## Exercise 2 - Lists and loops

- Make a list with the surnames of your 5 favourite authors, assigned to a variable (e.g. `forfattere = ...`). Print it with a `for` loop, one author per line.
- Modify: add one more author with `append` and print again. Delete author no. 2 so you have 5 again; print.
- Length: use `len` to get the length, store in a new variable, print it.
- Reverse: print the list in reversed order.

## Exercise 3 - GUI with tkinter (groups of 2-3)

Not a GUI course; goal is a brief meeting with tkinter plus use of the day's Python constructs. **Main task:** a Python program where the user enters a number and the program answers whether it is a **prime**, with a **tkinter** GUI.

Resources: `Gui_Selvstudium.py` (Canvas), `Exercise3_ExampleCode` (Canvas), a micro tkinter tutorial (below), Google; other resources allowed.

### Micro tour of tkinter basics (step by step)

1. Show the string `"Hej, velkommen til mit program\n\n\n"` in a Label.
2. Add a **Quit** button with red text, and a **"Change Text"** button (normal text) under it; both centred (default).
3. Use a `Frame` to pack everything: `frame = tk.Frame(root); frame.pack()`; label and buttons then refer to `frame` instead of `root`. Quit button: `command=quit` (predefined). Change button: `command=change` with `def change(): pass`.
4. Change `change()` so the label becomes `"Du har trykket på change knappen!\n"` (via `label.config(text=...)`). Notice how the buttons move.
5. **Text widget** (multi-line, images, styling) with a scrollbar: `S.pack(side=tk.RIGHT, fill=tk.Y)`, `T.pack(side=tk.LEFT, fill=tk.Y)`.
6. **Entry widget** (input field) in a second frame (`frame2`) under the first: `Label(frame2, text="Indtast navn:")` packed `side=tk.LEFT, padx=10, pady=10`, and `entry = tk.Entry(frame2)`. Modify `change()` so the heading label becomes what the user typed: `input = entry.get()`.
7. **Layout managers:** `pack`, `grid`, `place` - only `pack` used here; understand why pack places the UI as it does.
