import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#в скобках указывается стартовая точка,
# количество дат (10), а также интервал (freq) в один день (D)
dates = pd.date_range(start='2022-07-26', periods=10, freq='D')
#список из случайных значений - с помощью библиотеки NumPy.
# В круглых скобках указываем сколько значений
values = np.random.rand(10)
df = pd.DataFrame({'Date': dates, 'Value': values})

#Установим колонку Date в качестве индекса всего датафрейма
df.set_index('Date', inplace=True)
print(df)

#Ресэмплирование данных (изменения частоты временных рядов)
#использовали функцию resample(ME), чтобы разделить данные на месячные интервалы.
# К этой функции можно добавить метод mean(), который будет указывать программе
# вычислить среднее значение для каждого месяца
month = df.resample('ME').mean()
print(month)

#Обработка выбросов (необычные или экстремальные значения в наборе данных,
# которые могли попасть в массив данных случайно или в результате ошибки.
# Эти значения могут быть как ошибочными, так и реальными. Данные роста, например)
df1 = pd.DataFrame({'Value' : [1, 2, 3, 3, 3, 4, 4, 4, 5, 6, 7, 8, 9, 10, 55]})
# df1['Value'].hist() #гистограмма
# plt.show() #показывает график, который мы создали
df1.boxplot(column='Value')
plt.show()
print(df1.describe())

#Квартиль — это значение, которое разделяет упорядоченный набор данных на четыре равные части
#Первый квартиль (Q1) представляет собой значение, ниже которого находится 25% всех значений,
# а третий квартиль (Q3) — это значение, ниже которого находится 75% всех значений
#Межквартальный размах (IQR) вычисляется как разница между третьим и первым квартилями.
# Межквартальный размах показывает, как широко разбросаны средних 50 процентов значений
Q1 = df1['Value'].quantile(0.25)
Q3 = df1['Value'].quantile(0.75)
IQR = Q3 - Q1

#определим нижнюю и верхнюю границы для определения выбросов
downside = Q1 - 1.5 * IQR
upside = Q3 + 1.5 * IQR

#теперь необходимо удалить выбросы, которые не входят в очерченный диапазон.
# Создадим новый датафрейм
df1_new = df1[ (df1['Value']>=downside) & (df1['Value']<=upside) ]
df1_new.boxplot(column='Value')
plt.show()


