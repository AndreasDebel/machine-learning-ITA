# Machine Learning Week 8 - lecture slides (Convolutional Neural Networks)

Source: MachineLearning_Week_08.pdf, 53 slides, 21 Oct 2026 (Sila); based on Geron "Hands-On Machine Learning" Ch. 14. Condensed from extracted text plus viewed page images (key figures described in italics).

## Today
Convolutional neural networks: churn exercise, activation functions, batch normalization, convolutions.

## Exercise 1: Churn
See Canvas (Churn/StudentChurn.md).

## Activation functions recap
- Vanishing gradient (neuralnetworksanddeeplearning.com ch. 5): in deep nets the gradient tends to get smaller moving backward through hidden layers, so early layers learn much more slowly than later ones.
- Exploding gradients also occur (contrived example in same source).
- Prompt: let ChatGPT explain why the activation function matters; ask for a simpler explanation if needed. (Several Coursera slides on activation functions.)

## Batch normalization
- Makes networks faster and more stable by re-centering and re-scaling layer inputs; fixes means and variances of layer inputs, giving faster convergence and better gradient flow.
- Enables higher learning rates: small parameter changes in one layer do not propagate to others, avoiding exploding/vanishing gradients.
*[Slide 14: diagram of a block chain: Linear1 (W1,b1) -> z1 -> Activation Function1 -> a1 -> Batch Norm1 -> bn1 -> Linear2 (W2,b2).]*
- Suggestion: ask ChatGPT and try it yourself.

## Convolutions
- Useful for processing images; scan the image to detect useful features; just element-wise products and sums.
*[Slide 30: 5x5 binary input image with a 3x3 filter (entries 1/0), first window highlighted in green, output grid 3x3 with first value 4.]*
- Filters: a vertical-edge filter highlights vertical edges, a horizontal one highlights horizontal edges.
*[Slide 36: grayscale image (columns 50,50,0,0,0) convolved with filter rows [1 0 -1], stride = 1, result rows [150 150 0]: a vertical-edge detector.]*
- Stride determines how the filter scans the image; padding is a frame around the image giving edges similar importance to the center. Without padding, edge pixels are only partially processed and the output is smaller than the input.
- Exercises 2 and 3: single conv layer detecting a line (ML_Week_11_Exercise2_Convolution.py); book example p. 492 (v2 p. 453) with strides changed to 10 (the exercise PDF says p. 491).
- Stacked conv layers example (Keras): `Conv2D(1,(3,3), input_shape=(8,8,1))` then `Conv2D(1,(3,3))` gives output shapes (6,6,1) then (4,4,1), 10 params each, 20 total; feature maps shrink, a problem for very deep networks.
*[Slide 44: cat photo before and after pooling, half size, edges kept.]*
- Pooling: 2x2 max pooling halves image size, retaining the maximum; edges are maintained and even highlighted.
- Architecture example: GoogLeNet. Links on visualizing conv and pooling layers in Keras (data-flair.training).

## Remaining exercises
Exercises 4, 5, 6 and 7 (CIFAR-10 dense net, adding conv layers, batch norm + LeakyReLU, ChatGPT convolution example); see Exercises/Exercises_Week_08.md.

## Homework
Do the exercises. Read Geron Ch. 14 (p. 481-500, optional p. 500-516).
