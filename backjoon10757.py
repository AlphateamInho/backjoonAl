# 문제
# 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.
# 입력
# 첫째 줄에 A와 B가 주어진다. (0 < A,B < 1010000)
# 출력
# 첫째 줄에 A+B를 출력한다.


import sys
A,B = map(int, sys.stdin.readline().split())
print(A+B)

# 정답률 50%미만 문제라 뭐가 더 있을 줄 알았는데 이게끝이였다.
# 아마 큰 수를 다루는문제라서 sys.stdin.readline() 을 쓰는게 핵심이였던것 같다.