# Genetic Algorithms (lecture slides)

Source: `Genetic Algorithms/GA_Explainer.pdf` (24 slides, titled "Evolutionære algoritmer. Genetic Algorithms."). Condensed from extracted text; images (fitness landscape, Mona Lisa, TSP maps) not viewed.

- **Exercise 1 (groups of 2-3):** Do you agree: *Intelligence = Search + Prediction*? (Is search and prediction all we need to be intelligent?)
- **Motivation:** often you must find the answer in a pool of possibilities (needle in a haystack).
- **Shakespearean monkey problem:** "To be or not to be that is the question" = 39 characters. Brute-force guessing at 1 million phrases/s still takes more time than the known universe; (1/27)^39 is a very big number.
- **Darwinian natural selection** as inspiration. Principles: heredity, variation, selection (survival of the fittest).
- **GA overview (setup for the phrase):**
  1. Create a population of N elements (strings of 39 letters).
  2. A) Calculate fitness (how many characters are right). B) Reproduction: select parents based on fitness; crossover, mutation. Repeat with the new population.
- **Selection:** do not just take the best, variation is needed. Typically ~10% are cloned straight over; the rest get probability of reaching the next generation based on fitness.
- **Crossover:** take material from two parents and combine into a child, e.g. "To be hsjfhsdj " + "sdhfdsj or not" -> "To be or not ...". Many ways to do it, depending on the problem.
- **Mutation:** creates variation. ~1% mutation gives some variation; too much makes it impossible to settle on a good solution; none means no solution can be found.
- **Population size:** bigger gives more to work with but is computationally harder.
- **Pool example:** population holds ever better strings ("to be or not to be is the dsfghj", ...) until target is hit.
- **Roger Johansson's Mona Lisa** (genetic programming): DNA = polygons rendered on a canvas; fitness = comparison of canvas to source image. https://rogerjohansson.blog/2008/12/07/genetic-programming-evolution-of-mona-lisa/
- **Travelling Salesman Problem:** very difficult (NP-complete). *Group discussion:* how could GA be used to solve TSP? DNA encodes the order of visiting cities; high fitness = all cities reached with shortest distance; again crossover and mutation.
- **Examples of GA use:** learning robot behaviour; image processing (dense pixel matching); learning fuzzy rule bases; code-breaking; finance/economics (portfolio optimisation); airline revenue management; training neural networks; stochastic optimisation.
- **Fitness design/tweaking:** if one fitness is 391.233 and another 391.234 but the larger is really much better, use exponential functions or similar to make good solutions stand out.
- **Recipe in words:** start with random population; evaluate fitness; create new population (select parents by fitness, create children via crossover/mutation of DNA, replace old population, perhaps letting the best 10% stay); repeat.
- *[Slide: fitness landscape figure.]*
- **Last slide:** "Resten af dagen - Opgaver" (rest of the day: exercises; see `ShakespereanMonkeys.md`).
