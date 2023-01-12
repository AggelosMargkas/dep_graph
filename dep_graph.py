import json
from collections import deque

INITIAL_PATH = './tmp/deps.json'


def read_json_file(filepath):
    with open(filepath, 'r') as f:
        return json.load(f)


def create_dependency_graph(dependencies):
    graph = {}
    for pkg, deps in dependencies.items():
        graph[pkg] = deps
        for dep in deps:
            if dep not in graph:
                graph[dep] = []
    return "Input Graph.. " + str(graph)


def dep_graph(filename):

    output = []
    dependencies = read_json_file(filename)
    graph = create_dependency_graph(dependencies)
    print(graph)
    print("Output graph ..")
    print("\n")

    return temp(dependencies,  output)


def temp(graph, dependency):

    for node in graph:
        queue = deque()
        queue.append(node)

        while queue:
            s = queue.pop()
            dependency.append(s)

            for x in graph[s][::-1]:
                if x == node:
                    raise Exception("Ups, a circle appeared in our dependencies! Sorry, I will never terminate, "
                                    "need to go.")
                else:
                    queue.append(x)

    print(dependency)
    return dependency


dep_graph(INITIAL_PATH)
