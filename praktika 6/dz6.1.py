def main():
    m1 = [['name1 surname1', 1234], ['name2 surname2'], ['name3 surname3', 12345], ['name4 surname4', 123456]]
    def santa_users(m1):
        for i in m1:
            if len(i) == 1:
                i.append(None)
        r = dict(m1)
        return r
    print (santa_users(m1))

if __name__ == "__main__":
    main()