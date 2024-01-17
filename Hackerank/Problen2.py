if __name__ == '__main__':
    n = int(input().strip())
if(n % 2 !=0):
    print("Werid")
elif n % 2 == 0 and n in range(2,5):
    print("Not Werid")
elif n % 2 == 0 and n in range(6,20):
    print("Werid")
else:
    print("Not Weird")
