# Vibe coding rules

Source: `Vibe_Coding_Rules.pdf`, 3 pages. Author: Sila, January 25th, 2026. Second half in Danish.

## Six pillars
- Specs: make goals, constraints and acceptance criteria explicit before agents start building.
- Human control: keep people where decisions carry real risk and responsibility.
- Agentic Engineering: give autonomous agents clear roles, boundaries, tools and coordination.
- Harness Engineering: use tests, rules, feedback loops and guardrails to catch and correct failures.
- Architecture & Security: set boundaries before generated code reaches critical systems.
- Governance & Quality: define what AI-generated software must prove before production.

Reference: "From Vibe to AI-driven Software Engineering": https://vibekode.it/blog/ai-driven-software-engineering-vibe-coding/

## "Med flere ord" (in more words; Danish, translated) - extensions per pillar
1. Specs
   - Executable specifications: explicit examples (Given-When-Then, input-output pairs) are understood far better by AI agents than abstract goals.
   - Architectural frames: the agent must know the code standard (functional programming, SOLID, a specific design pattern) before starting, otherwise it guesses the style.
2. Human control
   - From human-in-the-loop to human-on-the-loop: define exactly when a human must approve; control sits at architecture review (before start) and pull request / code review (before integration), not every line.
   - Intent vs. output: the human's role shifts from writing code to validating that the agent's understanding matches the real business need.
3. Agentic Engineering
   - State management and memory: agents fail on long tasks through "context drift"; need a clear structure for sharing knowledge (shared "blackboard" architecture or git branches).
   - Deterministic tools: give agents tools with unambiguous answers (AST parsers, linters, sandboxed CLIs) rather than only probabilistic LLM logic.
4. Harness Engineering
   - Self-healing loops: feed test output (e.g. stack trace) back to the agent automatically so it fixes its own errors.
   - Test-quality evaluation (mutation testing): agents may write tests that always pass (no real asserts) to hit coverage targets; the harness must validate that tests are robust.
5. Architecture & Security
   - Sandboxing during development: run/test in isolated environments (Docker, short-lived cloud) without internal network or real API keys.
   - Static vulnerability scanning: AI reuses known patterns that can introduce classic vulnerabilities (SQL injection, hardcoded credentials); run automated scanners on all agent-generated code.
6. Governance & Quality
   - AI provenance: Git should show which code an agent wrote, from which prompt/spec, and who approved it.
   - Technical debt: AI generates huge amounts of code fast; ensure it is readable and maintainable by humans, not just working now.
