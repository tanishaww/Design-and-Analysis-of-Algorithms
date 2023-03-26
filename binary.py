def binarysearch():
    a=(1,3,4,5,7,9)
    low = 0
    high = len(a) - 1
    key=int(input("Enter the key "))
    while(low<=high):
        mid=(low+high)//2
        if key>mid:
            low=mid+1
        elif key<mid:
            high=mid-1
        else:
            print("number found at ",mid)
            break
binarysearch()