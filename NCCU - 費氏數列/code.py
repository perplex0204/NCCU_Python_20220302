'''
一自訂義函式計算費氏數列，輸入為此數列之最大上限，輸出為list
'''
import time

# 上限定義為數值


def fibinacci_number_limit_number(limit):
    answer = [1, 1]
    index = 2
    while answer[len(answer)-1] < limit:
        answer.append(answer[index-1]+answer[index-2])
        index = index + 1
    answer.pop(-1)
    return answer

# 上限定義為算到第幾項


def fibinacci_number_limit_count(limit):
    answer = []
    for i in range(limit):
        if i <= 1:
            answer.append(1)
        if i > 1:
            answer.append(answer[i-1]+answer[i-2])
    return answer


while True:
    try:
        input_number = int(input('請輸入整數數字：'))
        print('上限為數值的情況：', fibinacci_number_limit_number(input_number))
        print('上限為數項的情況：', fibinacci_number_limit_count(input_number))
    except ValueError:
        print('輸入錯誤，請輸入整數數字')
