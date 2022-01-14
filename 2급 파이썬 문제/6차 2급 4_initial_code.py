#다음과 같이 import를 사용할 수 있습니다.
#import math

def solution(cards):
    #여기에 코드를 작성해주세요.
    counter=[0,0,0]
    total = 0
    for card in cards:
        color = card[0]
        number = card[1]
        if color == 'blue':
            counter[0] += 1
        elif color == 'red':
            counter[1] += 1
        elif color == 'black':
            counter[2] += 1
        total += int(number)
    weight = max(counter)
    answer = total * weight
    return answer

#아래는 테스트케이스 출력을 해보기 위한 코드입니다.
cards1 = [["blue", "2"], ["red", "5"], ["black", "3"]]
ret1 = solution(cards1)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret1, "입니다.")

cards2 = [["blue", "2"], ["blue", "5"], ["black", "3"]]
ret2 = solution(cards2)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret2, "입니다.")