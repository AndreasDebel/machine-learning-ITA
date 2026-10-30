# Model comparison for section C

Learning aid, not handed in. The five course models that can predict `Survived`. Linear regression, k-means, PCA and CNN are ruled out.

## Side by side

|                                          | Logistic regression                                   | SVM                                                      | Decision tree                                | Random forest                                              | MLP                                                              |
|------------------------------------------|-------------------------------------------------------|----------------------------------------------------------|----------------------------------------------|------------------------------------------------------------|------------------------------------------------------------------|
| **Core idea**                            | Weighted sum of features, sigmoid gives a probability | Widest possible street between the classes               | Chain of yes/no questions that reduce gini   | Many trees on random samples, averaged                     | Layers of neurons, trained by backpropagation                    |
| **Boundary shape**                       | Straight                                              | Straight, or curved with a kernel                        | Boxes                                        | Averaged boxes                                             | Curved                                                           |
| **Interactions** (e.g. `Sex` x `Pclass`) | Only if added by hand                                 | Yes, with `rbf` or `poly` kernel                         | Yes, via the order of questions              | Yes                                                        | Yes, learned by hidden neurons                                   |
| **Output**                               | Probability                                           | Class; probability is an add-on                          | Probability (share in the leaf)              | Probability (average of trees)                             | Probability                                                      |
| **Explainable?**                         | High: read the weights                                | Medium if linear, low with kernels                       | High if shallow                              | Low: 100 trees cannot be read                              | Low: hidden neurons have no set meaning                          |
| **Scaling**                              | Recommended                                           | Needed                                                   | Not needed                                   | Not needed                                                 | Needed                                                           |
| **Main parameters**                      | `C`                                                   | `kernel`, `C`, `gamma`, `degree`                         | `max_depth`                                  | `n_estimators`, tree depth                                 | `hidden_layer_sizes`, `max_iter`, `batch_size`, activation       |
| **Overfitting risk**                     | Low; rises with high `C`                              | Rises with high `gamma`                                  | High without a depth limit                   | Lower than one tree                                        | Rises with network size; `(8,8)` has 153 learned numbers         |
| **Stability**                            | Stable                                                | Stable                                                   | Unstable: small data changes alter the tree  | Stable: quirks average out                                 | Result varies with `random_state`                                |
| **Pros**                                 | Simple, fast, clear reasons, good baseline            | Margin should generalise well; flexible with kernels     | Easy to read and draw; no data assumptions   | Often strong with default settings; steadier than one tree | Flexible; learns interactions itself; the course's Titanic model |
| **Cons**                                 | Misses interactions by default                        | Harder to explain; many settings; no default probability | Overfits; unstable                           | Hard to explain; slower                                    | Hard to explain; many settings; no guaranteed best solution      |
| **In the course**                        | Weeks 3-4: Zombie, bank loan                          | Weeks 3-4: Iris, breast cancer                           | Week 4: Iris, moons, comedians               | Weeks 4 and 7: moons, bank loan, digits                    | Weeks 5-7: Titanic (Ex 5), spine, bank loan                      |
| **Cross-validation accuracy**            | 0.792 (+/- 0.064)                                     | 0.795 (+/- 0.069) linear, 0.820 (+/- 0.062) rbf          | 0.817 (+/- 0.041) `max_depth=3`              | 0.800 (+/- 0.053) 100 trees                                | 0.819 (+/- 0.056) `(8,8)`                                        |
| **Section C argument**                   | Simple and explainable; a fair start                  | Possible, but hard to explain in one page                | Shows its reasoning and handles interactions | Fixes the tree's instability                               | Follows the course's Titanic exercise                            |

**Cross-validation:** 5-fold on the 640 training passengers with all 8 features, default settings unless shown. The number after +/- is the spread between folds. "Always predict died" scores 0.616. The test set was not used, and these are not section D results.

## Similarities

- All five learn from labelled examples (supervised learning) and solve binary classification.
- All use the same prepared data and are judged by the same section D measures.
- All can overfit, and each has parameters that control it, which suits section E.
- A neuron is close to a logistic regression, and a forest is built from decision trees, so the models come in related pairs.

## Differences that matter most

- **Linear or not:** logistic regression and linear SVM draw a straight boundary; the others do not need to.
- **Rules or weights:** trees ask questions one feature at a time; the others combine all features at once.
- **One model or many:** the forest is the only ensemble (combined group of models).
- **Explainable or flexible:** the simpler models show their reasoning; the flexible ones trade that away.

## Sources

Pros, cons and parameters follow the Week 3-7 slides and exercises (`canvas-mirror/INDEX.md`). The explainability, stability and scaling rows for tree and forest, and the section C row, are teaching judgement rather than course statements.
