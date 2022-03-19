# 첫째 줄에는 현재 시각이 나온다.
# 현재 시각은 시 A (0 ≤ A ≤ 23) 와 분 B (0 ≤ B ≤ 59)가 정수로 빈칸을 사이에 두고 순서대로 주어진다.
#  두 번째 줄에는 요리하는 데 필요한 시간 C (0 ≤ C ≤ 1,000)가 분 단위로 주어진다. 

# 출력
# 첫째 줄에 종료되는 시각의 시와 분을 공백을 사이에 두고 출력한다.
# (단, 시는 0부터 23까지의 정수, 분은 0부터 59까지의 정수이다.
# 디지털 시계는 23시 59분에서 1분이 지나면 0시 0분이 된다.)

H ,M = map(int, input().split())
# 시간과 분을 입력받는다.
T = int(input())
# 몇 분이 걸릴 지 입력받는다.

MT = M + T
# 현재 분에서 오븐이 완료될때 까지 몇분이 걸리는지를 합친다.
while(MT >= 60):
    MT -= 60
    H += 1
# 만약 합친시간이 60분 이상이라면, 60분미만이 될 때 까지 합친시간은 60만큼 빼고, 시간에 1시간씩 더한다.
if (H>23):
    H=H%24
# 시간이 24시(00)시를 넘기면, 24로 나눈 나머지 값을 완료 예정시간에 넣는다.
print(H)
print(MT)