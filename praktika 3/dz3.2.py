def main():
    from itertools import permutations
    n = int(input())
    m = [int(input()) for i in range(n)]
    for x in permutations(m,n):
        m.append(list(x))
    m = m[n::]
    mnew = []
    for i in m:
        if i not in mnew:
            mnew.append(i)
    print(mnew)
if __name__ == "__main__":
    main()