""" Test the dep_graph function by asserting certain list as an output.
    This way we can verify if the result is the one expected.

    Also checks the exception for the circle.
"""
from dep_graph import dep_graph
import os
import pytest

folder_path = './tmp'  # initial path of the folders.
list_of_tests = []  # list with all the json, that we test.

# Loop through the folder to get all the dependencies.
for root, dirs, files in os.walk(folder_path):
    for file in files:
        file_path = os.path.join(root, file)
        list_of_tests.append(file_path)


class TestClass:
    """ Grouping tests in class TestClass.
    """

    def test_initial(self):
        path = list_of_tests[0]
        assert dep_graph(path) == ['pkg1', 'pkg2',
                                   'pkg3', 'pkg3', 'pkg2', 'pkg3', 'pkg3']

    def test_scale(self):
        path = list_of_tests[1]
        assert dep_graph(path) == ["pkg1", "pkg2", "pkg3", "pkg4", "pkg4", "pkg3",
                                   "pkg4", "pkg2", "pkg3", "pkg4", "pkg4", "pkg3", "pkg4", "pkg4", ]

    def test_circle(self):
        path = './tmp/deps2.json'
        with pytest.raises(Exception, match="Ups") as e_info:
            dep_graph(path)
            print(e_info)

    def test_empty(self):
        path = './tmp/deps3.json'
        assert dep_graph(path) == ['pkg1', 'pkg2', 'pkg3']

    def test_bigger(self):
        path = './tmp/deps4.json'
        assert dep_graph(path) == ['pkg1', 'pkg2', 'pkg3', 'pkg4', 'pkg5', 'pkg4', 'pkg5', 'pkg3', 'pkg4', 'pkg5', 'pkg4',
                                   'pkg5', 'pkg5', 'pkg2', 'pkg3', 'pkg4', 'pkg5', 'pkg4', 'pkg5', 'pkg3', 'pkg4', 'pkg5', 'pkg4', 'pkg5', 'pkg5']
