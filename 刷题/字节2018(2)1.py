if __name__ == '__main__':
    n = int(input())
    st = {}
    arr = list(map(int,input().split()))
    for i in range(n):
        if arr[i] in st:
            st[arr[i]].append(i+1)
        else:
            st[arr[i]] = [i+1]
    q = int(input())
    b = []
    for i in range(q):
        brr = list(map(int,input().split()))
        l,r,k = brr[0],brr[1],brr[2]
        if k in st:
            c = st[k]
            count = 0
            for ci in c:
                if l<=ci<=r:
                    count += 1
            b.append(count)
        else:
            b.append(0)
    for ij in b:
        print(ij)


