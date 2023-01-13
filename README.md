# dep_graph

This program reada a JSON file from a fixed filesystem location, e.g. /tmp/deps.json, containing a list of packages and their dependencies.
In this JSON file, a key represents a package name, and the value is a list of dependencies (package names) for that key:
```sh
{
  "pkg1": ["pkg2", "pkg3"],
  "pkg2": ["pkg3"],
  "pkg3": []
}
```

The the goal is to traverse the whole graph for every dependency. The result is a list containing all the visited dependencies.

```sh
  Full Dependency Graph.
  
  ['pkg1', 'pkg2', 'pkg3', 'pkg3', 'pkg2', 'pkg3', 'pkg3']
```


<!-- GETTING STARTED -->
## Getting Started

Clone the repository.
  ```sh
  git clone https://github.com/AggelosMargkas/dep_graph.git
  ```
      

### Install requirements 

Install the requirement.
  ```sh
  pip install -r requirement.txt
  ```

### Run dep_graph.

To run dep_graph you need to run the command below.

Run dep_graph.
   ```sh
   python -m dep_graph
   ```
 
### Run dep_graph.

To test it run.
   ```sh
   pytest test_dep_graph.py
   ```

