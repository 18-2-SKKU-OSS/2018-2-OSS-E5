"""
수학에서 카오스 기계는 의사 랜덤 오라클을 생성하기 위해 카오스 이론 
(주로 결정론적 카오스)의 기초 위에 만들어진 알고리즘의 클래스입니다. 
무작위성과 민감성이 필요한 곳이라면 언제든지 적용 할 수있는 
모듈 식 디자인과 사용자 지정 가능한 매개 변수를 사용하여 보편적 인 계획을 세우는 아이디어를 나타냅니다.

이론 모델은 Maciej A. Czyzewski에 의해 2015 년 초에 출판되었습니다. 
해시 함수와 의사 무작위 함수의 이점을 결합하여 특별히 설계되었습니다. 
그러나 이것은 암호화 해시, 메시지 인증 코드 및 난수 추출기를 포함하는 많은 암호화 기본 요소를 구현하는 데 사용될 수 있습니다.
"""

"""간단한 카오스 머신의 예"""
from __future__ import print_function

try:
  input = raw_input  # 파이썬 2
except NameError:
  pass               # 파이썬 3

# 카오스 머신 (K, t, m)
K = [0.33, 0.44, 0.55, 0.44, 0.33]; t = 3; m = 5

# 버퍼 공간 (매개 변수 공간 포함)
buffer_space, params_space = [], []

# 머신 시간
machine_time = 0

def push(seed):
  global buffer_space, params_space, machine_time, \
    K, m, t

  # 동적 시스템 선택 (모두)
  for key, value in enumerate(buffer_space):
    # 진화 매개 변수
    e = float(seed / value)

    # 제어 이론 : 궤도 변경
    value = (buffer_space[(key + 1) % m] + e) % 1

    # 제어 이론 : 탄도 변화
    r = (params_space[key] + e) % 1 + 3

    # 변경 (전환 기능) - 점프
    buffer_space[key] = \
      round(float(r * value * (1 - value)), 10)
    params_space[key] = \
      r # 매개 변수 공간에 저장

  # 물류지도
  assert max(buffer_space) < 1
  assert max(params_space) < 4

  # 머신 타임
  machine_time += 1

def pull():
  global buffer_space, params_space, machine_time, \
    K, m, t

  # PRNG (George Marsaglia의 Xorshift)
  def xorshift(X, Y):
    X ^= Y >> 13
    Y ^= X << 17
    X ^= Y >> 5
    return X

  # 동적 시스템 선택 (증가)
  key = machine_time % m

  # 진화 (시간 길이)
  for i in range(0, t):
    # 변수 (위치 + 매개 변수)
    r     = params_space[key]
    value = buffer_space[key]

    # 변경 (전환 기능) - 흐름
    buffer_space[key] = \
      round(float(r * value * (1 - value)), 10)
    params_space[key] = \
      (machine_time * 0.01 + r * 1.01) % 1 + 3

  # 혼돈 데이터 선택하기
  X = int(buffer_space[(key + 2) % m] * (10 ** 10))
  Y = int(buffer_space[(key - 2) % m] * (10 ** 10))

  # 머신 타임
  machine_time += 1

  return xorshift(X, Y) % 0xFFFFFFFF

def reset():
  global buffer_space, params_space, machine_time, \
    K, m, t

  buffer_space = K; params_space = [0] * m
  machine_time = 0

#######################################

# 초기화
reset()

# 입력값 대입
import random
message = random.sample(range(0xFFFFFFFF), 100)
for chunk in message:
  push(chunk)

# 제어를 위함
inp = ""

# 결과값 출력
while inp in ("e", "E"):
  print("%s" % format(pull(), '#04x'))
  print(buffer_space); print(params_space)
  inp = input("(e)exit? ").strip()
