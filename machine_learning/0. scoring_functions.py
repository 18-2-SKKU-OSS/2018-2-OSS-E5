"""
score function
MAE(평균절대값오차), MSE (평균제곱오차)
RMSE (루트평균제곱오차), RMSLE(로그루트평균제곱오차)

이 4가지 함수들은 예측한값과 실제값의 차이를 계산하는데 쓰인다.
각각 제곱, 루트, 로그등 다양하게 에러를 구한 방법이다.
: param predict : 예측 값
: param actual  : 실제 값
"""
import numpy as np

#Mean Absolute Error
def mae(predict, actual):
    predict = np.array(predict)
    actual = np.array(actual)

    difference = abs(predict - actual)
    score = difference.mean()

    return score

#Mean Squared Error
def mse(predict, actual):
    predict = np.array(predict)
    actual = np.array(actual)

    difference = predict - actual
    square_diff = np.square(difference)

    score = square_diff.mean()
    return score

#Root Mean Squared Error
def rmse(predict, actual):
    predict = np.array(predict)
    actual = np.array(actual)

    difference = predict - actual
    square_diff = np.square(difference)
    mean_square_diff = square_diff.mean()
    score = np.sqrt(mean_square_diff)
    return score

#Root Mean Square Logarithmic Error
def rmsle(predict, actual):
    predict = np.array(predict)
    actual = np.array(actual)

    log_predict = np.log(predict+1)
    log_actual = np.log(actual+1)

    difference = log_predict - log_actual
    square_diff = np.square(difference)
    mean_square_diff = square_diff.mean()

    score = np.sqrt(mean_square_diff)

    return score

#Mean Bias Deviation
def mbd(predict, actual):
    predict = np.array(predict)
    actual = np.array(actual)

    difference = predict - actual
    numerator = np.sum(difference) / len(predict) 
    denumerator =  np.sum(actual) / len(predict)
    print(numerator)
    print(denumerator)

    score = float(numerator) / denumerator * 100

    return score
