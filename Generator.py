def interval(num):
    for i in range(num,1,-1):
        yield i

show = interval(10)
for x in show: 
    print(x)