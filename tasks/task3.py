# tasks/task3.py

def solve():
# Ниже пишите решение задачи
    n= int(input())
    count_100 = n//100
    n= n % 100
    count_20 = n//20
    n= n %20
    count_10 = n//10
    n = n % 10
    count_5 = n//5
    n = n % 5
    count_1 = n
    result = count_100 + count_20 + count_10 + count_5 + count_1
    print(result)


# Код ниже не трогать! он нужен для тестов
if __name__ == "__main__":
    solve()