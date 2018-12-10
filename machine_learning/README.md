## 머신 러닝

### 1. 선형 회귀
이 파트에서는 경사 하강법(gradient descent)을 사용하여 선형 회귀 파라미터 θ를 찾을 것입니다.

__가설 모델__
- 가설 모델 h(x)는 선형 모형에 의해 주어집니다. 

	![h theata](https://user-images.githubusercontent.com/38908132/49339027-7dab1680-f66e-11e8-91f4-0352437d0935.gif)
	
__비용 함수__
- 선형 회귀의 목표는 비용(cost)를 최소화하는 것입니다. 

	![codecogseqn](https://user-images.githubusercontent.com/38908132/49338989-beeef680-f66d-11e8-8b51-a9865da43f0c.gif)

__경사 하강법__
- 모델의 매개 변수가 θj 값임을 기억하십시오. 이것은 비용 J(θ)을 최소화하기 위해 조정할 값입니다. 이를 위한 한 가지 방법은 배치 경사 하강법(batch gradient descent)을 사용하는 것입니다. 배치 경사 하강법에서는 각 반복에서 업데이트를 수행합니다:

	![3](https://user-images.githubusercontent.com/38908132/49339052-104bb580-f66f-11e8-9068-016b9c7ef3ba.gif)

### 2. 로지스틱 회귀
이 파트에서는 로지스틱 회귀 분석을 위한 비용과 경사 하강법을 구현할 것 입니다.

__가설 모델__
- 비용 함수(cost function)를 구현하기 전에 로지스틱 회귀 가설 모델을 다음과 같이 정의할 것입니다:
	
	![4](https://user-images.githubusercontent.com/38908132/49339107-31f96c80-f670-11e8-9722-b81b12ab64e8.gif)

__활성 함수: 시그모이드 함수__
- 활성함수 g는 시그모이드 함수(igmoid function)이며, 다음과 같이 정의됩니다:

	![codecogseqn](https://user-images.githubusercontent.com/38908132/49339128-69681900-f670-11e8-9efc-5832bc513138.gif)

__비용 함수__
- 이제 우리는 로지스틱 회귀를 위한 비용 함수와 경사 하강법을 구현할 것입니다.
- 비용 함수는 다음과 같이 정의 됩니다:
	
	![6](https://user-images.githubusercontent.com/38908132/49339154-fad78b00-f670-11e8-8aa4-bd5e2ff23b9a.gif)

__경사 하강법__
- 비용 함수의 미분값(gradient)는 θ와 동일한 길이의 벡터로서, θ의 j (j = 0,1,...,d)번째 요소는 다음과 같이 정의 됩니다:

	![7](https://user-images.githubusercontent.com/38908132/49339182-64f03000-f671-11e8-9309-95809ff07230.gif)
