# judge.py
Simple and easy-to-use judger for ACM/OI use.

## Quick Start
### Change Current Folder

```
cd [path to judge.py]
```

### Generate New Problem Database

```
./judge.py generate [problem name]
```

which would make a new folder with a default configuration file if it does not exist.

**NOTICE**: All the problem will put into the `data` folder.

### Setup the Problem
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
    "input_suffix": "in",  // Input file extension
    "output_suffix": "out",  // Output file extension
    "name_format": "{0}{1}.{2}",  // Formatting: 0: name, 1: id, 2:in/out
    "time_limit": 1.0,  // Time limit in seconds
    "memory_limit": 128.0,  // Memory limit in MBs
    "special_judge": false  // Special judge
}
```

NOTICE: If you have enabled `special_judge`, you have to put `_spj.py` into your problem folder, renaming it to `spj.py`. Then `judge.py` will use `spj.py` to judge the score instead of simple diff.

### Run Your Solution
Put your solution `xxxx.cpp` into `source` folder, then:

```
./judge.py xxxx
```

will run the judgement.

### Datagen Extension
If you have the standard program, you can judge it in `datagen` mode:

```
./judge.py datagen xxxx
```

Then all the output of the program will be put into the problem folder as `out` files.

