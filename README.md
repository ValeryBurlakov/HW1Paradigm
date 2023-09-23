### Разобрал встроенный метод sorted(), 
### узнал, что он использует 2 алгоритма сортировки, что дает ему хорошую скорость работы от О(n) до O(n log n)
* коллекция разбивается на подколлекции
* каждая коллекция сортируется вставками
* сортировкой слиянием подколлекции сливаются в единую коллекцию
### для решения задачи пришлось добавить метод reverse_list, так как встроенная сортировка не предусматривает расположение по убыванию
