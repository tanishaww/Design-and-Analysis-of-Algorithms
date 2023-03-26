def bubblesort(a):
    n = len(a)
    for i in range(n-1):
        for j in range(0,n-i-1):
            if a[j] > a[j + 1]:
                t = a[j]
                a[j] = a[j+1]
                a[j+1] = t
    print(a)
a=[45,34,23,65,3,56]
bubblesort(a)

            