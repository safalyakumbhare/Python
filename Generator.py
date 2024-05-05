def count(num):
    for i in range(1,num+1):
        yield i

show = count(10)
for n in show:
    print(n)