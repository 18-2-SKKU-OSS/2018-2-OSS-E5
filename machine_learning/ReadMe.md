# Linear Regression

### Part 1: Gradient Descent

- In this part you will fit the linear regression parameters θ to our dataset using gradient descent.
- The objective of linear regression is to minimize the cost function

	![codecogseqn](https://user-images.githubusercontent.com/38908132/49338989-beeef680-f66d-11e8-8b51-a9865da43f0c.gif)

- where the hypothesis h(x) is given by the linear model

	![h theata](https://user-images.githubusercontent.com/38908132/49339027-7dab1680-f66e-11e8-91f4-0352437d0935.gif)

- Recall that the parameters of your model are the θj values. These are the values you will adjust to minimize cost  J(θ) . One way to do this is to use the batch gradient descent algorithm. In batch gradient descent, each iteration performs the update

	![3](https://user-images.githubusercontent.com/38908132/49339052-104bb580-f66f-11e8-9068-016b9c7ef3ba.gif)
