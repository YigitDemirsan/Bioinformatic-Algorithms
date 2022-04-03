# Homework question 3A
def string_composition(text, k):
    composition = []
    length = 0
    while length < (len(text) - k + 1):
        composition.append(text[length:length + k])
        length = length + 1
    return composition


# Homework question 3C
def overlapped_graph(collections):
    graph = {}
    for i in collections:
        graph[i] = []
    for i in graph:
        for j in collections:
            if i[1:] == j[:-1]:
                graph[i].append(j)
    return graph


# Homework question 3E
def graph_path(text, k):
    edge = string_composition(text, k)
    graph = []
    for i in edge:
        graph.append([i[:-1], i[1:]])
    return graph


def bruijn_graph_problem(collection, k):
    path = graph_path(collection, k)
    length = 0
    for i in path:
        for j in path[length + 1:]:
            if i[0] == j[0]:
                i.append([j[1]])
        length = length + 1

    final = []
    have_it = {}
    check = set(have_it)
    for i in path:
        check.add(i[0])
    for i in path:
        if i[0] in check:
            final.append(i)
            check.remove(i[0])


# Homework question 3F
def euler_cycle_problem(graph):
    degree_of_the_graph = graph.degrees()
    odd_vertices = [vertex for vertex in degree_of_the_graph.keys() if degree_of_the_graph[vertex] % 2 == 1]
    if len(odd_vertices) == 2:
        vertex_init = odd_vertices[0]
    elif len(odd_vertices) == 0:
        vertex_init = graph.some_vertex()
    else:
        return None
    list_of_stack = [vertex_init]
    path = []
    while list_of_stack:
        item = list_of_stack[-1]
        vertex = graph.adjacent_vertex(item)
        if vertex:
            list_of_stack.append(vertex)
            graph.delete_edge((item, vertex))
        else:
            path.append(list_of_stack.pop())

    return path
