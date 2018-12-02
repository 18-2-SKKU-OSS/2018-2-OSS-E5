"""
기본 회귀 탐색 트리의 구현
입력데이터 : 입력 데이터 셋은 연속된 라벨로 구성된 1차원의 형태를 띠어야만 합니다.
출력데이터 : 탐색트리는 실수 입력값을 실수 출력값으로 맵핑합니다.
"""
from __future__ import print_function

import numpy as np

class Decision_Tree:
    def __init__(self, depth = 5, min_leaf_size = 5):
        self.depth = depth
        self.decision_boundary = 0
        self.left = None
        self.right = None
        self.min_leaf_size = min_leaf_size
        self.prediction = None

    def mean_squared_error(self, labels, prediction):
        """
        mean_squared_error:
        @인자 라벨 : 1차원 numpy 배열
        @인자 예측 : float형 값
        반환 값 : 예측값과 라벨값에 대한 mse를 계산한 오차
        """
        if labels.ndim != 1:
            print("Error: Input labels must be one dimensional")

        return np.mean((labels - prediction) ** 2)

    def train(self, X, y):
        """
        train:
        @인자 X: 1차원 numpy 배열
        @인자 y: 1차원 numpy 배열
        y는 해당되는 X값에 대한 라벨들로 구성되어있다
        """
        """
        이 부분은 입력값들이 차원적으로 문제가 없는지 체크하는 부분이다
        """
        if X.ndim != 1:
            print("Error: Input data set must be one dimensional")
            return
        if len(X) != len(y):
            print("Error: X and y have different lengths")
            return
        if y.ndim != 1:
            print("Error: Data set labels must be one dimensional")
            return

        if len(X) < 2 * self.min_leaf_size:
            self.prediction = np.mean(y)
            return

        if self.depth == 1:
            self.prediction = np.mean(y)
            return

        best_split = 0
        min_error = self.mean_squared_error(X,np.mean(y)) * 2


        """
        쪼개진 모든 부분집합들을 검사하여 최적의 decision tree를 위한 부분을 찾아낸다.
        만약 전체 배열의 2 * error 보다 적은 부분이 존재하지 않는 경우 데이터 셋이 split하지 않은 것이고 배열 전체가 predictor로서 사용된다.
        """
        for i in range(len(X)):
            if len(X[:i]) < self.min_leaf_size:
                continue
            elif len(X[i:]) < self.min_leaf_size:
                continue
            else:
                error_left = self.mean_squared_error(X[:i], np.mean(y[:i]))
                error_right = self.mean_squared_error(X[i:], np.mean(y[i:]))
                error = error_left + error_right
                if error < min_error:
                    best_split = i
                    min_error = error

        if best_split != 0:
            left_X = X[:best_split]
            left_y = y[:best_split]
            right_X = X[best_split:]
            right_y = y[best_split:]

            self.decision_boundary = X[best_split]
            self.left = Decision_Tree(depth = self.depth - 1, min_leaf_size = self.min_leaf_size)
            self.right = Decision_Tree(depth = self.depth - 1, min_leaf_size = self.min_leaf_size)
            self.left.train(left_X, left_y)
            self.right.train(right_X, right_y)
        else:
            self.prediction = np.mean(y)

        return

    def predict(self, x):
        """
        predict:
        @인자 x: 트리의 decision boundary를 기초로 한 적절한 부분트리들의 예측 함수를 반복적으로 부름으로서 
        prediction function이 작동하는 라벨들을 예측하는 float형 값이다.
        """
        if self.prediction is not None:
            return self.prediction
        elif self.left or self.right is not None:
            if x >= self.decision_boundary:
                return self.right.predict(x)
            else:
                return self.left.predict(x)
        else:
            print("Error: Decision tree not yet trained")
            return None

def main():
    """
    이 설명에서 우리는 numpy의 sin 함수로부터 샘플 데이터들을 참조한다.
    우리는 그 데이터들로부터 decision tree를 훈련시키고 10개의 다른 test label 로부터 예측하는데 사용한다.
    또한 mean_squared error을 보여준다.
    """
    X = np.arange(-1., 1., 0.005)
    y = np.sin(X)

    tree = Decision_Tree(depth = 10, min_leaf_size = 10)
    tree.train(X,y)

    test_cases = (np.random.rand(10) * 2) - 1
    predictions = np.array([tree.predict(x) for x in test_cases])
    avg_error = np.mean((predictions - test_cases) ** 2)

    print("Test values: " + str(test_cases))
    print("Predictions: " + str(predictions))
    print("Average error: " + str(avg_error))

            
if __name__ == '__main__':
    main()
