def main():
    a = int(input())
    c = a
    b = ''
    while a > 0:
        b += str(a%10)
        a = a // 10
    if c == int(b):
        print ('True')
    else:
        print ('False')
if __name__ == "__main__":
    main()