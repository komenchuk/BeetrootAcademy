# Задаем граф (в данном случае с картинки)
graph = {'Math-151': ['CS-220'],
         'CS-220': ['CS-151', 'CS-360', 'CS-477'],
         'CS-150': ['CS-220', 'CS-151', 'CS-250'],
         'CS-151': ['CS-360', 'CS-250', 'CS-230'],
         'CS-250': ['CS-466'],
         'CS-230': ['CS-466'],
         'CS-466': ['CS-360', 'CS-250', 'CS-477', 'CS-490'],
         'CS-360': ['CS-466', 'CS-490'],
         'CS-477': ['CS-490'],
         'CS-490': ['CS-230']}


# Пишем функцию dfs_paths для поиска пути между двумя вершинами
def dfs_paths(graph, start, goal):
    stack = [(start, [start])]
    while stack:
        (vertex, path) = stack.pop()  # vertex - вершина, path - путь
        for next in set(graph[vertex]) - set(path):
            if next == goal:
                yield path + [next]
            else:
                stack.append((next, path + [next]))


# Пишем функцию shortest_path - для нахождения кратчайшего пути от вершины к вершине
def shortest_path(graph, start, goal):
    try:
        return next(dfs_paths(graph, start, goal))
    except StopIteration:
        return None


# Пользователь задаёт две случайные вершины из существующих
user_vertex_1 = input('Выберите 1-ю вершину: ')
user_vertex_2 = input('Выберите 2-ю вершину: ')

# Выводим варианты всех путей для заданых вершин списками
print(list(dfs_paths(graph, user_vertex_1, user_vertex_2)))
print(shortest_path(graph, user_vertex_1, user_vertex_2))
