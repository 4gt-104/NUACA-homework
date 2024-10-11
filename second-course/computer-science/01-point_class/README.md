# OOP in Python and CPP

The main goal of this assignment is to create a ``Point`` class, representing a point on a 2D surface, with methods to move along axes, compute distances between points, and more. The class was first implemented in Python and then rewritten in C++. Assignment for ``11.10.2024`` OOP Class.

Both implementations come with three test programs to verify the functionality of the class.

## Requirements

* Ensure your Python version is around `~=3.8`.
* Ensure your compiler supports the ``C++11`` standard.

## Running test cases
### To run the Python implementation:
From the assignment's root directory, run the following commands:

```bash
cd python/
python3 test1.py
python3 test2.py
python3 test3.py
```

### To run the C++ implementation:
From the assignment's root directory, run the following commands:

```bash
cd cpp/
g++ -o test1 test1.cpp
g++ -o test2 test2.cpp
g++ -o test3 test3.cpp
./test1
./test2
./test3
```