# judge.py
## Quick Start
1. Change your current folder to `judge.py`:

```
cd [path to judge.py]
```

2. Generate new problem database:

```
./judge.py generate [problem name]
```

which would make a new folder with a default configuration file if it does not exist.

3. Set up he problem:
Firstly, put all your data into the problem folder with format `xxxx.in/out`.
Then set up configure in `xxxx.json`:

```
{
    "name": "xxxx",  // Problem name
    "source_ext": ".cpp",  // Source extension
    "build_file": "a.out",  // Compiler output file (executable)
    "compiler": "g++ -O0 -std=c++11",  // Compile command line
    "start_id": 1,  // Start at xxxx1.in/out
    "end_id": 10,  // End at xxxx10.in/out
    "name_format": "{0}{1}.{2}",  // Formatting: 0: name, 1: id, 2:in/out
    "time_limit": 1.0,  // Time limit in seconds
    "memory_limit": 128.0,  // Memory limit in MBs
    "special_judge": false  // Special judge
}
```

NOTICE: If you have enabled `special_judge`, you have to put `_spj.py` into your problem folder, renaming it to `spj.py`. Then `judge.py` will use `spj.py` to judge the score instead of simple diff.

4. Run your solution:
Put your solution `xxxx.cpp` into `judge.py`'s folder, then:

```
./judge.py xxxx
```
will run the judgement.

5. Datagen extensions:
If you have the standard program, you can judge it in `datagen` mode:

```
./judge.py datagen xxxx
```

Then all the output of the program will be put into the problem folder as `out` files.

