# break
#   : 가장 가까이서 둘러싸는 반복문 빠져나감 (for, while)

# 루프문은 else 절을 가질 수 있다.
#   반복 가능한 자료형의 소진(for) 혹은 조건 거짓(while)이 되어 종료할 때 실행
#   그러나 break로 종료할 때는 실행되지 않는다.

#   여기서 else절은 if문이 아니라 for 루프에 속한다.
#   루프와 함께 사용될 때, else 절은 if문보다는 try문의 else절과 비슷하게 사용됨
#   try 문의 else절은 예외가 발생하지 않을 때 실행되고, 루프의 else절은 break가 발생하지 않을 때 실행됨

for i in range(2, 10):
    for j in range(2, i):
        if i % j == 0:
            print(i, 'equlas', j, '*', i//j)
            break
    else:
        # loop fell through without finding a factor
        print(i, 'is a prime number')

'''
2 is a prime number
3 is a prime number
4 equals 2 * 2
5 is a prime number
6 equals 2 * 3
7 is a prime number
8 equals 2 * 4
9 equals 3 * 3
'''


## continue
#   : 루프의 다음 반복절에서 계속하도록 만든다.
for num in range(2, 10):
    if num % 2 == 0:
        print("found an even number", num)
        continue
    print("found an odd number", num)

'''
Found an even number 2
Found an odd number 3
Found an even number 4
Found an odd number 5
Found an even number 6
Found an odd number 7
Found an even number 8
Found an odd number 9
'''

## pass
#   : 아무것도 하지 않음
#   문법적으로는 문장이 필요하지만, 프로그램이 특별히 할 일이 없을 때 사용
while True:
    pass
#   최소한의 클래스를 만들 때
class MyEmptyClass:
    pass
#   새 코드 작업 시 함수나 조건부 바디의 자리 채움
def initlog(*args):
    pass

