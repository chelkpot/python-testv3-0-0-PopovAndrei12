# tasks/task1.py

def solve():
# Ниже пишите решение задачи
    num = int(input())
    sum = (num//100)+((num//10)%10)+(num%10)
    print(sum)

    
# Код ниже не трогать! он нужен для тестов
if __name__ == "__main__":
    solve()