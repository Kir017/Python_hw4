# Задача 24: 
# В фермерском хозяйстве в Карелии выращивают чернику. Она растет на круглой грядке, причем кусты высажены только по окружности. 
# Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растет N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло различное число ягод – на i-ом кусте выросло ai ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники. Эта система состоит из управляющего модуля и нескольких 
# собирающих модулей. Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом, собирает ягоды с этого куста и с 
# двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может собрать за один заход собирающий модуль, находясь перед некоторым 
# кустом заданной во входном файле грядки.

list1 = input('Введите количество ягод на каждом кусте: ').split()
newList = []
if len(list1) >= 3:
    for i in range(1,len(list1) - 1):
        newList.append(int(list1[i-1]) + int(list1[i]) + int(list1[i+1]))
    newList.append(int(list1[-2]) + int(list1[-1]) + int(list1[0]))
    print(newList)
    print('Максимальное число ягод за один заход =', max(newList))
else:
    count = 0 
    for i in list1:
        count = count + int(i)
    print(count)