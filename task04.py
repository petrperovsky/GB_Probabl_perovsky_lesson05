'''Продавец утверждает, что средний вес пачки печенья составляет 200 г.
Из партии извлечена выборка из 10 пачек. Вес каждой пачки составляет:
202, 203, 199, 197, 195, 201, 200, 204, 194, 190.
Известно, что их веса распределены нормально.
Верно ли утверждение продавца, если учитывать, что доверительная вероятность равна 99%?'''

'''H0: продавец не врет'''

import numpy as np

x = [202, 203, 199, 197, 195, 201, 200, 204, 194, 190]
X = sum(x) / len(x)
print(X)  # средний вес пачки из выборки 198.5
m = 200 - X
s = np.std(x, ddof=1)
print(s)  # Нeсмещенная оценка std = 4.45
t = m / (s / 10 ** 0.5)
print(t) # 1.06

'''Критерий стьдента для доверит вероятности 99 % (а = 0.5% так как исходно не знаем больше или меньше)
и ст свободы 9 = 3.25
Т.о. с вероятностью ошибиться в 1% могу доверять словам продавца, что пачка печенья будет весить 200 гр'''