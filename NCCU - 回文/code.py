'''
檢查回文
'''

def palindrome_check(str):
    buffer1 = []
    buffer2 = []
    for i in range(len(str)):
        buffer1.append(str[i])
        buffer2.append(str[-i-1])
    if buffer1 == buffer2:
        return True
    else:
        return False


while True:
    print(palindrome_check(input('請輸入欲檢查的字串：')))
