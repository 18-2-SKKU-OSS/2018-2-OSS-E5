"""
세 개의 말뚝(L, R, C)과 지름이 서로 다른 임의의 개수의 원판이 주어진다. 
지름이 큰 원판은 항상 작은 원판보다 아래에 오도록 하며, 말뚝의 상위에 있는 한 개의 원판만을 이동시킬 수 있다. 
이와 같은 조건하에서 말뚝 L에서 말뚝 C를 이용하여 말뚝 R로 원판을 이동시키는 문제로, 문제 해결에서 수단 목표 분석의 한 예가 된다.
하노이 탑 [Hanoi tower]
"""

from __future__ import print_function
def moveTower(height, fromPole, toPole, withPole):  
    '''
    >>> moveTower(3, 'A', 'B', 'C')
    moving disk from A to B
    moving disk from A to C
    moving disk from B to C
    moving disk from A to B
    moving disk from C to A
    moving disk from C to B
    moving disk from A to B
    '''
    if height >= 1:
        moveTower(height-1, fromPole, withPole, toPole)
        moveDisk(fromPole, toPole)
        moveTower(height-1, withPole, toPole, fromPole)

def moveDisk(fp,tp):
    print(('moving disk from', fp, 'to', tp))

def main():
    height = int(input('Height of hanoi: '))
    moveTower(height, 'A', 'B', 'C')

if __name__ == '__main__':
    main()
