FILE1 = qsort_small.c
FILE2 = qsort_large.c

all: qsort_small qsort_large

qsort_small: qsort_small.c Makefile
	clang -static -Os -menable-experimental-extensions  -march=rv64ifd_zca0p70_zcf0p70_zcd0p70 -mabi=lp64d qsort_small.c -o qsort_small -lm
qsort_large: qsort_large.c Makefile
	/afs/inf.ed.ac.uk/user/s20/s2011935/llvm_install/bin/clang -Os -march=rv64ifd_zce -mabi=lp64d -msave-restore qsort_large.c -o qsort_large -lm
	mv qsort_large dynamic_Zce_qsort_large
clean:
	rm -rf qsort_small qsort_large output*
