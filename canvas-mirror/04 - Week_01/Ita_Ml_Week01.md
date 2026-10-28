# Digitalization - AI: ITA ML Week 1 slides

Source: `Ita_Ml_Week01.pdf` (87 slides). Title slide: "Digitalization - AI. IT-arkitekt. ML. Aug 26th, 2026. Sila". Condensed from extracted text only (many slides are screenshots/images that were not viewed, so some slides appear below with little content). Language: English with Danish parts.

## Intro (slides 1-5)

- Plan for the day: who am I (Simon Laub [sic: "Sila"], cand. scient. in mathematics and computer science, projects e.g. speech recognition), expectations, who are you (name, Python experience, ChatGPT experience in teaching), AI intro the rest of the day.
- Outline: AI projects (digitalization in the public sector; the JobTrend project: matching skills and jobs); AI everywhere (overview, problems, direction).

## AI projects (slides 6-19)

- **Digitalization in the Danish public sector** cases: ATP; Aalborg and Rødovre municipalities (source: DigitalLead webinar 28/9 2022; slides are images).
- **JobTrend project** (Spring 2023, article April 2023): education/job market - what skills to teach, what is in demand. Matching job ads and course materials with NLP Transformers ("Attention is all you need", 2017): split into sentences and compare using sentence transformers; plus "next steps" slide.

## AI everywhere (slides 20-35)

- Motivation/trends (source: Jeremy Wilken, VMware, MLCon 2018).
- Concepts: AI, Machine Learning, Deep Learning. Methods list: logistic regression, SVMs, decision trees, random forest, clustering (k-means, DBSCAN), neural nets, convolutions, GANs.
- "Hiding your head under a bush is not a useful technique for the future..."
- Industries that benefit from ML (Inexture presentation, 2020): medical/healthcare, marketing/sales, finance, transportation, agriculture, manufacturing, security. Transformers/NLP language models: something everyone in IT should know something about.
- AI and ML have many subfields.
- Classification problems: Ex 1 predictive maintenance (smart replacement, less planned maintenance, less service loss, IoT); Ex 2 healthcare (disease identification/diagnosis/prediction, medical imaging); Ex 3 *sometimes problematic*: prison sentences - bias, "AI is sending people to prison and getting it wrong" (MIT Technology Review, 2019).
- **Using ChatGPT: Exercise 1** (see `Exercises/Chat/chatGPT_Exercise_week01.md`).

## Zombie AI (slides 36-39)

Philosopher Shannon Vallor (Univ. of Edinburgh): many garbage/"zombie" systems keep coming; we should push them back. Problematic systems: ethical/social implications not considered; bias in training data ignored; no respect for privacy (inferring sexual orientation, emotional state, intentions, personality); method based on unscientific/doubtful science (pseudoscience such as facial features revealing character). Example: AI identifying emotion from walking style - do we want it in a local shopping mall?

## How good is AI now? (slides 40-62)

- AI in popular culture 1968-now (HAL 9000, 2001: A Space Odyssey; Arthur C. Clarke).
- **Turing test** (imitation game, 1950): a human evaluator judges natural-language conversations between human and machine; machine passes if indistinguishable.
- Blake Lemoine (Google, Jun 2022) claims LaMDA is a person ("alien intelligence of terrestrial origin").
- ChatGPT: initial release 30 Nov 2022, GPT family, fine-tuned from GPT-3.5. Ameca robot (Engineered Arts, Edinburgh Aug 2024 video).
- ChatGPT examples 1-6: good examples; failures that were later fixed; "hallucinations - will they go away? It depends who you ask".
- **Using ChatGPT: Exercise 2.**
- Is imitation (in Turing's sense) enough for intelligence? Searle: Watson doesn't know it won; a clever program that can't "think".
- GPT-4 (March 2023, arXiv 2303.12712 "Sparks of AGI"): performs at near human level across maths, coding, vision, medicine, law, psychology; possibly early AGI. Bar exam: GPT-3.5 bottom 10%, GPT-4 around 90%.
- How good is GPT-4, who is the judge? Dunning-Kruger effect; humans are clever (chimp/gravity experiments, Povinelli); language meaning is not obvious ("Bring your finest clothes to the wedding, and a hat"); meaning as "participatory sense-making" (Dirk Geeraerts); doubt and reasoning - it is not possible to rationally remove all doubt, cognitive limitations give "full beliefs" (e.g. "The Moon is made of green cheese... how do you know?"); possible way forward: models may need a "body" - the **4E approach** (embodied, embedded, enacted, extended cognition).

## Where does this end? (slides 63-68)

- "Paperclip maximiser" (Nick Bostrom, instrumental convergence).
- Asking GPT-4 which jobs it will replace (Twitter source).
- GANs: neural nets that generate e.g. images. Stable Diffusion (2022): text-to-image deep-learning model; also inpainting, outpainting, image-to-image.
- **Using ChatGPT: Exercises 3-4.**

## Python crash course (slides 69-83; Java-comparison slides from a CSE 142-style deck)

- Installing Python (python.org; Windows/Mac/Linux); interpreted language (code -> interpreter -> computer, vs Java compile + runtime); interpreter tips (Alt+P repeats previous command); docs at docs.python.org/3/.
- First program `print("Hello, world!")`; print statement, escapes (`\"`), strings in `'` or `"`; comments with `#`.
- Functions `def name():` with indented body, must be declared above main code; **whitespace/indentation is significant**.
- Variables ("a box you put things in", `A=3`); reserved words list.
- Lists: `myList = ['ko','so','kat']`, indexing from 0, `for navn in navne`, `len()`, slicing `a[start:stop]`, `a[start:]`, `a[:stop]`, `a[:]`, negative indexing (`[-1]` last item); lists can hold mixed types.
- Dictionaries: key/lookup-tag based, unordered (`purse['money'] = 12`).
- Loops: `break`, `continue`, `while True` input example.
- Functions: no overloading in Python (name alone identifies a function); default argument values (`def myfun(b, c=3, d="hello")`).
- Classes and objects: `class Hund(Dyr)` with `__init__`, `super().__init__`, `tostring`, instance `fido = Hund("Fido",2,True)`.

## Exercises and homework (slides 84-87)

- Tkinter programming reference (tutorialspoint); **group exercise (2-3):** Python program that tells whether a number is prime, with a tkinter GUI; use example code as inspiration plus the exercise text (see `Python - Getting started/Exercises_Python_GettingStarted.md`).
- **Homework:** do the week's exercises; read "Hands-On Machine Learning" (Geron) chapter 1, or the easier "Real-World Machine Learning" (Brink et al.) chapters 1-2 (What is ML, real-world data).
- Final slide: ChatGPT exercises 1-4 + Python exercises ("Hello World" + tkinter or GA assignment), see Canvas; contact sila@eaaa.dk.
