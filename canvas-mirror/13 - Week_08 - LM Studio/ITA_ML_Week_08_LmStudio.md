# ITA-ØK Week 8 - LM Studio (lecture slides)

Source: `ITA_ML_Week_08_LmStudio.pdf` (17 slides). Figures and book excerpts are from "AI Agents in
Action" by Michael Lanham. Every figure slide below was viewed as an image (slides 3-7 and 9-15);
slides 1, 2, 8, 16 and 17 contain only a title.

## Slide 3 - Prompting an LLM: clear instructions
Figure "Tactics for Strategy: Writing Clear Instructions". Six tactics, each with an example:
1. **Detailed queries** - give as much detail as you can. "Who's the prime minister?" is worse than
   "Who is the prime minister of Canada, and how frequently are elections held?".
2. **Adopting personas** - a SYSTEM message such as "You are a prompt expert..." sets who the model
   acts as. Personas can include demographics, knowledge and personality.
3. **Using delimiters** - triple quotes separate the text to work on from the instructions
   (e.g. "Summarize the text delimited by triple quotes with a limerick").
4. **Specifying steps** - spell out Step 1, Step 2 (summarize, then translate to French). Helps the
   model, but keep the number of steps limited.
5. **Providing examples** - a USER/ASSISTANT example pair shows the desired style
   ("Teach me about patience" -> a poetic answer, then "Teach me about the ocean"). This is
   few-shot learning.
6. **Specify output length** - in words, bullet points or other metrics (e.g. "about 50 words").

## Slide 4 - Listing 2.9 `detailed_queries.jsonl`
Two chat payloads (JSON lists of `role`/`content` messages), both with system message "You are a
helpful assistant.":
- General: user asks "What is an agent?".
- Specific: user asks "What is a GPT Agent? Please give me 3 examples of a GPT agent".

Shows that a more specific question, plus a request for examples, improves the answer.

## Slide 5 - Listing 2.10 `adopting_personas.jsonl`
Same user question both times: "What is the best subject to study." Only the system message differs:
- First persona: a 20 year old female college computer-science student answering as a junior
  programmer.
- Second persona: a 38 year old male registered nurse answering as a medical professional.

Same question, different persona -> different answer.

## Slides 6-7 - Add more knowledge/files to the prompt
- Slide 6: screenshot of the ChatGPT GPT builder "Knowledge" section. A PDF
  (`calculus_made_easy.pdf`) is uploaded via "Upload files"; adding files gives the assistant
  additional static knowledge. Capabilities ticked: Web Browsing, DALL-E Image Generation and
  Code Interpreter (enable it so the assistant can demonstrate concepts). Below it is a book excerpt
  describing how to create the GPT (My GPTs -> Configure tab -> upload the book).
- Slide 7: the book's exercise: *Objective - build an assistant with specialized knowledge from
  uploaded documents.* Tasks: pick a free e-book or document collection; upload it to a new GPT
  assistant and configure it as an expert; write prompts that test whether it can reference and
  summarize the documents; evaluate it and adjust for accuracy and helpfulness.

## Slide 8 - Running LLMs in LM Studio; prompt engineering
Title slide for the hands-on part (no figure).

## Slides 9-12 - More agents working on a task
- Slide 9: **user proxy agent + assistant agent** (AutoGen style). The human talks to the user proxy
  agent, which runs code in a shell with a human in the loop. The assistant agent (an LLM configured
  to write Python) does the actual task. Worked example: "Plot a chart of META and TESLA stock price
  change YTD" -> assistant writes code -> proxy runs it -> error "package yfinance is not installed"
  -> assistant says to `pip install yfinance` and re-run -> chart of price in $. The user then asks
  "No, please plot % change!" and gets revised code and a % chart. This is the evaluation and
  feedback loop between proxy and assistant.
- Slides 10 and 12: **CrewAI "Crew"** diagram with four layers. Agents (researcher, writer), each
  with a goal and backstory as persona; Tasks ("research on this {topic}", "write on this topic");
  Tools (search, call APIs, access data); Memory (conversational, task specific, semantic, with RAG
  patterns). Processing can be sequential or hierarchical. A picture of cartoon worker robots is
  decorative.
- Slide 11: book text "Enhancing code output with agent critics" plus two AutoGen layouts.
  *Nested chat*: the user proxy starts a chat with the engineer, the engineer's message goes to the
  critic, the critic replies with suggested updates and changes. *Group chat*: user proxy, engineer
  and critic collaborate through a group chat manager that routes all messages.

## Slides 13-15 - Agents calling functions
- Slide 13: **function (tool) calling flow**. A request goes to the LLM with messages and a tool
  definition (user asks for recommendations on time travel movies, recipes and gifts; tool is a
  `recommend` function). The GPT confirms the request matches the function definition and creates 3
  function replies, returning the function name and parameters for each. Your code executes the
  functions, adds the results to the conversation history, and asks the LLM again (same or a
  different LLM) to answer in natural language covering all three recommendations.
- Slide 14: **behaviour tree calling pattern**, figure 6.1 from the book. Behaviour trees come from
  robotics and game AI (Brooks, 1986). Node types: selector/fallback (`?`), sequence (`->`),
  condition (e.g. "Has apple") and action (e.g. "Eat apple"). Example tree numbered 1-7: root
  selector -> sequence (Has apple, Eat apple) or sequence (Has pear, Eat pear). Execution flows top to
  bottom, then left to right.
- Slide 15: book text. Every node returns success or failure, including conditions and selectors.
  **Agentic behaviour trees (ABTs)** use prompts to direct actions and conditions; because prompt
  results are somewhat random they could be called stochastic behaviour trees.

## Slide 16 - Prompting the LM Studio server
Title slide only (no figure): the "Running LLMs in LM Studio / Prompt engineering" slide with the
subtitle "Prompting LM Studio Server".

## Slide 17 - Exercises 1-6
See `Exercises_Week_08_LmStudio.md`.
