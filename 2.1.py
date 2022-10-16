def main():
    s = input()
    ns = []
    newst = ''
    maxs =''
    for i in s:
        while i in ns:
            del ns[0]
        ns.append(i)
        newst = ''.join(ns)
        maxs = max(maxs, newst, key = len)

    print (maxs)
if __name__ == "__main__":
    main()

