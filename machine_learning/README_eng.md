## Machine Learning GuideLine

### 1. Linear Regression
In this part of exercise you will fit the linear regression parameters θ to our dataset using gradient descent.

__Hypothesis Model__
- The hypothesis h(x) is given by the linear model

	![h theata](https://user-images.githubusercontent.com/38908132/49339027-7dab1680-f66e-11e8-91f4-0352437d0935.gif)
	
__Cost Function__

- The objective of linear regression is to minimize the cost function

	![codecogseqn](https://user-images.githubusercontent.com/38908132/49338989-beeef680-f66d-11e8-8b51-a9865da43f0c.gif)

__Gradient Descent__
- Recall that the parameters of your model are the θj values. These are the values you will adjust to minimize cost  J(θ) . One way to do this is to use the batch gradient descent algorithm. In batch gradient descent, each iteration performs the update

	![3](https://user-images.githubusercontent.com/38908132/49339052-104bb580-f66f-11e8-9068-016b9c7ef3ba.gif)


### 2. Logistic Regression
In this part of the exercise, you will implement the cost and gradient for logistic regression.

__Hypothesis Model__
- Before you start with the actual cost function, recall that the logistic regression hypothesis is defined as:
	
	![4](https://user-images.githubusercontent.com/38908132/49339107-31f96c80-f670-11e8-9722-b81b12ab64e8.gif)

__Sigmoid Function__
- where functino g is the sigmoid function. The sigmoid function is defined as:

	![codecogseqn](https://user-images.githubusercontent.com/38908132/49339128-69681900-f670-11e8-9efc-5832bc513138.gif)

__Cost Function__
- Now you will implement the cost function and gradient for logistic regression.
- The cost function in logistic regression is
	
	![6](https://user-images.githubusercontent.com/38908132/49339154-fad78b00-f670-11e8-8aa4-bd5e2ff23b9a.gif)

__Gradient Descent__
- The gradient of the cost is a vector of the same length as θ where the jth element (for j = 0,1,...,d) is defined as follows:

	![7](https://user-images.githubusercontent.com/38908132/49339182-64f03000-f671-11e8-9309-95809ff07230.gif)

### 3. Perceptorn
In this part, you will implement the perceptron. 

__Hypothes Model__
- The perceptron is defined as:

	![default](https://user-images.githubusercontent.com/38908132/49377601-f2a14d80-f74d-11e8-8228-5eb90681b0a7.PNG)

__Cost Function__
- Now you will implement the cost function and update rule for perceptron. The cost function in perceptron is

	![codecogseqn](https://user-images.githubusercontent.com/38908132/49377749-54fa4e00-f74e-11e8-8338-e65da50baec6.gif)

__Gradient Descent__
- and the gradient of perceptron is a vector of the same length as θ where the jth element (for j = 0,1,...,d) is defined as follows:

	![codecogseqn](https://user-images.githubusercontent.com/38908132/49377879-a1de2480-f74e-11e8-81d6-7af83c435bb5.gif)
	
- Note that while this gradient looks identical to the linear regression gra- dient, the formula is actually different because linear and logistic regression have different definitions of hθ(x).

url: https://www.codecogs.com/latex/eqneditor.php
