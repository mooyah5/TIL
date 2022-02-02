# Python 기초



### 자료형

- 불린형 0, 0.0, (), [], {}, '', None
- 문자열
- None
- 수치형
  - int
    - 8진수 : 0o (0ctal)
    - 2진수 : 0b (binary)
    - 16진수 : 0x (hexadecimal)
  - float
  - comple



### 오버플로우

데이터 타입 별로 사용 가능한 메모리 크기가 제한되어 있는데,

표현 가능한 수 범위를 넘어가는 연산 시 기대값이 출력되지 않는 현상.

메모리를 넘어선 상황.



### 임의 정밀도 산술

현재 남아있는 만큼의 가용 메모리를 모두 수 표현에 끌어다 쓸 수 있는 형태



### datetime

```python
import datetime
today = datetime.datetime.today()
print(today)

print(f'오늘은 {today:%Y}년 {today:%m}월 {today:%d}일 {today:%A}')
# 오늘은 2022년 02월 02일 Wednesday
```



### 실수 연산

3.5 - 3.12 = 0.37999999999999

round(3.5-3.12, 2) = 0.38

3.5 - 3.12 == 0.38 = False

#### 처리방법

1. abs()

   ```python
   a = 3.5-3.12
   b = 0.38
   abs(a-b) <= 1e-10
   # True
   ```

2.  sys 모듈

   ```python
   import sys
   abs(a-b) <= sys.float_info.epsilon
   # True
   ```

3. python 3.5부터 가능한 math 모듈

   ```python
   import math
   math.isclose(a, b)
   ```



### 문자열

1. Immutable (변경 불가)
2. Iterable (순회 가능)



### 컨테이너

여러 개의 값을 저장할 수 있는 객체

서로 다른 자료형을 저장할 수 있다.

1. 시퀀스형 - 순서 O
   - 리스트 (가변형, mutable)
   - 튜플 (불변형, immutable)
   - 레인지 (불변형)
2. 비 시퀀스형 - 순서 X
   - 세트 (가변형)
   - 딕셔너리 (가변성)



### 단축평가

- 첫 번째 값이 확실할 대, 두 번째 값은 확인하지 않는다.
- 조건문에서 뒷 부분 판단이 필요 없어, 속도가 향상된다.

```python
print ('a' and 'b') 	# b
print ('a' or 'b')		# a

vowels = 'aeiou'

print('a' and 'b' in vowels) # False
print('b' and 'a' in vowels)	 # True

print(3 and 5)	# 5
print(3 and 0)	# 0
print(0 and 3)	# 0
print(0 and 0)	# 0

print(5 or 3)	# 5
print(3 or 0)	# 3
print(0 or 3)	# 3
print(0 or 0)	# 0
```

- and
  - 둘 다 T일 경우에만 T
  - 첫 값이 True라도 두번째 값을 확인해야 함
- or
  - 하나만 T면 T
  - True를 만나면 바로 반환



### 프로그램 구성 단위

#### 1. 식별자 identifier

- 변수, 함수, 클래스 등 프로그램이 실행되는 동안 다양한 값을 가질 수 있는 이름
- 예약어는 사용 불가

#### 2. 리터럴 literal

- 읽혀지는 대로 쓰여있는 값 그 자체

#### 3. 표현식 Expression

- 새로운 데이터 값을 생성하거나 게산하는 코드 조각

#### 4. 문장 Statement

- 특정한 작없을 수행하는 코드 전체
- 파이썬이 <u>실행 가능</u>한 최소한의 코드 단위



- 표현식은 값을 생성하는 일부분
- 문장은 특정 작업을 수행하는 코드 전체

![image-20220202190257312](C:\Users\SSAFY_hanna\AppData\Roaming\Typora\typora-user-images\image-20220202190257312.png)

#### 5. 함수 Function

- 특정 명령을 수행하는 함수 묶음

#### 6. 모듈 Module

- 함수/클래스의 모음 or 하나의 프로그램을 구성하는 단위

#### 7. 패키지 Package

- 프로그램과 모듈의 묶음
  - 프로그램 : 실행하기 위한 것
  - 모듈 : 다른 프로그램에서 불러와 사용하기 위한 것

#### 8. 라이브러리 Library

- 패키지의 모음