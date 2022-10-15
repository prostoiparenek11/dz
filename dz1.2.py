def main():
    a = int(input())
    astr =''
    if a >= -2**7 and a <= (2**7 - 1):
        astr = str(a)[::-1]
        if astr[-1] == '-':
            astr = astr[:-1:]
            astr = '-' + astr
        print (astr)
    else:
        print ('no solution')
if __name__ == "__main__":
    main()