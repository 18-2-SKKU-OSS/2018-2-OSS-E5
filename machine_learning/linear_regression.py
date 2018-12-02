"""
선형 회귀 분석은 예측 분석에 있어서 가장 기본적이고 일반적인 회귀 분석방법 입니다.
이 아이디어는 매우 간단합니다. 우선 우리는 데이터 셋과 feature를 가지고 있습니다.
이 features는 우리의 모델의 성능을 좌우하기 때문에 반드시 신중히 선택되어야 합니다.
우리는 매 itertaion을 통해 feature weigths를 업데이트를 하고, 가장 예측을 잘하는
weights를 선정하게 됩니다. 밑에 코드에서는, CSGO 데이터 셋을 사용했습니다. 
"""
from __future__ import print_function

import requests
import numpy as np


def collect_dataset():
    """ Collect dataset of CSGO
    The dataset contains ADR vs Rating of a Player
    :return : dataset obtained from the link, as matrix
    """
    response = requests.get('https://raw.githubusercontent.com/yashLadha/' +
                            'The_Math_of_Intelligence/master/Week1/ADRvs' +
                            'Rating.csv')
    lines = response.text.splitlines()
    data = []
    for item in lines:
        item = item.split(',')
        data.append(item)
    data.pop(0)  # This is for removing the labels from the list
    dataset = np.matrix(data)
    return dataset


def run_steep_gradient_descent(data_x, data_y,
                               len_data, alpha, theta):
    """ Run steep gradient descent and updates the Feature vector accordingly_
    :param data_x   : contains the dataset
    :param data_y   : contains the output associated with each data-entry
    :param len_data : length of the data_
    :param alpha    : Learning rate of the model
    :param theta    : Feature vector (weight's for our model)
    ;param return    : Updated Feature's, using
                       curr_features - alpha_ * gradient(w.r.t. feature)
    """
    n = len_data

    prod = np.dot(theta, data_x.transpose())
    prod -= data_y.transpose()
    sum_grad = np.dot(prod, data_x)
    theta = theta - (alpha / n) * sum_grad
    return theta


def sum_of_square_error(data_x, data_y, len_data, theta):
    """ Return sum of square error for error calculation by vectorized computation
    :param data_x    : contains our dataset
    :param data_y    : contains the output (result vector)
    :param len_data  : len of the dataset
    :param theta     : contains the feature vector
    :return          : sum of square error computed from given feature's
    """
    hypothesis = np.dot(theta, data_x.transpose())
    error = np.mean(np.square(hypothesis - data_y.transpose())) / 2
    
    return error


def run_linear_regression(data_x, data_y):
    """ Implement Linear regression over the dataset
    :param data_x  : contains our dataset
    :param data_y  : contains the output (result vector)
    :return        : feature for line of best fit (Feature vector)
    """
    iterations = 100000
    alpha = 0.0001550

    no_features = data_x.shape[1]
    len_data = data_x.shape[0] - 1

    theta = np.zeros((1, no_features))

    for i in range(0, iterations):
        theta = run_steep_gradient_descent(data_x, data_y,
                                           len_data, alpha, theta)
        error = sum_of_square_error(data_x, data_y, len_data, theta)
        print('At Iteration %d - Error is %.5f ' % (i + 1, error))

    return theta


def main():
    """ Driver function """
    data = collect_dataset()

    len_data = data.shape[0]
    data_x = np.c_[np.ones(len_data), data[:, :-1]].astype(float)
    data_y = data[:, -1].astype(float)

    theta = run_linear_regression(data_x, data_y)
    len_result = theta.shape[1]
    print('Resultant Feature vector : ')
    for i in range(0, len_result):
        print('%.5f' % (theta[0, i]))


if __name__ == '__main__':
    main()
