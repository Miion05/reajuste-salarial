from math import ceil

reaj = 0
opt = 0

salary = float(input('Salário: '))

def final_value(a, b):
    return a + b

def reajuste(a, b):
    return a * b

high_salary = ceil(salary)

if high_salary <= 0:
    raise Exception('ERRO! APENAS NÚMEROS ACIMA DE 0 SÃO ACEITOS!')

if high_salary in range(0, 401, 1):
    reaj = reajuste(salary, 0.15)
    opt = 1
elif high_salary in range(401, 801, 1):
    reaj = reajuste(salary, 0.12)
    opt = 2
elif high_salary in range(801, 1201, 1):
    reaj = reajuste(salary, 0.1)
    opt = 3
elif high_salary in range(1201, 2001, 1):
    reaj = reajuste(salary, 0.07)
    opt = 4
elif high_salary > 2000:
    reaj = reajuste(salary, 0.04)
    opt = 5

final = final_value(reaj, salary)

print(f'Novo salário: {final :.2f}')
print(f'Reajuste ganho: {reaj :.2f}')
if opt == 1:
    print(f'Em percentual: 15%')
elif opt == 2:
    print(f'Em perceentual: 12%')
elif opt == 3:
    print(f'Em perceentual: 10%')
elif opt == 4:
    print(f'Em perceentual: 7%')
else:
    print(f'Em perceentual: 4%')



