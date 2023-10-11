a = 0
b = 1
sum = 0

n = int(input("Enter limit for fibonacci series: "))

if n < 0: 
    print("Enter number above 0")
else:
    for i in range(n):
        print(sum, end=" ")
        a = b 
        b = sum
        sum = a + b


