# Machine Learning - Week 5 slides (Neural Nets)

Source: `MachineLearning_Week_05.pdf` (57 slides, "Sila, Sept 23rd 2026"). Condensed summary from extracted text; diagram-only slides described briefly.

## Program
Comments on last week's exercises; intro and history; neural networks and training; applications; exercises.

## Recap of last week
- **K-Means:** inertia = sum of squared distances between each point and its centroid (summed over clusters); low is good. Elbow method: choose K where the decrease in inertia starts to slow (K=3 in the example plot). Good model = low inertia AND few clusters.
- Discuss in groups (2-3): decision trees and random forest; problems/observations; your Comedians solution; your circles-dataset solution (Exercise 5: classification on other data, circles dataset, labeled).
- **Hard vs soft voting:** hard = pick the prediction with most votes; soft = combine (average) the probabilities of each model and pick the class with highest total probability.
- **Diabetes dataset exercise:** see `Exercise - Diabetes/Diabetes_DataSet_Exercise.md`.

## Intro to neural nets
- NNs are everywhere: AI-generated movie script (https://youtu.be/LY7x2Ihqjmc), trained with LSTMs (http://colah.github.io/posts/2015-08-Understanding-LSTMs/); Gen AI inspirational video from Veed (March 2024).
- ANN example: learning to walk. Inspiration from the brain: biological neuron model.
- **History:** introduced 1943 (Warren McCulloch); revival in the 1980s with better training algorithms; other methods took over; huge revival in the last ~10 years (faster computers, more data). AlphaGo/AlphaZero use NNs.
- **Neurons simulate OR, AND, NOT gates** (perceptrons): neuron C fires when input evaluates true; AND needs both A and B; OR needs one; NOT = B inhibits firing.
- **Neuron output:** z = sum(w_i * x_i), output h(z). Example: input (2,3,5), weights (1,2,-1) -> z = 2*1+3*2+5*(-1) = 3, h(3) = 1, which feeds the next neuron.
- **Activation functions:** step function; sigmoid/logistic (once popular, biological); **ReLU** f(x) = max(0,x) is better for ANNs (Glorot & Bengio, 2010), "a major breakthrough", fast to compute; **Softplus** f(x) = log(1+exp(x)) is a smooth, everywhere-differentiable ReLU.
- **Limitation of perceptrons:** cannot do XOR. Fix: combine several gates -> **Multi Layer Perceptron** computes XOR.

## NN training
- Fully connected layers; any number of hidden layers/inputs/outputs; more than 1 hidden layer = "deep learning".
- **How many layers/neurons?** 1 hidden layer is enough for most problems; 2-3 layers sometimes converge faster. Input neurons = number of features. Output neurons match the target (binary classification = 1 neuron). Rule of thumb: hidden size between output and input layer sizes; no hard rule, experiment.
- **Training:** adjust edge weights so the correct output is produced for as many training inputs as possible; needs labeled data (supervised). Iterative; training is NP-hard (no guarantee of optimal weights). Most common: **back-propagation** (Rumelhart et al., 1985), a variant of gradient descent.
- **Backprop in words:** forward pass for each training instance -> compare to the true output -> compute error -> go back layer by layer adjusting weights to reduce error (gradient descent step) -> repeat until convergence or stop. Does not require input normalization (per the slide). Can run in batch mode (update weights after several samples; faster). Not guaranteed to find the optimum but works very well in practice.
- *[Slides: pseudo code for 1 hidden layer (Wikipedia); figure of forward propagation (black) and backward propagation (red) updating W[1], W[2], b[1], b[2]; chain-rule derivation of delta w with sigmoid activations.]* See also `BackProp.md`.
- **Simulator:** http://playground.tensorflow.org/ -> Exercises 1-3 in Playground TensorFlow Exercises.

## Applications and frameworks
- Image recognition (TensorFlow tutorials), AlphaGo (NN evaluates positions and selects moves; supervised on expert moves, then reinforcement learning by self-play, with Monte Carlo tree search), AlphaZero (reinforcement learning).
- **Frameworks:** implementing ANNs from scratch is slow; use TensorFlow (Google, open source, desktop/cloud/mobile via TF Lite, version 2, general purpose), Keras (higher level), scikit-learn (limited NN support since 0.18).
- TensorFlow has two phases: construction (build graph) and execution (run data). Example: variables x=3, y=4, f = x*x*y + y + 2 = 42 (TF1-style session code on the slide). General workflow: load/prepare data, define model, train, evaluate, predict.
- MNIST with TensorFlow: 100 training iterations, accuracy 0.9745 (97.45 %), approx 20 minutes on a good laptop. TensorBoard for visualizing graphs.

## Exercises in class
- **Exercises 2-5:** in groups (2-3), discuss and agree on answers, write them down, draw the 3 activation functions yourself; discussed in class afterwards.
- **Exercise 6** (Iris MLP tutorial; start in class) and **Exercise 7** (blobs): questions A-D as in `Exercises/Exercises_Week_05.md`.

## Homework (Week 5)
All exercises. Literature: Hands-On ML chapter 10, pp. 299-317, 344-353 (v.3); chapter 11 optional.

## Figure notes (from page images)
- *[Slide 12: "ANN Example: Learning to walk" - video thumbnail "DeepMind AI learned how to walk" showing a simulated humanoid figure running.]*
- *[Slide 24: "Neurons can simulate OR, AND & NOT gates. But not Xor." - XOR truth table (0,0->0; 0,1->1; 1,0->1; 1,1->0, Y = X1 xor X2) and 2D plots showing the XOR points cannot be separated by a single line (two lines L1, L2 are needed).]*
- *[Slide 26: section title "Neural Networks and training".]*

## Additional figure notes (all 57 slides viewed)
- *[Slide 3: K-means inertia vs number of clusters k=1..7 line plot; steep drop to k=3 then flat (elbow at K=3).]*
- *[Slides 5-6: voting diagram. Hard voting: M1=1, M2=1, M3=0 -> majority 1. Soft voting (slide 8): M1 1:80%/0:20%, M2 1:90%/0:10%, M3 1:20%/0:80% -> average of 1 = 63%, average of 0 = 36.6% -> predicts 1.]*
- *[Slide 10 (NN everywhere): still from the AI-written short film; slide 9 divider "Intro to Neural Networks".]*
- *[Slide 13: photo of stained/fluorescent biological neurons. Slide 14: labelled biological neuron: dendrites, nucleus, cell body, axon, synapses.]*
- *[Slide 16: perceptron gate diagrams: C = A, C = A AND B, C = A OR B, C = A AND NOT B (inhibitory connection from B drawn with a minus circle); legend: ^ = AND, v = OR, not = NOT.]*
- *[Slide 17: single neuron diagram: inputs x1..x3, weights w1..w3, weighted sum z = w^T x, step(z); h_w(x) = step(w^T x). Heaviside(z) = 0 if z<0, 1 if z>=0; sgn(z) = -1, 0, +1 for z<0, =0, >0.]*
- *[Slide 18: sigmoid S(x) = 1/(1+e^-x) = e^x/(e^x+1); ReLU f(x) = max(0,x). Slide 19: sigmoid S-curve plot on [-6,6], 0 to 1, 0.5 at x=0.]*
- *[Slide 20: plot of ReLU (rectifier, purple, flat 0 then linear) and Softplus (green, smooth curve above it) on x in [-4,4].]*
- *[Slide 21: Minsky and Papert (1969) showed simple perceptrons cannot do XOR; book cover "Perceptrons" (expanded edition); XOR truth table.]*
- *[Slide 22: Boolean functions and perceptrons: AND (weights 1,1, threshold t=1.5), OR (t=0.5), NOT (weight -1, t=-0.5), with 2D plots; AND/OR separable by one line L1/L2, XOR is not.]*
- *[Slide 23: linear decision boundary: w0 + sum w_i x_i = 0; > 0 gives y=1, < 0 gives y=0.]*
- *[Slide 25: XOR solved by a 2-layer network: hidden threshold units with weights/biases shown (-0.5, -1, -1.5, 0.5, +1) and inputs x1, x2; plot shows the shaded band separating the XOR classes.]*
- *[Slide 27: "What is a Neural Network": 3 input nodes, 4 hidden nodes, 2 output nodes, fully connected.]*
- *[Slide 32: Wikipedia pseudo code: initialize weights (small random values); do: for each training example: prediction = neural-net-output(network, ex) // forward pass; actual = teacher-output(ex); compute error at output units; compute delta w_h for hidden->output weights (backward pass); compute delta w_i for input->hidden weights (backward pass continued); update network weights (input layer not modified by error estimate); until all examples classified correctly or another stopping criterion satisfied; return the network.]*
- *[Slides 33-34: computation graph z[1] = W[1]x + b[1] -> a[1] = sigma(z[1]) -> z[2] = W[2]a[1] + b[2] -> a[2] = sigma(z[2]) -> L(a[2], y); black arrows forward, red arrows backward. Slide 34 adds the chain-rule derivative list (dZ[2] = A[2] - Y, dW[2] = dZ[2] A[1]T, db[2], dA[1], dZ[1] = W[2]T dZ[2] * sigma'(Z[1]), dW[1] = dZ[1] X^T, ...) and the binary cross-entropy loss L(y_hat, y) = -[y log y_hat + (1-y) log(1-y_hat)].]*
- *[Slide 35: 1D curve with a global maximum, local maximum, local minimum and global minimum - gradient descent can get stuck in a local minimum.]*
- *[Slide 38: image-recognition examples (TensorFlow tutorials): mite, container ship, motor scooter, leopard with top-5 prediction bar charts (e.g. mite, black widow, cockroach, tick, starfish). Slide 39: Lee Sedol press photo (AlphaGo). Slide 40: AlphaZero documentary still plus the Bing quote.]*
- *[Slide 44: logos of companies using TensorFlow (Airbnb, NVIDIA, Uber, SAP, Kakao, DeepMind, Dropbox, eBay, Google, Snapchat, Intel, Coca-Cola, Xiaomi, ZTE, Qualcomm, Twitter).]*
- *[Slide 46: TensorFlow architecture stack: training libraries / inference libs; Python client, C++ client; C API; distributed master + dataflow executor; kernel implementations (Const, Var, MatMul, Conv2D, ReLU, Queue); networking layer (RPC, RDMA) and device layer (CPU, GPU).]*
- *[Slide 48: TF code (x=3, y=4, f = x*x*y+y+2, result 42) beside the TensorBoard computation graph (x, y, mul, mul_1, add, add_1, init nodes). Slide 50: grid of MNIST handwritten digits with labels. Slide 51: training-error curve over 100 iterations, dropping steeply then flat. Slide 52: TensorBoard screenshot.]*
- *[Slide 54-56: Exercise 6 slide shows questions A-D; Exercise 7 slide is a header only; Homework slide.]*
