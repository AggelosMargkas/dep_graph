# dep_graph

This program must read a JSON file from a fixed filesystem location, e.g. /tmp/deps.json, containing a list of packages and their dependencies. In this JSON file, a key represents a package name, and the value is a list of dependencies (package names) for that key:


<!-- GETTING STARTED -->
## Getting Started

1. Clone the repository.
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

1. Run dep_graph.
   ```sh
   python -m dep_graph
   ```
 
### Run dep_graph.

To test it run.
   ```sh
   pytest test_dep_graph.py
   ```

