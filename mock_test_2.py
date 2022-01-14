# << 모의고사 2회 >>

# 1번 문제 - 축구장 임대료를 구하는 함수 빈칸 채우기
def solution(n,price):
    games = n*(n-1)//2
    per_day = n//2
    answer = (games // per_day) * price
    return answer

# Test Case
ret = solution(8,1000)
print(ret)

# 2번 문제 - 축구화 주문 수량 구하는 함수 완성하기
def solution(shoes_size):
    answer = [0,0,0,0,0,0]
    for i in shoes_size:
        if i == "7":
            answer[0] += 1
        elif i =="7.5":
            answer [1] += 1
        elif i == "8":
            answer[2] += 1
        elif i == "8.5":
            answer[3] += 1
        elif i == "9":
            answer[4] += 1
        elif i == "9.5":
            answer[5] += 1
    return answer

# Test Case
ret = solution(["7","7.5","8","8.5","9","8.5"])
print(ret)

# 3번 문제 - 방문객 수의 차이를 구하는 함수의 빈칸 채우기
def func_a(arr,num):
    ret =[]
    for i in arr:
        if i != num:
            ret.append(i)
    return ret

def func_b(a,b):
    if a > b:
        return a-b
    else:
        return b-a

def func_c(arr):
    ret = -1
    for i in arr:
        if ret < i:
            ret = i
    return ret

def solution(visitor):
    max_first = func_c(visitor)
    visitor_removed = func_a(visitor,max_first)
    max_second = func_c(visitor_removed)
    answer = func_b(max_first,max_second)
    return answer

# Test Case
ret = solution([10,4,40,30,50,20])
print(ret)

# 4번 문제 - 학점별 인원수를 구하는 함수의 빈칸 채우기
def solution(scores):
    grade_counter = [0 for i in range(len(scores)-1)]
    for i in scores:
        if i >= 85:
            grade_counter[0] += 1
        elif i >= 70:
            grade_counter[1] +=1
        elif i >= 55:
            grade_counter[2] += 1
        elif i >= 40:
            grade_counter[3] += 1
        else:
            grade_counter[4] += 1
    return grade_counter

# Test Case
ret = solution([100,30,60,20,90,40])
print(ret)

# 5번 문제 - 빈도(출현)를 구하는 함수의 빈칸 채우기
def func_a(arr):
    counter = [0 for _ in range(1001)]
    for i in arr:
        counter[i] += 1
    return counter

def func_b(arr):
    ret = 0
    for i in arr:
        if ret < i:
            ret = i
    return ret

def func_c(arr):
    ret = func_b(arr)
    for i in arr:
        if ret > i and i != 0:
            ret = i
    return ret

def solution(arr):
    counter = func_a(arr)
    max_cnt = func_b(counter)
    min_cnt = func_c(counter)
    return max_cnt // min_cnt

# Test Case
ret = solution([500,500,1,1000,500,500,1000,1,1])
print(ret)

# 문제 6번 - 몸무게가 큰 사람의 수를 구하는 함수 수정하기
def solution(weight,k):
    answer = 0
    for w in weight:
        if w > k:
            answer += 1
    return answer

# Test Case
ret = solution([65,70,75,80,84],75)
print(ret)

# 문제 7번 - 문자열 내 특정 문자를 바꾸는 함수 수정하기
def solution(s):
    answer = []
    for c in s:
        if '0' <= c <= '9':
            n = ord('i')-ord(c)
            c = chr(n)
        answer.append(c)
    return "".join(answer)

# Test Case
ret = solution('ab1c3d')
print(ret)

# 문제 8번 - 이름에 특정 문자가 포함된 개수를 구하는 함수 수정하기
def solution(name_list):
    answer = 0
    for name in name_list:
        for char in name:
            if char.find('A') != -1 or char.find('K') != -1:
                answer += 1
                break
    return answer

# Test Case
ret = solution(['Kickboard Association','Common Engineering','Adios','CafeMasita. Ltd'])
print(ret)

# 문제 9번 - 제품 포장을 위한 상자의 개수를 구하는 함수 수정하기
def solution(orders):
    answer = 0
    size = 0
    for o in orders:
        for i in range(6):
            if o[i] != 0:
                size += ((i+1)**2)*o[i]
    answer = size // 36
    if size % 36 != 0:
        answer += 1
    return answer

# Test Case
ret = solution([[0,0,4,0,0,1]])
print(ret)

# 문제 10번 - ISBN 규칙을 확인하는 함수 작성하기
def sum_isbn(isbn):
    sum = 0
    for i in range(len(isbn)):
        c = int(isbn[i])
        if i % 2:
            w=3
        else:
            w = 1
        sum += w * c
    return sum

def solution(isbn):
    answer = ''
    sum = sum_isbn(isbn[:-1])
    r = 10 - (sum % 10)
    if r == 10:
        answer = '0'
    else:
        answer = str(r)
    return answer

# Test Case
ret = solution("9788960777330")
print(ret)