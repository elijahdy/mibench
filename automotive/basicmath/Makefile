FILE1 = basicmath_small.c   rad2deg.c  cubic.c   isqrt.c
FILE2 = basicmath_large.c   rad2deg.c  cubic.c   isqrt.c

all: basicmath_small basicmath_large

basicmath_small: ${FILE1} Makefile
	/afs/inf.ed.ac.uk/user/s20/s2011935/llvm_install/bin/clang -static -Os -march=rv64ifd -mabi=lp64d -msave-restore ${FILE1} -o basicmath_small -lm
basicmath_large: ${FILE2} Makefile
	/afs/inf.ed.ac.uk/user/s20/s2011935/llvm_install/bin/clang -static -Os -march=rv64ifd -mabi=lp64d -msave-restore ${FILE2} -o basicmath_large -lm
	mv basicmath_large static_baseISA_basicmath_large
clean:
	rm -rf basicmath_small basicmath_large output*
