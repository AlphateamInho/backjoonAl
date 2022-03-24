# 알파벳 대소문자로 된 단어가 주어지면, 이 단어에서 가장 많이 사용된 알파벳이 무엇인지 알아내는 프로그램을 작성하시오. 
# 단, 대문자와 소문자를 구분하지 않는다.
# 입력
# 첫째 줄에 알파벳 대소문자로 이루어진 단어가 주어진다.
#  주어지는 단어의 길이는 1,000,000을 넘지 않는다.

# 첫째 줄에 이 단어에서 가장 많이 사용된 알파벳을 대문자로 출력한다.
#  단, 가장 많이 사용된 알파벳이 여러 개 존재하는 경우에는 ?를 출력한다

inputData = input().upper()
# 문자열.upper() 문자열 모두 대문자로 변환
searchKeys = list(set(inputData))
# 검색 키들을 따로 리스트로 만들어놓음, 하지만 검색 키값이 중복되면 안되기에 중복을 제거하는 set() 활용

countArr = []
for key in searchKeys:
    countArr.append(inputData.count(key))

if countArr.count(max(countArr)) > 1:
    # 리스트 내에 최대 값을 반환하는 max()
    # 리스트내에 해당 값이 몇개인지 검색하는 리스트.count()
    print("?")
else:
    print(searchKeys[countArr.index(max(countArr))])
    # 리스트내에 해당 값이 몇개인지 검색하는 리스트.count()