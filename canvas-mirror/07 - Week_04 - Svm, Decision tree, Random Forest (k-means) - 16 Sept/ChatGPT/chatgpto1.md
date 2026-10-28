# Test of ChatGPT o1-preview (Sila, September 15th, 2024)

Source: `chatgpto1.pdf` (42 slides, Sila, September 15th 2024). Slides are screenshots of ChatGPT o1-preview sessions with Sila's one-line captions. Condensed transcription from viewing all pages.

## Intro (p.1-5)
- p.1 title; p.2 "Two riddles for chatgpt o1 preview": PROBLEM -> SEE WHAT IT DOES -> EVALUATE.
- p.3 OpenAI "Learning to Reason with LLMs": o1 ranks in the 89th percentile on Codeforces, places among top 500 US students in the AIME qualifier, exceeds human PhD-level accuracy on GPQA (physics, biology, chemistry); o1-preview released in ChatGPT and to trusted API users.
- p.4 OpenAI tweet: o1 is a new series of models designed to spend more time thinking before responding; harder problems in science, coding, math.
- p.5 Medium article "Tech Review: OpenAI o1 / Strawberry - a new PhD reasoning model": hidden chain-of-thought, test-time compute, more thinking time gives more accurate results (10-20 s).

## Riddle 1: three fruit boxes (p.6-8)
Prompt: three boxes (apples, pears, mixed); all labels are wrong; how can I take one fruit from one box (without looking) and relabel correctly? o1-preview (thought 11 s): pick from the box labelled "Mixed Fruits" (it must be pure apples or pears); if apple, that box is apples, the box labelled "Pears" cannot be pears or apples so it is mixed, and the "Apples" box is pears (symmetric for a pear); swap labels accordingly.
Sila: "Thats nice. The old model chatGPT-o couldn't solve this a couple a month ago." (Correct.)

## Riddle 2: switch box (p.9-42)
Prompt (typos in original): a wooden box with a hole on each side (north, east, south, west); inside each hole is a switch, on or off, starting random. Goal: put all switches in the same position (all up or all down). You may touch only 2 switches at a time. After you feel/set them, a super-intelligent robot spins the box; the new position is chosen by its algorithm and unknown to you. Again you may change only two switches. What do you do to get all switches in the same position as fast as possible, with a guarantee of being done before the robot's 6th rotation?

Attempt 1 (33 s, p.10-14): set everything to "on": each move touch any two holes, flip "off" to "on", leave "on". Claims every switch is touched within 6 moves. Sila: "Guaranteed...." Follow-up p.15: Sila says this is not correct since you might reach the same 2 switches each time.

Attempt 2 (64 s, p.15-18): apologizes; says it is impossible to guarantee, since the robot can always present the same two switches; suggests extra constraints (limit rotations, touch three switches, feedback). Sila: "Baaah...." Sila (p.19) replies that you decide which holes to reach into (N+S, then E+W, and so on).

Attempt 3 (50 s thinking trace, shown in Danish, p.20-24; then English answer p.24-28): strategy of reaching into every pair of holes (6 unique pairs: NE, NS, NW, ES, EW, SW), one pair per move, setting both switches to "on". Claims the robot cannot prevent access to any switch. Sila (p.29): not correct again; moves 1,3,4,6 could set the same 2 switches, and likewise 2 and 5, so one switch may remain off; improve.

Attempt 4 (65 s, p.30-33): concedes the earlier flaw; proposes toggling N and E on all six moves, with a "why this works: inevitability of accessing all switches" argument. Sila (p.34-35): the robot can land the box in the same position so you always touch the same 2 switches; strategy fails. o1 (33 s): states the problem as given is unsolvable; conclusion: impossible to guarantee all switches equal in six (or any finite number of) moves. Sila: "No, no .... This is NOT correct...." and "No,no there is a solution..." (p.36-37).

Attempt 5 (56 s, p.38-39): Sila insists you choose holes and flips and a guaranteed strategy exists. o1 gives plan: moves 1-2 reach NE then SW and set both "on". Sila: "Hmmmm.... here we go again..." Sila (p.40, 75 s reply): N and E, and S and W, could be the same 2 holes after rotation, so 2 holes may never be reached; "you are incorrect." Sila caption "hmmm...."

## "Solution to the Puzzle" (p.41)
Sila's reference solution (adjacent pairs of holes NS = north-south pair, EW = east-west pair, "SE" = a diagonal pair as written):
1. NS: flip both on.
2. SE: flip both on. At least 3 switches are now on; the last must be flipped off (otherwise you win after this step) [sic].
3. NS: flip 1 switch off (if one is already off flip it on and win). After this step the 2 on switches are next to each other, likewise the 2 off switches.
4. SE: flip both switches regardless of state. If both on, switching to off makes 4 off and you win; if both off, 4 on and you win. Otherwise the on switches are across from each other and off switches across from each other.
5. SE: flip both switches regardless of state. The switches are in the same state across from each other, so flipping the pair makes all 4 the same. You win.
(Classic "four switches / spinning box" puzzle: solved in at most 5 moves.)

p.42 closing slide: "Well, Well...."

Takeaway: o1-preview solved the fruit riddle at once but failed the switch riddle after five attempts, repeatedly asserting guarantees or impossibility and only conceding after user corrections; it never reached the solution.
