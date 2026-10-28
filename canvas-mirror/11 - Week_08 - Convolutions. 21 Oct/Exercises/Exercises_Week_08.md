# Exercises. Machine Learning. Week 8

Source: Exercises_Week_08.pdf, 4 pages, "Sila, Oct 21st, 2026"

## Exercise 1
See the StudentChurn.pdf document on Canvas (transcribed in Churn/StudentChurn.md).

## Exercise 2
Getting started with convolutional layers. Use a single convolutional layer to detect a line in some input data. See ML_Week_11_Exercise2_Convolution.py for a demo of the calculations.

## Exercise 3
Run the example from the book p. 491 (v2: p. 453); explanation there (ML_Week_11_Exercise3_Convolution.py). Change the strides parameter to 10 and see what happens. Look at output for both pictures.

## Exercise 4 (groups of 2-3)
Classify the CIFAR-10 dataset: 60.000 32x32-pixel colour images included in Keras, each in exactly 10 classes; learn the classification. Look at the code in ML_Week_11_Exercise4_DeepLearning.ipynb.

Look up the meaning of the Keras concepts Flatten and Dense layer, and explain them to each other. Then run the code; you will likely end up with a result around 50 %.
- What does this mean? Is it better than random guessing?

Extra: test another loss function and see if that helps. Read: https://keras.io/api/losses/

## Exercise 5 (groups of 2-3)
Add convolutional layers to the model of exercise 4. Code: ML_Week_11_Exercise5_Conv_DeepLearning.ipynb.

Explain the model in detail to each other, from how the input enters the model, layer to layer.

Sketch what this layer looks like and does:
```
conv_layer_1 = Conv2D(
    filters = 10
    , kernel_size = (4,4)
    , strides = 2
    , padding = 'same'
    )(input_layer)
```
Run the code. Apparently adding (naively) just these 2 convolutional layers did not help. Try with just one convolution; did it help? Try different learning_rates and numbers of epochs to get a feel for how close or far we are from a big improvement compared to the previous exercise.

## Exercise 6 (groups of 2-3)
Add convolutional layers plus batch normalization and explicitly the Leaky ReLU activation. Code: ML_Week_11_Exercise6_Conv_DeepLearning.ipynb.

Running takes (a lot) longer but should show significant improvement: around 70 % or better expected. Expect 100-150 sec per epoch depending on laptop.

Try removing some convolutions, e.g. blocks like:
```
x = Conv2D(filters = 64, kernel_size = 3, strides = 1, padding = 'same')(x)
x = BatchNormalization()(x)
x = LeakyReLU()(x)

x = Conv2D(filters = 64, kernel_size = 3, strides = 2, padding = 'same')(x)
x = BatchNormalization()(x)
x = LeakyReLU()(x)
```
Adjust the strides parameter in a layer (increasing it gives less output to the next layer). Try with and without the dropout layer (supposedly regularization). Findings will be discussed next time.

## Exercise 7 (groups of 2-3)
Work with ChatGPT to come up with your own example of using convolutions. What does ChatGPT suggest? Does it work?
