import sys

g = [
	"hirosima",
	"nagasaki"
]

names = [
	"Bob",
	"Siryoga"
]

g.append("bomba") 			#Добавить в конец списка элемент
g.extend(names) 			#Добавить в конец списка элементы другого списка
g.insert(1, "DESTROYER") 	#Добавить в элемент списка i элемент "DESTROYER"
g.remove("bomba") 			#Удалить из списка элемент
g.pop() 					#Удаляет последний элемент списка и возвращает его, если указать i , то удаляет i элемент и возвращает его
g.index("hirosima")			#Возвращает индекс указанного элемента
g.count("Bob")				#Выдает, сколько таких элементов в списке
g.sort()					#Сортирует список
g.reverse()					#Переворачивает список
g.clear()					#Очистка списка, вывод будет -> []

g.append("qwe")
g.append("rty")
g.append("uio")

print(g)
print(g.pop())
print(g)



print(g[0])



#Словари (dict)

di = {1 : "MyName", "key2" : "pizdec"}
print(di["key2"])

piz = dict (small = "Vika", big = "Danya")
piz['big'] = "dick"
print(piz['big'])

person = {'name' : {'first_name' : "Daniil", 'second_name' : "Shashev"},'dick' : [13, 15, 17], 'phone' : {'home_phone' : "517391", 'mobile_phone' : "+79635098584"}}
print(person['dick'][1])