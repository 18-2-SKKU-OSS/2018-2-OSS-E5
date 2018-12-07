# (번역)파이썬 용 선형 대수학 라이브러리

이 모듈에는 파이썬 2에서 선형 대수를 다루기위한 유용한 클래스와 함수가 포함되어 있습니다.

---

## 개요

- 클래스 벡터
    -이 클래스는 임의 크기의 벡터와 그에 대한 연산을 나타냅니다.

    ** 방법에 대한 개요 : **
        
    - 생성자 (components : list) : 벡터 초기화
    - set (components : list) : 벡터 구성 요소를 변경합니다.
    - \ _ \ _ str \ _ \ _ () : toString 메서드
    - component (i : int) : i 번째 구성 요소를 가져옵니다 (0으로 시작).
    - \ _ \ _ len \ _ \ _ () : 벡터의 크기 / 길이를 구합니다 (구성 요소 수)
    - euclidLength () : 벡터의 가로 길이를 반환합니다.
    - 연산자 + : 벡터 추가
    - 연산자 - : 벡터 빼기
    - 연산자 * : 스칼라 곱셈 및 내적 곱
    - copy () :이 벡터를 복사하여 반환합니다.
    - changeComponent (pos, value) : 지정된 컴포넌트를 변경합니다.

- 함수 제로 벡터 (치수)
    - 'dimension'의 0 벡터를 반환합니다.
- 함수 unitBaseVector (dimension, pos)
    - 인덱스 'pos'에 1이있는 단위 벡터를 반환합니다 (0으로 인덱싱).
- 함수 axpy (스칼라, 벡터 1, 벡터 2)
    - axpy 연산을 계산합니다.
- 함수 randomVector (N, a, b)
    - 'a'와 'b'사이의 임의의 정수 구성 요소를 사용하여 크기 N의 임의의 벡터를 반환합니다.

- 클래스 매트릭스
    -이 클래스는 임의의 크기와 행렬로 이루어진 행렬을 나타냅니다.

    ** 방법에 대한 개요 : **
    
    - \ _ \ _ str \ _ \ _ () : 문자열 표현을 반환합니다.
    - 연산자 * : 행렬 벡터 곱셈을 구현합니다.
                   행렬 - 스칼라 곱셈을 구현합니다.
    - changeComponent (x, y, value) : 지정된 컴포넌트를 변경합니다.
    - component (x, y) : 지정된 컴포넌트를 반환합니다.
    - width () : 행렬의 너비를 반환합니다.
    - height () : 행렬의 높이를 반환합니다.
    - 연산자 + : 행렬 추가를 구현합니다.
    - 연산자 - _는 행렬 빼기를 구현합니다.

- 함수 squareZeroMatrix (N)
    - 차원 NxN의 제곱 제로 행렬을 반환합니다.
- 함수 randomMatrix (W, H, a, b)
    - 'a'와 'b'사이의 정수 성분을 갖는 랜덤 행렬 WxH를 반환합니다.
---

## 문서

모듈은 잘 문서화되어 있습니다. 파이썬 내장```help (...)``함수를 사용할 수 있습니다.
예를 들어```help (Vector)``는 Vector 클래스에 대한 모든 정보를 제공합니다.
또는```help (unitBasisVector)``는 당신에게 필요한 모든 정보를 제공합니다.
전역 함수```unitBasisVector (...)```. 특정 정보가 필요한 경우
메소드에```help (CLASSNAME.METHODNAME)```라고 입력하십시오.

---

# Linear algebra library for Python  

This module contains some useful classes and functions for dealing with linear algebra in python 2.  

---

## Overview  

- class Vector  
    - This class represents a vector of arbitray size and operations on it.  

    **Overview about the methods:**    
        
    - constructor(components : list) : init the vector  
    - set(components : list) : changes the vector components.  
    - \_\_str\_\_() : toString method  
    - component(i : int): gets the i-th component (start by 0)  
    - \_\_len\_\_() : gets the size / length of the vector (number of components)  
    - euclidLength() : returns the eulidean length of the vector.  
    - operator + : vector addition  
    - operator - : vector subtraction  
    - operator * : scalar multiplication and dot product  
    - copy() : copies this vector and returns it.  
    - changeComponent(pos,value) : changes the specified component.  

- function zeroVector(dimension)  
    - returns a zero vector of 'dimension'  
- function unitBasisVector(dimension,pos)  
    - returns a unit basis vector with a One at index 'pos' (indexing at 0)  
- function axpy(scalar,vector1,vector2)  
    - computes the axpy operation  
- function randomVector(N,a,b)
    - returns a random vector of size N, with random integer components between 'a' and 'b'.

- class Matrix
    - This class represents a matrix of arbitrary size and operations on it.

    **Overview about the methods:**  
    
    -  \_\_str\_\_() : returns a string representation  
    - operator * : implements the matrix vector multiplication  
                   implements the matrix-scalar multiplication.  
    - changeComponent(x,y,value) : changes the specified component.  
    - component(x,y) : returns the specified component.  
    - width() : returns the width of the matrix  
    - height() : returns the height of the matrix  
    - operator + : implements the matrix-addition.  
    - operator - _ implements the matrix-subtraction  

- function squareZeroMatrix(N)  
    - returns a square zero-matrix of dimension NxN  
- function randomMatrix(W,H,a,b)  
    - returns a random matrix WxH with integer components between 'a' and 'b'  
---

## Documentation  

The module is well documented. You can use the python in-built ```help(...)``` function.  
For instance: ```help(Vector)``` gives you all information about the Vector-class.  
Or ```help(unitBasisVector)``` gives you all information you needed about the  
global function ```unitBasisVector(...)```. If you need informations about a certain  
method you type ```help(CLASSNAME.METHODNAME)```.  

---

## Usage  

You will find the module in the **src** directory its called ```lib.py```. You need to  
import this module in your project. Alternative you can also use the file ```lib.pyc``` in python-bytecode.   

---

## Tests  

In the **src** directory you also find the test-suite, its called ```tests.py```.  
The test-suite uses the built-in python-test-framework **unittest**.  
