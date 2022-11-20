# f(x) = 5x^2 + 10x - 30

# Определить корни

# Найти интервалы, на которых функция возрастает

# Найти интервалы, на которых функция убывает

# Построить график

# Вычислить вершину

# Определить промежутки, на котором f > 0

# Определить промежутки, на котором f < 0

import sympy

# def diskr(a,b,c):
#     return (b**2 - 4*a*c)

# def solve(a,b,c):
#     d = diskr(a,b,c)
#     if d < 0:
#         return ['Корней нет']
#     elif d == 0:
#         return [(-b + d**(0.5))/2]
#     else:
#         return [(-b + d**(0.5))/(2*a), (-b - d**(0.5))/(2*a)]

# def top_h(a,b,c):
#     return (-b/(2*a))

# def up_n_dwn():
#     global a,b,c
#     return f'Убывание на промежутке ((-беск; {top_h(a,b,c)}), возрастание на ({top_h(a,b,c)}; +беск))'

# def pos_neg(mass):
#     return f'Функция < 0 на промежутке ({mass[1]}; {mass[0]}), функция > 0 на промежутке (-беск; {mass[1]}; ) ({mass[0]}; +беск)'

a = int(input())
b = int(input())
c = int(input())

# print(solve(a,b,c))
# print(top_h(a,b,c))
# print(up_n_dwn())
# print(pos_neg(solve(a,b,c)))

x = sympy.Symbol('x')
# sympy.plotting.plot(5*x**2 + 10*x - 30)
# a = sympy.solve(5*x**2 + 10*x - 30, x)
# i = (a[0] + a[1])/2
# if 5*i**2 + 10 * i - 30 > 0:
#     print(f'функция > 0 на промежутке ({a[1]}; {a[0]}')
# else:
#     print(f'функция > 0 на промежутке (-беск; {a[1]}) ({a[0]}; +беск')

# print(sympy.solve(5*x**2 + 10*x - 30 > 0, x))
# print(sympy.solve(5*x**2 + 10*x - 30 < 0, x))

f = 5*x**2 + 10*x - 30
diff = sympy.diff(f,x)
print(diff)
print(sympy.solve(diff > 0, x))
print(sympy.solve(diff < 0, x))
print(sympy.solve(diff, x))