"""
선형 회귀 분석은 예측 분석에 있어서 가장 기본적이고 일반적인 회귀 분석방법 입니다.
이 아이디어는 매우 간단합니다. 우선 우리는 데이터 셋과 weights(theta)를 가지고 있습니다.
이 weitghs는 우리의 모델의 성능을 좌우하기 때문에 반드시 신중히 선택되어야 합니다.
우리는 매 itertaion을 통해 weigths를 업데이트를 하고, 가장 예측을 잘하는
weights를 선정하게 됩니다. 밑에 코드에서는, CSGO 데이터 셋을 사용했습니다. 
"""
from __future__ import print_function

import requests
import numpy as np


def collect_dataset():
    """ CSGO 데이터 셋 수집
    선수의 ADR vs Rating 정보를 가지고 있는 데이터 셋
    ;retrun : 행렬화 된 데이터 셋
    """
    response = requests.get('https://raw.githubusercontent.com/yashLadha/' +
                            'The_Math_of_Intelligence/master/Week1/ADRvs' +
                            'Rating.csv')
    lines = response.text.splitlines()
    data = []
    for item in lines:
        item = item.split(',')
        data.append(item)
    data.pop(0)  # 리스트에서 레이블을 빼내는 과정
    dataset = np.matrix(data)
    return dataset


def run_steep_gradient_descent(data_x, data_y,
                               len_data, alpha, theta):
    """ Gradient Descent 방법을 이용해 theta를 업데이트하는 함수
    :param data_x   : 데이터 셋
    :param data_y   : 결과(output)값
    :param len_data : feature의 개수
    :param alpha    : 학습률 (Learning rate)
    :param theta    : weigths
    ;return         : 업데이트된 weights(theta)
    """
    n = len_data
    
    hypothesis = np.dot(theta, data_x.transpose())
    gradient = np.dot(hypothesis-data_y.transpose(),data_x)/n
    theta = theta - alpha * gradient
    
    return theta


def sum_of_square_error(data_x, data_y, len_data, theta):
    """ 에러값 (sum of square error) 값을 반환하는 함수
    :param data_x    : 데이터셋
    :param data_y    : 결과값
    :param len_data  : feature의 개수
    :param theta     : weights
    ;return          : 에러값
    """
    hypothesis = np.dot(theta, data_x.transpose())
    error = np.mean(np.square(hypothesis - data_y.transpose())) / 2
    
    return error


def run_linear_regression(data_x, data_y):
    """ 선형회귀를 시행하는 함수
    :param data_x  : 데이터 셋
    :param data_y  : 결과값 
    ;return        : 가장 예측을 잘하는 weights
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
    """ 메인 함수 """
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
