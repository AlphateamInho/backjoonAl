print("테스트 횟수를 입력 : \n")
C = int(input())

arr = []

for i in range(C):
    print("학생수를 입력 : \n")
    N = int(input())
    count = 0
    for i in range(N):
        arr.append(input())
        print(arr[i])