from dep_graph import dep_graph
import pytest
import os

folder_path = './tmp'
list_of_tests = []

for root, dirs, files in os.walk(folder_path):
    for file in files:
        file_path = os.path.join(root, file)
        list_of_tests.append(file_path)


class TestClass:

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
