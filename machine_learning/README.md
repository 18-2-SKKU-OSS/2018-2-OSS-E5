## 머신 러닝

### 1. 선형 회귀
이 파트에서는 경사 하강법(gradient descent)을 사용하여 선형 회귀 파라미터 θ를 찾을 것입니다.

__Hypothesis Model__
- 가설 모델 h(x)는 선형 모형에 의해 주어집니다. 

	![h theata](https://user-images.githubusercontent.com/38908132/49339027-7dab1680-f66e-11e8-91f4-0352437d0935.gif)
	
__Cost Function__

- 선형 회귀의 목표는 비용 기능을 최소화하는 것입니다. 

	![codecogseqn](https://user-images.githubusercontent.com/38908132/49338989-beeef680-f66d-11e8-8b51-a9865da43f0c.gif)

__Gradient Descent__
- 모델의 매개 변수가 θj 값임을 기억하십시오. 이것은 비용 J(θ)을 최소화하기 위해 조정할 값입니다. 이를 위한 한 가지 방법은 배치 경사 하강법(batch gradient descent)을 사용하는 것입니다. 배치 경사 하강법에서는 각 반복에서 업데이트를 수행합니다:

	![3](https://user-images.githubusercontent.com/38908132/49339052-104bb580-f66f-11e8-9068-016b9c7ef3ba.gif)

