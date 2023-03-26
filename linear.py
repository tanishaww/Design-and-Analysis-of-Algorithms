def linearsearch(a,b,c):
    for i in range(0,c):
        if a[i] == b:
            return i
        return -1
a=[1,3,6,2,8,32,14]
b = int(input("Enter the number you want to search: "))
c = len(a)
ans = linearsearch(a,b,c)
if (ans == -1):
    print("Element not found")
else:
    print("Element found at index:",ans)
    