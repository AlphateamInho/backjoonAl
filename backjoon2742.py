# 입력
# 첫째 줄에 100,000보다 작거나 같은 자연수 N이 주어진다.

# 출력
# 첫째 줄부터 N번째 줄 까지 차례대로 출력한다.

N = int(input())

for i in range(N):
    print(N-i)
    i -= 1