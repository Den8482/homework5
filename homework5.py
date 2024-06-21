immutable_var = 1,2,3,'Printer',False
print(immutable_var)
#immutable_var[0] = 5
#TypeError: 'tuple' object does not support item assignment
#Кортеж не поддерживает обращение к элементам. Изменить элементы внутри кортежа не получится.
mutable_list = [1,2,3,'Printer',False]
mutable_list[3] = 'Mouse'
print(mutable_list)