import pandas as pd
import matplotlib.pyplot as plt

df = pd.DataFrame({
    'name' : ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Mat', 'Roj', 'Fil', 'Alex','Pit'],
    'math' : [2,4,5,4,3,5,5,3,5,5],
    'history' : [3,3,4,4,5,5,5,3,4,5],
    'biology' : [4,4,5,4,5,4,5,5,5,3],
    'physics' : [5,5,2,2,3,4,4,5,3,5],
    'literature' : [5,5,5,5,5,5,5,5,4,4]
})
print(df.head())
print(f'Средняя оценка по математике - {df['math'].mean()}')
print(f'Средняя оценка по истории - {df['history'].mean()}')
print(f'Средняя оценка по биологии - {df['biology'].mean()}')
print(f'Средняя оценка по физике - {df['physics'].mean()}')
print(f'Средняя оценка по литературе - {df['literature'].mean()}')
print(f'Медиана по математике - {df['math'].median()}')
print(f'Медиана оценка по истории - {df['history'].median()}')
print(f'Медиана оценка по биологии - {df['biology'].median()}')
print(f'Медиана оценка по физике - {df['physics'].median()}')
print(f'Медиана оценка по литературе - {df['literature'].median()}')
print(f'Стандартное отклонение по математике - {df['math'].std()}')
print(f'Стандартное отклонение оценка по истории - {df['history'].std()}')
print(f'Стандартное отклонение оценка по биологии - {df['biology'].std()}')
print(f'Стандартное отклонение оценка по физике - {df['physics'].std()}')
print(f'Стандартное отклонение оценка по литературе - {df['literature'].std()}')
Q1 = df['math'].quantile(0.25)
Q3 = df['math'].quantile(0.75)
IQR = Q3 - Q1
print(f'Квартиль 1 - {Q1}; Квартиль 3 - {Q3}; IQR - {IQR}')
df.set_index('name', inplace=True)
subjects = df.columns

#создаем фигуру и сетку подграфиков - объект фигуры fig и массив осей axes
# для настройки и построения каждого подграфика
# будет одна строка подграфиков, количество столбцов подграфиков равно количеству предметов
#размер фигуры в дюймах 15 на 5, а ось Y будет общая для всех подграфиков, чтобы
#шкала оценок была одинаковой для них всех
fig, axes = plt.subplots(nrows=1, ncols=len(subjects), figsize=(15,5), sharey=True)

#строим для каждого предмета столбчатую диаграмму.
# zip позволяет проходить одновременно по двум массивам
# df[subject] выбирает столбец с оценками для каждого предмета
#kind='bar' указывает, что строим столбчатую диаграмму,
# график рисуем на текущей оси X. ax.set_xticklabels(df.index, rotation=45) - устанавливает
# метки для оси из датафрейма и поворачивает их на 45 градусов

for ax, subject in zip(axes, subjects):
    df[subject].plot(kind='bar', ax=ax, title=subject)
    ax.set_xlabel('Ученик')
    ax.set_ylabel('Оценка')
    ax.set_xticklabels(df.index, rotation=45)

#автоматически регулирует параметры размещения графиков, чтобы они не перекрывались
plt.tight_layout()
plt.show()


