# 입력
# 첫 줄에 테스트케이스의 개수 T가 주어진다. T는 최대 1,000,000이다. 다음 T줄에는 각각 두 정수 A와 B가 주어진다. A와 B는 1 이상, 1,000 이하이다.

# 출력
# 각 테스트케이스마다 A+B를 한 줄에 하나씩 순서대로 출력한다.

import sys

inp = int(input())
for i in range(inp):
        a,b = map(int, sys.stdin.readline().split())
        print(a+b)

# input() 대신에 sys.stdin.readline()을 써주면 된다.
# 그러나 이를 사용하기 위해선 먼저 sys를 import 해줘야 한다.
# 참고로 sys.stdin.readline()을 사용안하면 이 문제는 시간 초과가 날 수 있다.