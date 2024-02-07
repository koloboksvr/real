# Дополнить справочник возможностью копирования данных из одного файла в другой. Пользователь вводит номер строки, которую необходимо перенести из одного файла в другой.

# Формат сдачи: ссылка на свой репозиторий.


# Добавлена предзагрузка справочника при наличии файла.
# Добавлены функции редактирования, удаления, экспорта.
# # Переработаны некоторые функции и пункты меню
# riter = csv.DictWriter(csv_file, fieldnames=fieldnames)
# writer.writeheader()
# writer.writerows(list_contacts)



# 'cp1251'
# 'cp-1251'
# f = open('myfile.txt', 'w', encoding='utf-8')
# f.write('какая-то строка\n')
# f.close()
#
# f = open('myfile.txt', 'a', encoding='utf-8')
# f.write('новая строка\n')
# f.close()

# with open('myfile.txt', 'w', encoding='utf-8') as fd:
#     fd.write('какая-то строка\n')

# with open('myfile.txt', 'r', encoding='utf-8') as fd:
#     from_file = fd.readlines()
#     print(from_file)
#
# with open('myfile2.txt', 'w', encoding='utf-8') as fd:
#     lines = ['строка\n', 'ещё строка\n', 'и ещё одна строчка\n']
#     fd.writelines(lines)
# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в текстовом файле
# 3. Пользователь может ввести одну из характеристик для поиска определенной записи
#    (Например имя или фамилию человека)
# main.py
# FILE_NAME = 'phone_book.txt'

# with open('phone_book.txt', 'r', encoding='utf-8') as f:
#         lines = f.readlines()
#         for line in lines:
#             print(line)
# FileNotFoundError
# try:
#         # print('открытие файла')
#     with open('phone_book.txt', 'r', encoding='utf-8') as f:
#         lines = f.readlines()
#         for line in lines:
#             print(line)
# except FileNotFoundError as err:
#         print('файла нет. Сначала введите данные\n')
# else:
#         print('else')
# finally:
#     print('finally')
#     last_name,first_name,patronymic,phone_number
# # Иванов, Иван,Иванович,"777
# # "
# # Иванов,Александр,Юрьевич,"888
# # "
# #  Иван, Иванов, Иванович, 777
# # eeee, Иванов, Иванович, 777
# # Александр, Иванов, Юрьевич, 888
#     import csv,os

# 'cp1251'
# 'cp-1251'
# f = open('myfile.txt', 'w', encoding='utf-8')
# f.write('какая-то строка\n')
# f.close()
#
# f = open('myfile.txt', 'a', encoding='utf-8')
# f.write('новая строка\n')
# f.close()

# with open('myfile.txt', 'w', encoding='utf-8') as fd:
#     fd.write('какая-то строка\n')

# with open('myfile.txt', 'r', encoding='utf-8') as fd:
#     from_file = fd.readlines()
#     print(from_file)
#
# with open('myfile2.txt', 'w', encoding='utf-8') as fd:
#     lines = ['строка\n', 'ещё строка\n', 'и ещё одна строчка\n']
#     fd.writelines(lines)
# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в текстовом файле
# 3. Пользователь может ввести одну из характеристик для поиска определенной записи
#    (Например имя или фамилию человека)
# main.py
# FILE_NAME = 'phone_book.txt'
#     from typing import List

#     def clear_console():
#         os.system('clear')



#     def copy_to_file (file, data):
#         pass
#     def copy_to_file (file,data,export_ind):
#         list_contacts = []
#     counter = 0
#     if len(data)>0:
#         for i in export_ind:
#             line = data[i-1].split(', ')
#             list_contacts.append({})
#             list_contacts[counter]['last_name'] = line[1]
#             list_contacts[counter]['first_name'] = line[0]
#             list_contacts[counter]['patronymic'] = line[2]
#             list_contacts[counter]['phone_number'] = line[3]                            
#             counter+=1


#         try:
#             with open(file, 'w', newline='', encoding='utf-8') as csv_file:
#                     fieldnames = list_contacts[0].keys()
#                     writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
#                     writer.writeheader()
#                     writer.writerows(list_contacts)  
#             print ('Файл создан успешно')
#         except Exception as exc:
#             print ('Возникли проблемы при сохранении:',exc)


#     def edit_line (data,idx,file_name):
#         print ("Что будем изменять 1 - Имя, 2 - Фамилию, 3 - Отчество, 4 - телефон:")
#         answer = int(input())-1
#         print ('Введите новое значение')
#         pars = data[idx].split(', ')
#         pars[answer] = input()
#         data[idx] = ', '.join(pars)
#         # print (data)
#         # for line in data:
#         #             line = line.split(', ')
#         #             print (line)
#         #             print(f'{line[0]}, {line[1]}, {line[2]}, {line[3]}\n')
#         print (['Ошибка редактирования','изменения зафиксированы'][save_data(file_name,data)]   )

#     def save_data (file,data):
#         try:
#             if len(data)>0:
#                 with open(file, 'w', encoding='utf-8') as f:
#                     f.seek(0)
#                 f.writelines(data)

#                 # for line in data:
#                 #     line = line.split(', ')
#                 #     print (f'{line[0]}, {line[1]}, {line[2]}, {line[3]}\n')
#                 #     f.write2(f'{line[0]}, {line[1]}, {line[2]}, {line[3]}\n')
#                 f.truncate()
#             return True
#         except:
#                 return False



# def read_file(file):
    
#     #@@ -48,28 +77,13 @@ 
#     def read_file(file):

#         def show_data(data: list):
#             print()
# print (data)
# print('Содержимое справочника:')
    
# for line in enumerate(data):
#         print(line[0]+1,line[1])
    # with open('phone_book.txt', 'r', encoding='utf-8') as f:
    #     lines = f.readlines()
    #     for line in lines:
    #         print(line)
    # FileNotFoundError
    # try:
    #     # print('открытие файла')
    #     with open('phone_book.txt', 'r', encoding='utf-8') as f:
    #         lines = f.readlines()
    #         for line in lines:
    #             print(line)
    # except FileNotFoundError as err:
    #     print('файла нет. Сначала введите данные\n')
    # else:
    #     print('else')
    # finally:
    #     print('finally')

# def save_data(file):
#     print ()

#     def add_data(file):
#         print('Введите данные контакта:')
#     first_name = input('Введите имя: ')
#     last_name = input('Введите фамилию: ')
#     #@@ -104,12 +118,13 @@ 
#     def main():
#         print('1 - запись в файл')
#         print('2 - показать записи')
#         print('3 - найти запись')
#         print('4 - редактировать запись')
#         print('5 - экспорт выбранных контактов в csv файл')      
#     answer = input('Выберите действие: ')
#     if answer == '0':
#         flag = False
#     elif answer == '1':
#         save_data(file_name)
#         add_data(file_name)
#     elif answer == '2':
#         data = read_file(file_name)
#         show_data(data)
#     #@@ -118,11 +133,24 @@ 
#     #def main():
#         founded_data = search_data(data)
#     show_data(founded_data)
    
#     elif answer == '4':
#     data = read_file(file_name)
#     show_data(data) 
#     print ('Введите номер строки для редактирования:') 
#     idx = int(input())-1
#     edit_line(data,idx,file_name)

#     elif answer == '5':
#     print ("введите имя файла для экспорта (без расширения)", end = ' ')
#     csv_file_name = input().strip()+'.csv'
#     print (csv_file_name)
#     data = read_file(file_name)            
#     show_data(data)
#     print ('Введите номера строк для импорта через запятую: ')
#     export_num = list(map(int,input().split(',')))
#     if max(export_num)>len(data):
#         print ('Введеный номер строки больше максимальной, продолжение невозможно.') 
#     else:
#         copy_to_file ( csv_file_name ,data,export_num)    


#     if __name__ == '__main__':
#         if os.path.exists(file_name):
#             print ('Найден и загружен телефонный справочник')
#         data = read_file(file_name)
#         flag = True
#     flag = True

#     while flag:
#         print('0 - выход')



# import pandas as pd
# import seaborn as sns
# import matplotlib.pyplot as plt

# penguins = pd.read_csv("penguins.csv")
# print(penguins.head())
# print(penguins.columns)
# print(penguins.describe())
# print(penguins.isnull().sum())
# penguins.dropna(inplace=True)
# print(penguins.head())
# print(penguins.isnull().sum())
# # sns.scatterplot(data=penguins, x="species", y="body_mass_g", hue="sex")
# # sns.scatterplot(data=penguins, x="bill_length_mm", y="bill_depth_mm", hue="species", style="sex")
# # sns.PairGrid(penguins, hue='species').map(sns.scatterplot).add_legend()
# # sns.heatmap(data=penguins.corr(numeric_only=True), annot = True, vmin=-1, vmax=1, center= 0, cmap= 'crest',
# #             cbar_kws= {'orientation': 'horizontal'})
# # df.loc[df['housing_median_age'] <= 20, 'age_group'] = 'Молодые'
# # df.loc[(df['housing_median_age'] > 20) & (df['housing_median_age'] <= 50), 'age_group'] = 'Ср. возраст'
# # df.loc[df['housing_median_age'] > 50, 'age_group'] = 'Пожилые'
# penguins.loc[penguins['bill_length_mm'] >= 42, "bill_size"] = "high"
# penguins.loc[(penguins['bill_length_mm'] >= 35) & (penguins['bill_length_mm'] < 42), "bill_size"] = "middle"
# penguins.loc[penguins['bill_length_mm'] < 35, "bill_size"] = "low"

# sns.histplot(data=penguins, x="flipper_length_mm", hue="bill_size")
# plt.show()

# #pip3 install pandas
# import pandas as pd
# import random

# # Создание DataFrame с данными
# lst = ['robot'] * 10 + ['human'] * 10
# random.shuffle(lst)
# data = pd.DataFrame({'whoAmI': lst})

# # Получение уникальных значений из столбца 'whoAmI'
# unique_values = data['whoAmI'].unique()

# # Создание новых столбцов по уникальным значениям и заполнение нулями
# for value in unique_values:
#     data[value] = (data['whoAmI'] == value).astype(int)

# # Удаление исходного столбца 'whoAmI'
# data = data.drop('whoAmI', axis=1)

# data.head()

# print(data.head())
