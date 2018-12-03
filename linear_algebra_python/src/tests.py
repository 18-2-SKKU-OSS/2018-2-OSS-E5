# -*- coding: utf-8 -*-
"""
Created on Mon Feb 26 15:40:07 2018

@author: Christian Bender
@license: MIT-license

This file contains the test-suite for the linear algebra library.
"""

import unittest
from lib import *

class Test(unittest.TestCase):
    def test_component(self):
        """
            test for method component
        """
        x = Vector([1,2,3])
        self.assertEqual(x.component(0),1)
        self.assertEqual(x.component(2),3)
        """
        x = Vector([1,2,3])에 대해
        component가 일치하는 함수가 제대로 동작하는 지를 확인한다.
        x.component(0)=1, x.component(2)=3
        """
        try:
            y = Vector()
            self.assertTrue(False)
        except:
            self.assertTrue(True)
    def test_str(self):
        """
            test for toString() method
        """
        x = Vector([0,0,0,0,0,1])
        self.assertEqual(str(x),"(0,0,0,0,0,1)")
        """
        x = Vector([0,0,0,0,0,1])에 대해
        "(0,0,0,0,0,1)"과 같은 요소들로 이루어져 있는지를 확인한다.
        str(x) = (0,0,0,0,0,1)
        """
    def test_size(self):
        """
            test for size()-method
        """
        x = Vector([1,2,3,4])
        self.assertEqual(len(x),4)
        """
        x = Vector([1,2,3,4])에 대해
        len(x)==4 라는 명령을 제대로 수행하는지를 확인한다.
        len(x)=4   (x가 갖는 원소들의 갯수)
        """
    def test_euclidLength(self):
        """
            test for the eulidean length
        """
        x = Vector([1,2])
        self.assertAlmostEqual(x.eulidLength(),2.236,3)
        """
        유클리드 거리 함수가 제대로 작동하는지를 확인
        ([1,2]) 과 원점과의 거리가 sqrt(5) 이므로,
        근사값인 2.236과의 비교를 수행한다.
        sqrt(5)=2.23606797749978969640917366873127623(almost)
        """
    def test_add(self):
        """
            test for + operator
        """
        x = Vector([1,2,3])
        y = Vector([1,1,1])
        self.assertEqual((x+y).component(0),2)
        self.assertEqual((x+y).component(1),3)
        self.assertEqual((x+y).component(2),4)
        """
        Vector 로 정의된 두 배열간의 합이 제대로 이루어졌는지에
        대한 검사. (x+y)의 원소들은 차례로 2,3,4이므로
        이 값이 제대로 저장이 되었는지를 확인한다.
        """
    def test_sub(self):
        """
            test for - operator
        """
        x = Vector([1,2,3])
        y = Vector([1,1,1])
        self.assertEqual((x-y).component(0),0)
        self.assertEqual((x-y).component(1),1)
        self.assertEqual((x-y).component(2),2)
        """
        Vector 로 정의된 두 배열간의 뺄셈이 제대로 이루어졌는지에
        대한 검사. (x-y)의 원소들은 차례로 0,1,2이므로
        이 값이 제대로 저장이 되었는지를 확인한다.
        """
    def test_mul(self):
        """
            test for * operator
        """
        x = Vector([1,2,3])
        a = Vector([2,-1,4]) # for test of dot-product
        b = Vector([1,-2,-1])
        self.assertEqual(str(x*3.0),"(3.0,6.0,9.0)")
        self.assertEqual((a*b),0)
        """
        배열에 *을 사용하였을때 값이 올바르게 저장이 되는지를 검사하는
        함수. Vector x에 대해서는 3을 곱한 값이 저장 되어 있는지를
        검사한다. Vector a와 b에 대해서는 두 벡터간의 내적 값이
        올바른 값인 0을 저장하고 있는지를 검사한다.
        """
    def test_zeroVector(self):
        """
            test for the global function zeroVector(...)
        """
        self.assertTrue(str(zeroVector(10)).count("0") == 10)
        """
        zeroVector 함수를 이용해 만들어낸 열개의 영벡터를 .count 
        메소드를 이용해 10과 일치하는지를 나타내는 함수.
        zeroVector(10)이 제대로 수행되고 있는지를 테스트한다.
        """
    def test_unitBasisVector(self):
        """
            test for the global function unitBasisVector(...)
        """
        self.assertEqual(str(unitBasisVector(3,1)),"(0,1,0)")
        """
        unitVector이며 BasisVector (크기가 1인, BasisVector)인 Vector
        을 생성해내 이가 (0,1,0)과 같은지를 테스트 하는 함수이다.
        """
    def test_axpy(self):
        """
            test for the global function axpy(...) (operation)
        """
        x = Vector([1,2,3])
        y = Vector([1,0,1])
        self.assertEqual(str(axpy(2,x,y)),"(3,4,7)")
        """
        axpy 의 이름 뜻은 alpha * x + y 으로,
        axpy(2,x,y)는 즉슨 2*x+y를 계산하는 것이며
        따라서 (3,4,7)이 되고 이 값이 제대로 나오는지를 확인하는
        함수이다.
        """
    def test_copy(self):
        """
            test for the copy()-method
        """
        x = Vector([1,0,0,0,0,0])
        y = x.copy()
        self.assertEqual(str(x),str(y))
        """
        .copy() 메소드를 불러내는 테스트함수이다.
        """
    def test_changeComponent(self):
        """
            test for the changeComponent(...)-method
        """
        x = Vector([1,0,0])
        x.changeComponent(0,0)
        x.changeComponent(1,1)
        self.assertEqual(str(x),"(0,1,0)")
        """
        .changeComponent() 메소드의 테스트함수이다.
        첫번째 인자값에 있는 Vector의 원소값을 두번째 인자값으로
        변경시켜주는 함수이며 따라서 (0,1,0)과 같은지를 확인한다.
        """
    def test_str_matrix(self):
        A = Matrix([[1,2,3],[2,4,5],[6,7,8]],3,3)
        self.assertEqual("|1,2,3|\n|2,4,5|\n|6,7,8|\n",str(A))
        """
        Matrix 메소드는 Matrix를 이루는 행과 열을 입력한 후,
        각각의 행과 열 크기를 마지막에 인자로 받아 차원을 표시한다.
        따라서 문자열 행렬인 "|1,2,3|\n|2,4,5|\n|6,7,8|\n"와
        같은지를 확인한다.
        """
    def test__mul__matrix(self):
        A = Matrix([[1,2,3],[4,5,6],[7,8,9]],3,3)
        x = Vector([1,2,3])
        self.assertEqual("(14,32,50)",str(A*x))
        self.assertEqual("|2,4,6|\n|8,10,12|\n|14,16,18|\n",str(A*2))
        """
        매트릭스와 벡터간의 곱과 매트릭스의 스칼라곱이
        수행되는것을 테스트하는 함수이다.
        """
    def test_changeComponent_matrix(self):
        A = Matrix([[1,2,3],[2,4,5],[6,7,8]],3,3)
        A.changeComponent(0,2,5)
        self.assertEqual("|1,2,5|\n|2,4,5|\n|6,7,8|\n",str(A))
        """
        .changeComponent() 메소드가 제대로 실행되고
        있는지를 확인하는 함수이다. Vector메소드의 원소변경함수와
        마찬가지로 이 테스트에선 0번째행 2번째 열에 해당하는 원소를
        (3에서) 5로 바꿔주는 함수이다. 
        """
    def test_component_matrix(self):
        A = Matrix([[1,2,3],[2,4,5],[6,7,8]],3,3)
        self.assertEqual(7,A.component(2,1),0.01)
        """
        A 행렬의 2번째 행, 1번째 열에 7이 저장되어 있는지를
        확인하는 함수이다.
        """
    def test__add__matrix(self):
        A = Matrix([[1,2,3],[2,4,5],[6,7,8]],3,3)
        B = Matrix([[1,2,7],[2,4,5],[6,7,10]],3,3)
        self.assertEqual("|2,4,10|\n|4,8,10|\n|12,14,18|\n",str(A+B))
        """
        두 행렬과의 덧셈이 이루어지는 것을 테스트하는 함수이다.
        """
    def test__sub__matrix(self):
        A = Matrix([[1,2,3],[2,4,5],[6,7,8]],3,3)
        B = Matrix([[1,2,7],[2,4,5],[6,7,10]],3,3)
        self.assertEqual("|0,0,-4|\n|0,0,0|\n|0,0,-2|\n",str(A-B))
        """
        두 행렬과의 뺄셈이 이루어지는 것을 테스트하는 함수이다.
        """
    def test_squareZeroMatrix(self):
        self.assertEqual('|0,0,0,0,0|\n|0,0,0,0,0|\n|0,0,0,0,0|\n|0,0,0,0,0|' 
        +'\n|0,0,0,0,0|\n',str(squareZeroMatrix(5)))
        """
        새롭게 만들어낸 영행렬 5개와 문자열로 이루어진 (5x5) 영행렬과의 비교를
        테스트하는 함수이다. squareZeroMatrix(5)가 이를 수행한다.
        """
        

if __name__ == "__main__":
    unittest.main()
