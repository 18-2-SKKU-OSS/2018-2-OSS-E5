"""
로지스틱 회귀 분석은 Classification(분류) 문제에 있어서 가장 기본적인 회귀분석 방법입니다.
로지스틱 모형의 결과값은 조건부확률(P(y|x))이며, 여기에서는 연결함수로 sigmoid 함수를 
사용하였습니다. sigmoid 함수는 결과값이 항상 [0,1]사이에 있게 하며, 값이 1에 가까울 수록
target 값이 1일 확률이 높다는걸 나타냅니다.
"""

import numpy as np
import matplotlib.pyplot as plt

from sklearn import datasets

def sigmoid_function(z):
    """ sigmoid 함수
    :return : sigmoind 함수 반환값
    """
    return 1 / (1 + np.exp(-z))


def cost_function(h, y):
    """ cost 함수
    :param h : 예측 값
    :param y : 실제(target) 값
    ;return  : error 값
    """
    return (-y * np.log(h) - (1 - y) * np.log(1 - h)).mean()

def logistic_reg(alpha, X, y, max_iterations=70000,):
    """ 로지스틱 회귀 실행
    :param alpha : 학습률
    :param X     : 데이터 셋
    :param y     : 결과(target) 값
    ;return      : 업데이트된 weights(theta)
    """
    converged = False
    iterations = 0
    theta = np.zeros(X.shape[1])

    while not converged:
        z = np.dot(X, theta)
        hypothesis = sigmoid_function(z)
        gradient = np.dot(X.T, h - y) / y.size
        theta = theta - alpha * gradient

        z = np.dot(X, theta)
        hypothesis = sigmoid_function(z)
        J = cost_function(h, y)

        iterations += 1

        if iterations == max_iterations:
            print ('Maximum iterations exceeded!')
            print ('Minimal cost function J=', J)
            converged = True

    return theta

if __name__ == '__main__':
    iris = datasets.load_iris()
    X = iris.data[:, :2]
    y = (iris.target != 0) * 1

    alpha = 0.1
    theta = logistic_reg(alpha, X, y, max_iterations=70000)
    print (theta)


    def predict_prob(X):
        """ 계산한 theta를 바탕으로 예측
        ;return : 예측값
        """
        return sigmoid_function(np.dot(X, theta))  


    plt.figure(figsize=(10, 6))
    plt.scatter(X[y == 0][:, 0], X[y == 0][:, 1], color='b', label='0')
    plt.scatter(X[y == 1][:, 0], X[y == 1][:, 1], color='r', label='1')
    (x1_min, x1_max) = (X[:, 0].min(), X[:, 0].max())
    (x2_min, x2_max) = (X[:, 1].min(), X[:, 1].max())
    (xx1, xx2) = np.meshgrid(np.linspace(x1_min, x1_max),
                             np.linspace(x2_min, x2_max))
    grid = np.c_[xx1.ravel(), xx2.ravel()]
    probs = predict_prob(grid).reshape(xx1.shape)
    plt.contour(xx1, xx2, probs, [0.5], linewidths=1, colors='black',)
    plt.legend()
