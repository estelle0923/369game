number = input('Please input an end number:')
print('369 369, 369 369 !!')

def claptime(i):
    number_count = 0
    a = str(i)
    for x in a:
        if x in '369':
            number_count += 1
    if number_count == 0:
        print(i)
    else:
        print('짝!' * number_count)
        

for j in range(1, int(number)+1):
    claptime(j)
