# Exercise: Chain of Thought (COT)

Source: `COT.pdf` (8 pages). Group exercise (2-3 people), mostly a pasted ChatGPT conversation as inspiration.

## Task
What is chain of thought (CoT) and how could it be useful? Ask ChatGPT and discuss in groups. Be inspired by conversations like the one below.

## Pasted ChatGPT conversation (summary)
1. **"Explain in simple terms what chain of thought is in LLMs."** CoT = the model reasons step by step like a person instead of jumping to the answer. Example: 15 x 12 -> 15x10=150, 15x2=30, 150+30=180. Benefits: improved accuracy (fewer errors), transparency (user can follow/verify), learning aid. "Like the model thinking out loud."
2. **"Example of a puzzle that couldn't be solved without CoT."** The three mislabeled boxes puzzle (apples / oranges / both; all labels wrong; open one box, take one fruit; the PDF says "by tasting the fruit"). Solution: open the box labeled "Apples and Oranges". If an apple comes out, that box is apples only; the box labeled "Oranges" must then be apples+oranges, and the box labeled "Apples" must be oranges. If an orange comes out: that box is oranges only, the "Apples" box is both, the "Oranges" box is apples. Explanation: needs complex deduction, elimination and logical sequencing; without CoT a model may jump to wrong conclusions.
3. **"How is CoT used in the o1 preview model?"** Internal step-by-step reasoning that breaks questions into smaller steps; more accurate/consistent; the chain of thought is usually *hidden* from the user (clean, concise answers); user can ask for it ("Explain your reasoning", "Show me the step-by-step solution"); trained on CoT-style data. Example: 60 mph for 2.5 h -> distance = speed x time = 150 miles.
