#숫자가 들어있는 리스트의 합계
def sum_list(scores):
    result = sum(scores)
    return result

#최댓값
def max_list(scores):
    result = max(scores)
    return result

#최솟값
def min_list(scores):
    result = min(scores)
    return result

#평균
def avg_list(scores):
    result = sum(scores) / len(scores)
    return result

#짝수인 것만 세기
def count_even(scores):
    count=0
    result=[]
    for i in scores:
        if i % 2 == 0:
            count+=1
            result.append(i)
    return(result,count)

#N개의 0을 가진 리스트 만들기
def make_list(n):
    result= [0]*n
    return result



#Test Case
scores = [10, 3, 20, 50]
print(sum_list(scores))

print(max_list(scores))

print(min_list(scores))

print(avg_list(scores))

print(count_even(scores))

print(make_list(6))