FILE1 = basicmath_small.c   rad2deg.c  cubic.c   isqrt.c
FILE2 = basicmath_large.c   rad2deg.c  cubic.c   isqrt.c

all: basicmath_small basicmath_large

basicmath_small: ${FILE1} Makefile
	/home/elijah/llvm_install/bin/clang-18 -static --target=riscv64 -Os -march=rv64i -mabi=lp64 --sysroot=/home/elijah/rv64_gnu_install/riscv64-unknown-elf --gcc-toolchain=/home/elijah/rv64_gnu_install/ ${FILE1} -o basicmath_small -lm
basicmath_large: ${FILE2} Makefile
	gcc -static ${FILE2} -o basicmath_large -lm

clean:
	rm -rf basicmath_small basicmath_large output*
