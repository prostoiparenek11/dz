#Задается количество элементов в списке ( >4).
# Задается целочисленный список длины N.
# Задается цель.
# Необходимо найти сумму 4 чисел, которые равны цели или находятся близко к ней и вывести их.
#Input:
#N = 5
#[1, 2, 4, -5,-2]
#C = 1
#Output:
#[1,2,4,-5]
#2
#Input:
#N = 6
#[4, -5, -7, 12,-2,5]
#C = -5
#Output:
#[4,-5,-7,5]
#-3
#Input:
#N = 7
#[1,1,1,1,1,1,1]
#C = 5
#Output:
#[1,1,1,1]
#4
#Input:
#N = 5
#[1,3,0,-4,8]
#C = 3
#Output:
#[1,0,-4,8]
#5
def main():
    import itertools
    elements = [int(input()) for i in range(int(input()))]
    C = int(input())
    p = list(itertools.combinations(elements, 4))
    min_range = abs(sum(p[0]) - C)
    res = p[0]
    for i in p:
        if abs(sum(i) - C) < min_range:
            res, min_range = i, abs(sum(i) - C)
    print(list(res), sum(res), sep = '\n')
if __name__ == '__main__':
    main()
















