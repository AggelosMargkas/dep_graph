"""
    
    This program reads a JSON file from a fixed filesystem location, e.g. /tmp/deps.json,
    containing a list of packages and their dependencies and

    traverses the dependencies loaded from the JSON file and reconstruct the full dependency graph.

"""

import json
from collections import deque

INITIAL_PATH = './tmp/deps.json'  # This is the initial location.


def read_json_file(filepath):
    """ Reads a path of the .json dependencies.

    Args:
        filepath (str): The path to the initial folder.

    Returns:
        f: The conversion of a json to dictionary.
    """
    with open(filepath, 'r') as f:
        return json.load(f)


def create_dependency_graph(dependencies):
    """ Reads the dictionary to a string for reading.

    Args:
        dependencies (dictionary): Input dependencies.

    Returns:
        String: The input graph in a string.
    """
    graph = {}
    for pkg, deps in dependencies.items():
        graph[pkg] = deps
        for dep in deps:
            if dep not in graph:
                graph[dep] = []
    return "Input Graph.. " + str(graph)


def dep_graph(filename):
    """A filename as an input and returns an object representing the fully resolved graph.

    Args:
        filename (str): The input folder.

    Returns:
        list: A list with all the dependencies that it visited.
    """

    output = []  # The list of the output.
    dependencies = read_json_file(filename)
    graph = create_dependency_graph(dependencies)

    print(graph)
    print("Output graph ..")
    print("\n")

    return depth_traverse(dependencies,  output)


def depth_traverse(graph, dependency):
    """ Uses a DFS logic. Uses a deque() for collecting all the dependencies.
        When it meets a dependency it sees the kids of it and adds it in the queue.
        Uses LIFO.

    Args:
        graph (dic): The initial dependencies.
        dependency (str): The root of the graph.

    Raises:
        Exception: If we have a circle it raises an exception.

    Returns:
        dependency: Object of all dependencies visited.
    """
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
