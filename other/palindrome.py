"""
Palindrome : 회문으로, 앞에서부터 읽으나 뒤에서부터 읽으나 동일한 단어나 구를 의미한다.
이 코드에서 문자열을 입력받으면 그 문자열이 Palindrome 인지 아닌지를 테스트한다.
"""
# 인자로 받은 문자열이 회문인지 아닌지를 검사
def is_palindrome(str):
    start_i = 0
    end_i = len(str) - 1
    while start_i < end_i:              # 증가하는 앞부분과 감소하는 뒷부분의 크기가 반전이 되면 회문의 발견.
        if str[start_i] == str[end_i]:  # 현 시작점과 현 마지막점의 문자가 같으면 반복 계속,
            start_i += 1
            end_i -= 1
        else:
            return False                # 한번이라도 다른 문자끼리 비교가 된다면 회문 탐색 실패.
    return True                         # 그렇지 않은 경우 참 반환


# 재귀를 통한 구현
def recursive_palindrome(str):
    if len(str) <= 1:                   # base 조건, 즉 인자의 길이가 1이 되면, 원래 문자열의 중간부분까지 탐색이 완료되었다는 것이므로 
        return True                     # 회문의 발견. 즉 참 반환
    if str[0] == str[len(str) - 1]:     # 재귀 조건, 인자의 첫 문자와 마지막 문자가 같으면, 
        return recursive_palindrome(str[1:-1])  # 그 두문자를 빼 다음 재귀함수의 인자로 전달.
    else:
        return False                    # 인자의 첫 문자와 마지막 문자가 다르면, 회문 탐색 실패, 거짓 반환


def main():
    str = 'ama'
    print(recursive_palindrome(str.lower()))
    print(is_palindrome(str.lower()))


if __name__ == '__main__':
    main()
