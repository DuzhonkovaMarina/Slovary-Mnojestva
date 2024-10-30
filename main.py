my_dict = {'Елена':'Старший специалист','Антон':'Старший специалист','Мария':'Ведущий специалист'}
print(my_dict)
print(my_dict['Антон'])
print(my_dict.get('Ольга'))
my_dict.update({'Олег':'Ведущий специалист','Марина':'Главный специалист'})
a = my_dict.pop('Елена')
print(a)
print(my_dict)
my_set = {7,5,9,'Соня','Гарик',7,7,'Соня', True}
print(my_set)
print(my_set.add(3))
print(my_set.add('Павел'))
print(my_set.discard(7))
print(my_set)