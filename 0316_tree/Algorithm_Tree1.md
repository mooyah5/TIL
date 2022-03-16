# Algorithm - 0314 Tree 1

## 1. 정의

- 1개 이상의 노드로 이루어진 유한 집합
- 조건
  - 노드 중 최상위 노드 : 루트(root)
  - 나머지 노드들은 0개 이상의 분리 집합으로 분리되어 subtree라 한다.
  - 정점 = node = Vertex
  - 단말노드 = leaf node
- 비선형구조
  - 트리 = 1:N
  - 그래프 = N:N



## 2. 트리 용어정리

- 노드(node) - 트리의 원소
- 간선(edge) - 노드 연결선. 부모와 자식 노드를 연결
- 루트노드(root node) - 트리의 시작 노드
- 형제노드(sibling node) - 같은 부모 노드의 자식 노드들
- 조상노드 - 간선을 따라 루트까지 이르는 경로에 있는 모든 노드들
- 서브트리(subtree) - 부모와 연결된 간선을 끊었을 때 생성되는 트리
- 자손노드 - 서브트리에 있는 하위 레벨의 노드들
- 차수(degree) 
  - 노드 차수 - 노드에 연결된 자식 노드의 수
  - 트리 차수 - 트리에 있는 노드차수 중 가장 큰 값
  - 단말 노드(leaf node) - 차수가 0인 노드. 자식 없는 노드.
- 높이
  - 노드 높이 : 루트 ~ 노드까지의 간선 수 (노드의 레벨)
  - 트리 높이 : 가장 높은 높이 (최대 레벨)



## 3. 이진트리

- 모든 노드들이 최대 2개의 서브트리를 갖는 특별한 형태의 트리
  - 왼쪽 자식 : left child node
  - 오른쪽 자식 : right child node
  - 자식이 없을 수도(0~2개)
- 레벨 i에서의 노드 최대 개수는 2**i 개
- 높이가 h인 이진 트리가 가질 수 있는 노드 최소 개수 = h+1개
- 높이가 h인 이진트리가 가질 수 있는 노드 최대 개수 = 2**(h+1)-1



### 포화이진트리 (Full Binary Tree)

- 모든 레벨에 노드가 포화 상태로 차 있는 이진 트리

- 높이가 h일 때, 최대의 노드 개수인 2**(h+1)-1 의 노드를 가진 이진 트리

  - 높이가 3일 때 2**(3+1)-1 = 15개의 노드

- 루트를 1번으로 하여 최대 노드수까지 정해진 위치에 대한 노드 번호를 가짐

  ![image-20220316190645878](C:\Users\baekh\AppData\Roaming\Typora\typora-user-images\image-20220316190645878.png)



### 완전 이진 트리 (Complete Binary Tree)

- 높이가 h이고 노드 수가 n개일 때, 포화이진트리의 노드 번호 1번부터 n번까지 빈자리가 없는 이진트리



### 편향 이진 트리 (Skewed Binary Tree)

- 높이 h에 대한 **최소 개수 **의 노드를 가지면서 한쪽 방향의 자식 노드만을 가진 이진 트리

  - 왼쪽 편향 이진트리

    ![image-20220316191009552](C:\Users\baekh\AppData\Roaming\Typora\typora-user-images\image-20220316191009552.png)

  - 오른쪽 편향 이진 트리

    ![image-20220316191024462](C:\Users\baekh\AppData\Roaming\Typora\typora-user-images\image-20220316191024462.png)



### 순회 Traversal

- 트리의 각 노드를 중복되지 않게 전부(빠짐없이 중복없이) 방문하는 것

- 트리는 비선형구조이므로, 선형구조처럼 선후연결관계는 알 수 없음

- 3가지의 기본 순회법

  - 전위순회 VLR (preorder traversal)

    - 부모 - 좌자식 - 우자식

    - 수행방법

      1. 현재노드 n을 방문하여 처리 -> V
      2. 현재노드 n의 왼쪽 서브트리로 이동 -> L
      3. 현재노드 n의 오른쪽 서브트리로 이동 -> R

    - 알고리즘

      ```python
      def preorder(T):
      	if T :
      		visit(T)		# print(T.item)
      		preorder(T.left)
      		preorder(T.right)
      ```

  - 중위순회 LVR (inorder traversal)

    - 좌자식 - 부모 - 우자식

    - 수행방법

      1. 현재노드 n의 왼쪽 서브트리로 이동 -> L
      2. 현재노드 n을 방문하여 처리 -> V
      3. 현재노드 n의 오른쪽 서브트리로 이동 -> R

    - 알고리즘

      ```python
      def preorder(T):
      	if T :
      		preorder(T.left)
      		visit(T)		# print(T.item)
      		preorder(T.right)
      ```

  - 후위순회 LRV (postorder traversal)

    - 좌자식 - 우자식 - 부모

    - 수행방법

      1. 현재노드 n의 왼쪽 서브트리로 이동 -> L
      2. 현재노드 n의 오른쪽 서브트리로 이동 -> R
      3. 현재노드 n을 방문하여 처리 -> V

    - 알고리즘

      ```python
      def preorder(T):
      	if T :
      		preorder(T.left)
      		preorder(T.right)
      		visit(T)		# print(T.item)
      ```



### 순회 순서 알아보기

![image-20220316191914389](C:\Users\baekh\AppData\Roaming\Typora\typora-user-images\image-20220316191914389.png)

- 전위 순회 : A B D H I E J C F K G L M
- 중위 순회 : H D I B J E A K F C L G M
- 후위 순회 : H I D J E B K F L M G A C



### 배열을 이용한 이진트리 표현

![image-20220316192206185](C:\Users\baekh\AppData\Roaming\Typora\typora-user-images\image-20220316192206185.png)

- 완전(혹은 포화)이진트리 형태로 부여
- 이진 트리에 각 노드 번호를 0부터 부여
- 루트 번호 = 1

- 노드 번호(i)의 성질
  - 부모 노드 번호 = i //2
  - 왼쪽 자식 노드번호 = 2*i
  - 오른쪽 자식 노드번호 = 2*i+1

- 노드 번호를 배열 인덱스로 사용!
- 높이가 h인 이진트리를 위한 배열 크기는?
  - 2**(h+1)-1



- 보통, 정점(V)의 개수가 주어지면 간선(N)의 개수를, 간선의 개수가 주어지면 정점의 개수를 알 수 있다. (1 차이)

  - 부모 번호를 인덱스로 자식 번호를 저장

    ```
    4					# 간선의 개수 N
    1 2 1 3 3 4 3 5		# 부모 자식 순
    ```

    ![image-20220316194018784](C:\Users\baekh\AppData\Roaming\Typora\typora-user-images\image-20220316194018784.png)

    ```
    for i in range(N):
    	read p, c
    	if c1[p] == 0:
    		c1[p] = c
    	else:
    		c2[p] = c
    ```

    ```python
    '''
    4 (간선)
    1 2 1 3 3 4 3 5
    '''
    def pre_order(v):			# 정점번호 v
        if v:					# 0번 정점이 없으므로... 0번은 자식이 없는 경우를 표시
            print(v)			# visit(v)
            pre_order(ch1[v])	# 왼쪽 자식으로 이동
            pre_order(ch2[v])	# 오른쪽 자식으로 이동
    
    E = int(input())			# 간선 수
    arr = list(map(int, input().split()))
    V = E + 1					# 정점 수 == 1번부터 V번까지 정점일 있을 때 마지막 정점번호
    
    # 부모번호를 인덱스로 자식번호 저장
    ch1 = [0] * (V+1)
    ch2 = [0] * (V+1)
    for i in range(E):
        p, c = arr[i*2], arr[i*2+1]
        if ch1[p]==0: # 아직 자식이 없으면
            ch1[p] = c
        else:
            ch2[p] = c
    print(ch1)	# [ 0, 2, 0, 4, 0, 0]
    print(ch2)	# [ 0, 3, 0, 5, 0, 0]
    
    ```

    - 이진트리 정점번호 규칙
      - 포화이진트리
        - 1번 루트 O
        - 부모 < 자식
      - 그 외 - XXX

  

  

  - 자식 번호를 인덱스로 부모 번호를 저장

    ```python
    par = [0]*(V+1)	#정점번호까지 인덱스가 있어야하므로 +1
    for i in range(0,E,2):
    	p, c = arr[i], arr[i+1]
    	par[c] = p
    	
    '''
    4
    2 1 2 4 4 3 4 5
    '''
    print(*par)		# 0 2 0 4 2 4 (0 1 2 3 4 5)
    # 1. root 찾기에 쓸 거야
    for i in range(1, V+1):
        if par[i] == 0:
            root = i
            break
    print(root)
    in_order(2)		# 1 2 3 4 5
    
    # 조상 찾기
    c = 5			# 정점 c의 조상 찾기
    while par[c] != 0:
        anc.append(par[c])
        c = par[c]
    print(*anc)		# 4 2 (5의 조상은 4와 2)
    ```





### 연결리스트

- 배열을 이용한 이진트리 표현의 단점(편향이진트리는 미사용 배열 원소에 대한 메모리 공간 낭비, 트리 중간에 새로운 노드 삽입이나 삭제의 경우 배열 크기 변경이 어려워 비효율적) 보완을 위해 연결리스트로 트리 표현
- 연결 자료구조를 이용한 이진트리의 표현
  - 이진 트리의 모든 노드는 최대 2개의 자식 노드를 가지므로 일정한 구조의 단순 연결 리스트 노드를 사용하여 구현



#### 연습문제

```python
'''
13 # 정점 개수 (V)
1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13
'''
def pre_order(v): 	# 시작노드입력
    if v:			# 0번 정점에는 자식이 없음
        print(v)	# visit(v)
        pre_order(ch1[v])
        pre_order(ch2[v])
        
V = int(input())
arr = list(map(int, input().split()))
E = V - 1		# 간선 개수 = 정점 - 1

ch1 = [0] * (V+1)
ch2 = [0] * (V+1)

for i in range(0,E,2):
    p, c = arr[i], arr[i+1]
    if ch1[i] == 0:
        ch1 = c
    else:
        ch2[i] = c
        
pre_order(1)
```





## 수식 트리

- 수식을 표현하는 이진 트리

- 수식 이진 트리 (Expression Binary Tree)

- 연산자 : 루트노드 or 가지노드

- 피연산자 : 모두 잎(leaf) 노드

  ![image-20220316200958207](C:\Users\baekh\AppData\Roaming\Typora\typora-user-images\image-20220316200958207.png)

- 수식 트리의 순회

  ![image-20220316201056767](C:\Users\baekh\AppData\Roaming\Typora\typora-user-images\image-20220316201056767.png)

  - 중위 순회 : `A/B*C*D+E`
  - 후위 순회 : `AB/C*D*E+`
  - 전휘 순회 : `+**/ABCDE`



## 이진 탐색 트리

- 탐색 작업을 효율적으로 하기 위한 자료구조
- 모든 원소는 서로 다른 유일한 키를 갖는다.
- **key(왼** 서브트리) < key(루트노드) **< key(오른쪽** 서브트리)
- 왼쪽 서브트리와 오른쪽 서브트리도 이진탐색트리임
- **중위 순회하면 오름차순으로 정렬된 값**을 얻을수 있음



#### 연산

- 탐색연산
  - 루트에서 시작
  - 탐색할 키 값 x를 루트 노드의 키 값과 비교
    - key(x) = 루트 : 원하는 원소 찾음. 탐색연산 성공
    - key(x) < 루트 : 루트의 왼쪽 서브트리 탐색연산 수행
    - key(x) > 루트 : 루트의 오른쪽 서브트리 탐색연산 수행
  - 서브트리에 대해서 순환적으로 탐색 연산을 반복



- 삽입연산

  1. 먼저 탐색연산
     - 삽입할 원소와 같은 원소가 트리에 있으면 삽입이 불가능하므로, 같은 원소가 트리에 있는지부터 확인
     - 탐색 실패 결정 위치 = 삽입 위치
  2. 탐색 실패 위치에 원소를 삽입

  - 5 삽입 예시

    ![image-20220316201902822](C:\Users\baekh\AppData\Roaming\Typora\typora-user-images\image-20220316201902822.png)



- 탐색(searching), 삽입(insertion), 삭제(deletion) 시간은 트리 높이 만큼 시간이 걸린다.
  - O(h), h : BST의 깊이 (height)
- 평균
  - 이진트리가 균형적으로 생성되면 O(log n)
- 최악
  - 한쪽으로 치우친 경사 이진트리 O(n)
  - 순차탐색과 시간복잡도가 같다.



#### [참고] Heap

#### 힙연산 - 삽입

```python
cc
```



#### 힙 연산 - 삭제

- 힙에서는 루트에 있는 것만 삭제 혹은 꺼내진다.
- 최대힙에서는 가장 큰 수가 꺼내질 것이며, 다음값이 루트로 올라갈 것
- ![image-20220316204006400](C:\Users\baekh\AppData\Roaming\Typora\typora-user-images\image-20220316204006400.png)
  - 루트 삭제
  - 마지막 노드를 루트로 옮김
  - 루트가 작으면 양쪽 자식들 중 큰 수와 교체



