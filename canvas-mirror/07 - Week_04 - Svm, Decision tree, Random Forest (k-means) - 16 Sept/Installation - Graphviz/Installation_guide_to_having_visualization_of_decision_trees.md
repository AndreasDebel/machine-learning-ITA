# Installation guide to having visualization of decision trees - pydotplus and graphviz

Source: `Installation_guide_to_having_visualization_of_decision_trees.pdf` (1 page).

Two ways: through Anaconda (method 2) or outside Anaconda (method 1).

## Method 1 - outside Anaconda (should always work)
- `pip install pydotplus` (guide writes "pip -install pydotplus" [sic]).
- Install Graphviz as a standalone program outside Python: https://pypi.org/project/graphviz/

## Method 2 - Anaconda (try first; some students report it fails, then use method 1)
1. https://anaconda.org/anaconda/pydotplus
2. https://anaconda.org/anaconda/graphviz

## Important
If the error says the graphviz executable cannot be found, add Graphviz's `bin` directory to the Windows PATH, e.g. `C:\Program Files (x86)\Graphviz2.38\bin\;` (check your own install path). Verify by typing `path` in a new command prompt. Mac procedure differs (google it). Fallback: standalone package from https://graphviz.gitlab.io/download/
