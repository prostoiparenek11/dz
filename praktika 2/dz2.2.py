def main():
    stroka = input()
    a = stroka.split()
    a.reverse()
    st = ' '.join(a)
    st = st.capitalize()
    print (st)
if __name__ == "__main__":
    main()