# python-cardiac-emu
A simple [CARDIAC](https://en.wikipedia.org/wiki/CARDboard_Illustrative_Aid_to_Computation) emulator written in Python


#### Properties
* Emulates programs written for the CARDIAC architecture
* Ignores behavior left undefined in the specification to keep things simple (e.g., no out-of-bounds checks)
* No dependencies, just plain Python 3.6+ (minimum Python version due to [variable annotations](https://www.python.org/dev/peps/pep-0526/))


#### Caveats
* No explicit support for negative memory cells
* No exception handling: Buggy programs can crash the emulator 
* No debugging tools (yet)


#### Example call
```commandline
$ python3 main.py example_programs/powers_of_2.txt 
001
002
004
008
016
032
064
128
256
512
```


#### Resources and inspiration
* https://www.cs.drexel.edu/~bls96/museum/CARDIAC_manual.pdf
* https://www.cs.drexel.edu/~bls96/museum/cardiac.html