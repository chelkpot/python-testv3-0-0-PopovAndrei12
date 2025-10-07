# tasks/task5.py

def solve():
# Ниже пишите решение задачи
    n=int(input())
    n=n%86400
    hours = n//3600
    minutes = (n % 3600) // 60
    seconds=n%60
    print(hours,':' ,minutes//10,minutes%10,':' ,seconds//10, seconds%10,sep="")
    

   
# Код ниже не трогать! он нужен для тестов
if __name__ == "__main__":
    solve()