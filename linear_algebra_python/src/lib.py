# -*- coding: utf-8 -*-
"""
Created on Mon Feb 26 14:29:11 2018

@author: Christian Bender
@license: MIT-license

This module contains some useful classes and functions for dealing
with linear algebra in python.

Overview:

- class Vector
- function zeroVector(dimension)
- function unitBasisVector(dimension,pos)
- function axpy(scalar,vector1,vector2)
- function randomVector(N,a,b)
- class Matrix
- function squareZeroMatrix(N)
- function randomMatrix(W,H,a,b)

이 모듈에는 파이썬에서 선형 대수를 다루기 위한 유용한 클래스와 함수가 포함되어 있습니다.

개요 :

- 클래스 벡터
- 함수 제로 벡터 (치수)
- 함수 unitBaseVector (dimension, pos)
- 함수 axpy (스칼라, 벡터 1, 벡터 2)
- 함수 randomVector (N, a, b)
- 클래스 매트릭스
- 함수 squareZeroMatrix (N)
- 함수 randomMatrix (W, H, a, b)
"""


import math
import random


class Vector(object):
    """
        이 클래스는 임의 크기의 벡터를 나타냅니다.
         벡터 구성 요소를 제공해야합니다.
        
         방법에 대한 개요 :
        
         생성자 (components : list) : 벡터 초기화
         set (components : list) : 벡터 구성 요소를 변경합니다.
         __str __ () : toString 메서드
         component (i : int) : i 번째 구성 요소를 가져옵니다 (0으로 시작).
         __len __ () : 벡터 크기 (구성 요소 수)를 가져옵니다.
         euclidLength () : 벡터의 가로 길이를 반환합니다.
         연산자 + : 벡터 추가
         연산자 - : 벡터 빼기
         연산자 * : 스칼라 곱셈 및 내적 곱
         copy () :이 벡터를 복사하여 반환합니다.
         changeComponent (pos, value) : 지정된 컴포넌트를 변경합니다.
         TODO : 비교 연산자
    """
    def __init__(self,components=[]):
        """
            input : 벡터 초기화를위한 컴포넌트 또는 간단한 생성자
        """
        self.__components = list(components)
    def set(self,components):
        """
            입력 : 새 구성 요소가 벡터의 구성 요소를 변경합니다.
            새로운 구성 요소로 교체하십시오.
        """
        if len(components) > 0:
            self.__components = list(components)
        else:
            raise Exception("please give any vector")
    def __str__(self):
        """
            벡터의 문자열 표현을 반환합니다.
        """
        return "(" + ",".join(map(str, self.__components)) + ")"
    def component(self,i):
        """
            입력 : 색인 (0에서 시작)
            output : 벡터의 i 번째 성분.
        """
        if type(i) is int and -len(self.__components) <= i < len(self.__components) :
            return self.__components[i]
        else:
            raise Exception("index out of range")
    def __len__(self):
        """
            벡터의 크기를 반환합니다.
        """
        return len(self.__components)
    def eulidLength(self):
        """
            벡터의 유클리드 길이를 반환합니다.
        """
        summe = 0
        for c in self.__components:
            summe += c**2
        return math.sqrt(summe)
    def __add__(self,other):
        """
             입력 : 다른 벡터
             가정 : 다른 벡터의 크기가 동일 함
             합을 나타내는 새 벡터를 반환합니다.
        """
        size = len(self)
        if size == len(other):
            result = [self.__components[i] + other.component(i) for i in range(size)]
            return Vector(result)
        else:
            raise Exception("must have the same size")
    def __sub__(self,other):
        """
             입력 : 다른 벡터
             가정 : 다른 벡터의 크기가 동일 함
             differenz를 나타내는 새 벡터를 반환합니다.
        """
        size = len(self)
        if size == len(other):
            result = [self.__components[i] - other.component(i) for i in range(size)]
            return result
        else: # 오류의 예
            raise Exception("must have the same size")
    def __mul__(self,other):
        """
            mul은 스칼라 곱셈 및 내적을 구현한다.
        
        """
        if isinstance(other,float) or isinstance(other,int):
            ans = [c*other for c in self.__components]
            return ans
        elif (isinstance(other,Vector) and (len(self) == len(other))):
            size = len(self)
            summe = 0
            for i in range(size):
                summe += self.__components[i] * other.component(i)
            return summe
        else: # 오류의 예
            raise Exception("invalide operand!")
    def copy(self):
        """
            이 벡터를 복사하여 반환합니다.
        """
        return Vector(self.__components)
    def changeComponent(self,pos,value):
        """
            입력 : 인덱스 (pos)와 값은 'value'로 지정된 구성 요소 (pos)를 변경합니다.
        """
        # 전제 조건
        assert (-len(self.__components) <= pos < len(self.__components))
        self.__components[pos] = value
    
def zeroVector(dimension):
    """
        'dimension'크기의 0 벡터를 반환합니다.
    """        
    # 전제 조건
    assert(isinstance(dimension,int))
    return Vector([0]*dimension)


def unitBasisVector(dimension,pos):
    """
        인덱스 'pos'에 1이있는 단위 벡터를 반환합니다 (0으로 인덱싱).
    """
    #precondition
    assert(isinstance(dimension,int) and (isinstance(pos,int)))
    ans = [0]*dimension
    ans[pos] = 1
    return Vector(ans)
        

def axpy(scalar,x,y):
    """
         입력 : '스칼라'와 두 개의 벡터 'x'와 'y'
         출력 : 벡터
         axpy 연산을 계산한다.
    """
    # 전제 조건
    assert(isinstance(x,Vector) and (isinstance(y,Vector)) \
    and (isinstance(scalar,int) or isinstance(scalar,float)))
    return (x*scalar + y)
    

def randomVector(N,a,b):
    """
         입력 : 벡터의 크기 (N).
               임의의 범위 (a, b)
         출력 : 크기 N의 랜덤 벡터를 반환합니다.
                 'a'와 'b'사이의 임의의 정수 구성 요소.
    """
    random.seed(None)
    ans = [random.randint(a,b) for i in range(N)]
    return Vector(ans)


class Matrix(object):
    """
     class : 행렬
     이 클래스는 임의의 행렬을 나타냅니다.
    
     방법에 대한 개요 :
    
            __str __ () : 문자열 표현을 반환합니다.
            연산자 * : 행렬 벡터 곱셈을 구현합니다.
                         행렬 - 스칼라 곱셈을 구현합니다.
            changeComponent (x, y, value) : 지정된 컴포넌트를 변경합니다.
            component (x, y) : 지정된 구성 요소를 반환합니다.
            width () : 행렬의 너비를 반환합니다.
            height () : 행렬의 높이를 반환합니다.
            연산자 + : 행렬 - 추가를 구현합니다.
            연산자 _는 행렬 빼기를 구현합니다.
    """
    def __init__(self,matrix,w,h):
        """
           간단한 생성자는 구성 요소를 사용하여 행렬을 초기화합니다.
        """
        self.__matrix = matrix
        self.__width = w
        self.__height = h
    def __str__(self):
        """
            이 행렬의 문자열 표현을 반환합니다.
        """
        ans = ""
        for i in range(self.__height):
            ans += "|"
            for j in range(self.__width):
                if j < self.__width -1:
                    ans += str(self.__matrix[i][j]) + ","
                else:
                    ans += str(self.__matrix[i][j]) + "|\n"
        return ans
    def changeComponent(self,x,y, value):
        """
            이 행렬의 x-y 성분을 변경합니다.
        """
        if x >= 0 and x < self.__height and y >= 0 and y < self.__width:
            self.__matrix[x][y] = value
        else:
            raise Exception ("changeComponent: indices out of bounds")
    def component(self,x,y):
        """
            지정된 (x, y) 컴포넌트를 리턴한다.
        """
        if x >= 0 and x < self.__height and y >= 0 and y < self.__width:
            return self.__matrix[x][y]
        else:
            raise Exception ("changeComponent: indices out of bounds")
    def width(self):
        """
            너비에 대한 게터
        """
        return self.__width
    def height(self):
        """
            높이에 대한 게터
        """
        return self.__height
    def __mul__(self,other):
        """
             행렬 - 벡터 곱셈을 구현합니다.
             행렬 - 스칼라 곱셈을 구현합니다.
        """
        if isinstance(other, Vector): # vector-matrix 
            if (len(other) == self.__width):
                ans = zeroVector(self.__height)
                for i in range(self.__height):
                    summe = 0
                    for j in range(self.__width):
                        summe += other.component(j) * self.__matrix[i][j]
                    ans.changeComponent(i,summe)
                    summe = 0
                return ans
            else:
                raise Exception("vector must have the same size as the " + "number of columns of the matrix!")
        elif isinstance(other,int) or isinstance(other,float): # matrix-scalar
            matrix = [[self.__matrix[i][j] * other for j in range(self.__width)] for i in range(self.__height)]
            return Matrix(matrix,self.__width,self.__height)
    def __add__(self,other):
        """
            행렬 - 추가를 구현합니다.
        """
        if (self.__width == other.width() and self.__height == other.height()):
            matrix = []
            for i in range(self.__height):
                row = []
                for j in range(self.__width):
                    row.append(self.__matrix[i][j] + other.component(i,j))
                matrix.append(row)
            return Matrix(matrix,self.__width,self.__height)
        else:
            raise Exception("matrix must have the same dimension!")
    def __sub__(self,other):
        """
            행렬 - 뺄셈을 구현합니다.
        """
        if (self.__width == other.width() and self.__height == other.height()):
            matrix = []
            for i in range(self.__height):
                row = []
                for j in range(self.__width):
                    row.append(self.__matrix[i][j] - other.component(i,j))
                matrix.append(row)
            return Matrix(matrix,self.__width,self.__height)
        else:
            raise Exception("matrix must have the same dimension!")
    

def squareZeroMatrix(N):
    """
        차원 NxN의 제곱 제로 행렬을 반환합니다.
    """
    ans = [[0]*N for i in range(N)]
    return Matrix(ans,N,N)
    
    
def randomMatrix(W,H,a,b):
    """
        'a'와 'b'사이의 정수 성분을 갖는 랜덤 행렬 WxH를 반환
    """
    random.seed(None)
    matrix = [[random.randint(a,b) for j in range(W)] for i in range(H)]
    return Matrix(matrix,W,H)
            
        
