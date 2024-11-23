import pandas as pd

data = {
    'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'gender': ['female', 'male', 'male', 'male', 'female'],
    'department': ['HR', 'Engineering', 'Marketing', 'Engineering', 'HR']
}
df = pd.DataFrame(data)

#Преобразуем столбцы в категориальные данные.
# Мы можем сделать категории для столбцов "gender" и "department"
df['gender'] = df['gender'].astype('category')
df['department'] = df['department'].astype('category')

#просмотр уникальных категорий, которые есть в датафрейме
print(df['gender'].cat.categories)
print(df['department'].cat.categories)

#посмотреть числовые коды категорий
print(df['gender'].cat.codes)
print(df['department'].cat.codes)

#добавить новую категорию, remove_categories - удаление категории
df['department'] = df['department'].cat.add_categories(['Finance'])
print(df['department'].cat.categories)
df['department'] = df['department'].cat.remove_categories(['HR'])
print(df['department'].cat.categories)
print(df)