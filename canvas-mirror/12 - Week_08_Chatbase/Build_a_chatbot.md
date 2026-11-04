# Build an AI Chatbot (Chatbase slides)

Source: `Build a chatbot.pdf`. Slide deck; the example is a course-syllabus chatbot from a University of Montana information systems course. The later slides are screenshots of the Chatbase UI with only a few captions.

## Framework (3 questions)
1. What do you want to do, and why automate it? (Example: answer basic student questions that are answered in the syllabus or timeline, to save time.)
2. If you did it yourself: (A) steps in the process, (B) what you need, (C) how the response is delivered. (Example: read the question, look in the syllabus and timeline, answer and cite where; otherwise formulate an answer. Needs the syllabus and timeline. Answer through the same channel as the question.)
3. Guardrails: what should the agent not do? (Example: never make things up; if the answer isn't clearly in the files, refer the student to email or ask in person.)

## Chatbase.co steps
1. Training material: tell the bot what it knows (syllabus, timeline).
2. Role: set the system prompt, as in prompt engineering, under a `### Role` heading. Example: well-informed teaching assistant, professional and direct, parsimonious answers, ask clarifying questions when unclear, hopeful tone if the student is frustrated, end on a positive note, don't make up answers.
3. Constraints (`### Constraints`): no divulging that it has training data; stay focused and redirect off-topic questions; rely exclusively on training data and use a fallback response otherwise; don't perform tasks outside the role.

## Playground settings (screenshots)
- Q&A feature is not used for this bot but is useful for many.
- Model selection: GPT-4.1 Nano is the default ("ultra-low latency").
- "Temperature" sets the tone; the example picks "Reserved".
- The system prompt choice changes the instructions: role and primary function, plus constraints (guardrails).
