def square_digits(num):
    squared_num = 0
    total = ''
    num = str(num)
    for item in num:
        squared_num = str(int(item)**2)
        total = ''.join([total,squared_num])
    return int(total)

print(square_digits(9119))