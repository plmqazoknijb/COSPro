# # << 모의고사 1회 >>
#
# # 1번 문제 - 거스름돈을 계산하는 함수 작성하기
# def solution(price, money):
#     answer = 0
#     sum_p = sum(price)
#     if sum_p <= money:
#         answer = money - sum_p
#     else:
#         answer = -1
#     return answer
#
# # Test Case
# ret = solution([2100,3200,2100,800],10000)
# print(ret)
# ret = solution([2100,3200,2100,800],5000)
# print(ret)
#
# # 2번 문제 - 점수의 총합에서 최고 점수와 최저 점수를 뺼셈하는 함수의 빈칸 채우기
# def func_a(s):
#     s.sort()
#     return s[len(s)-1],s[0]
# def func_b(s):
#     ret = 0
#     for i in s:
#         ret += i
#     return ret
# def solution(scores):
#     sum = func_b(scores)
#     max,min = func_a(scores)
#     return sum - max - min
#
# # Test Case
# ret = solution([10,30,40,20])
# print(ret)
#
#
# # 3번 문제 - 학급 대상자 수를 구하는 함수 수정하기
# def solution(scores):
#     count = 0
#     for s in range(len(scores)):
#         if scores[s] <= 200:
#             count += 1
#     return count
#
# # Test Case
# ret = solution([100,200,30,20,210])
# print(ret)
#
# # 4번 문제 - 관세를 매긴 금액을 구하는 함수 작성하기
# def solution(price,grade):
#     answer = 0
#     if grade == 'S':
#         answer = int(price*1.05)
#     elif grade == "G":
#         answer = int(price*1.10)
#     elif grade == "V":
#         answer = int(price*1.15)
#     return answer
#
# # Test Case
# ret = solution(1000,'S')
# print(ret)
# ret = solution(1000,'G')
# print(ret)
# ret = solution(1000,'V')
# print(ret)
#
# # 5번 문제 - 정수에서 3,6,9가 포함되어 있는지 확인하는 함수의 빈칸 채우기
# def solution(number):
#     count = 0
#     for i in range(number+1):
#         current = i
#         while current != 0:
#             unit= current%10
#             if unit == 3 or unit == 6 or unit == 9:
#                 count += 1
#             current//=10
#     return count
#
# # Test Case
# ret = solution(15)
# print(ret)
#
# # 6번 문제 - 교차점의 개수를 구하는 함수 빈칸 채우기
# def solution(left_rings):
#     answer = 0
#     for i in range(len(left_rings)):
#         if left_rings[i] <= i:
#             for k in range(i):
#                 if left_rings[k] > left_rings[i]:
#                     answer += 1
#     return answer
#
# # Test Case
# ret = solution([0,3,1,4,2])
# print(ret)

# 7번 문제 - 파일 업로드를 위한 파일 정보를 확인하는 함수의 빈칸 채우기
def solution(file_info):
    sucess = 0
    fail = 0
    for f in file_info:
        splited = f.split(",")
        if splited[0] == "jpeg" and int(splited[2]) < 1000:
            sucess += 1
        else:
            fail += 1
    return sucess, fail

#Test Case
ret = solution(["jpeg,all.jpg,500","mpeg,all.mp3,500"])
print(ret)

# 8번 문제 - 거꾸로 읽어도 같은 회문을 확인하는 함수 수정하기
def solution(sentence):
    filtered = []
    for s in sentence:
        if s !=' ' and s !='.':
            filtered.append(s)
    before = ''.join(filtered)
    filtered.reverse()
    after = ''.join(filtered)
    return before == after

# Test Case
ret = solution('never odd or even')
print(ret)
ret = solution('ababbda')
print(ret)

# 9번 문제 - 중복되는 문자를 제거하는 함수 수정하기
def solution(characters):
    result = [characters[0]]
    for i in range(1,len(characters)):
        if characters[i-1] != characters[i]:
            result.append(characters[i])
    return ''.join(result)

#  Test Case
ret = solution('reeplay')
print(ret)

# 10번 문제 - 특정 값보다 작은 값을 찾는 함수 수정하기기
def solution(data):
    total = 0
    for i in data:
        total += i
    cnt = 0
    average = total // len(data)
    for i in data:
        if i < average:
            cnt += 1
    return cnt

# Test Case
ret = solution([1,2,3,4,5,6,7,8,9,10])
print(ret)