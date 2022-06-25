#Перечислить методы списка(list)

''' index, append, count, pop, insert, reverse, sort, remove'''

#Написать их через запятую с параметрами

#index(element [,start [, end]])
elements = ['a', 'b', 'c', 'd', 'e']
print(elements.index('c'))

#append(item)
elements.append('f')
print(elements)

#count(element)
elements.append('f')
print(elements.count('f'))

#pop([index])
elements.pop(0)
print(elements)

#insert(index, element)
elements.insert(0, 'a')
print(elements)

#reverse
elements.reverse()
print(elements)

#sort([key [, reverse]])
elements.sort()
print(elements)

#remove(element)
elements.remove('f')
print(elements)

#Отсортировать методы по частоте использования (по вашему мнению)

'''append, count, pop, insert, remove, sort, index, reverse'''

#Прокомментировать свой выбор

'''Данный выбор обусловлен субъективным мнением частоты применения методов. 
Во первых метод APPEND скорее наиболее употребим, так как позволяет добовлять элементы 
в уже сформированные списки, а это наиболее востребованное действие. 
Метод COUNT позволяет оперативно получать информацию о количестве элементов в списке, 
что на мой взгляд является наиболее востребованной информацией.
Метод POP позволяет точечно удалять элементы из списка, что также является востребованной функцией.'''

#в пункте 3 дополнительно к приведению к нижнему регистру выполнить лемматизацию.