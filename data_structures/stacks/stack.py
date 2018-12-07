from __future__ import print_function
__author__ = 'Omkar Pathak'


class Stack(object):
    """ A stack is an abstract data type that serves as a collection of
    elements with two principal operations: push() and pop(). push() adds an
    element to the top of the stack, and pop() removes an element from the top
    of a stack. The order in which elements come off of a stack are
    Last In, First Out (LIFO).

    https://en.wikipedia.org/wiki/Stack_(abstract_data_type)
    """
    '''스택은 추상 데이터 유형으로 컬렉션의 역할을합니다.
     두 가지 기본 연산  push ()와 pop ()이있습니다. push ()는
     요소를 스택 맨 위로 가져오고, pop ()은 맨 위에서 요소를 제거합니다
     스택의. 요소가 스택에서 벗어나는 순서는 다음과 같습니다.
     라스트 인 퍼스트 아웃 (LIFO).
     https://en.wikipedia.org/wiki/Stack_(abstract_data_type)
     '''

    def __init__(self, limit=10):
        self.stack = []
        self.limit = limit

    def __bool__(self):
        return not bool(self.stack)

    def __str__(self):
        return str(self.stack)

    def push(self, data):
        """ Push an element to the top of the stack."""
        #스택의 top에 원소를 push한다.
        if len(self.stack) >= self.limit:
            raise StackOverflowError
        self.stack.append(data)

    def pop(self):
        """ Pop an element off of the top of the stack."""
        #스택의 top에서 pop하여 원소를 제거한다.
        if self.stack:
            return self.stack.pop()
        else:
            raise IndexError('pop from an empty stack')

    def peek(self):
        """ Peek at the top-most element of the stack."""
        #최상위 원소를 읽어온다.
        if self.stack:
            return self.stack[-1]

    def is_empty(self):
        """ Check if a stack is empty."""
        return not bool(self.stack)

    def size(self):
        """ Return the size of the stack."""
        return len(self.stack)


class StackOverflowError(BaseException):
    pass


if __name__ == '__main__':
    stack = Stack()
    for i in range(10):
        stack.push(i)

    print('Stack demonstration:\n')
    print('Initial stack: ' + str(stack))
    print('pop(): ' + str(stack.pop()))
    print('After pop(), the stack is now: ' + str(stack))
    print('peek(): ' + str(stack.peek()))
    stack.push(100)
    print('After push(100), the stack is now: ' + str(stack))
    print('is_empty(): ' + str(stack.is_empty()))
    print('size(): ' + str(stack.size()))
