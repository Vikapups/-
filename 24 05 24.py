def summ(start, end):
    if start > end:
        start, end = end, start
    a = 0
    for i in range(start, end + 1):
        a += i
    print (a)
