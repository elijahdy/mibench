FILE1 = basicmath_small.c   rad2deg.c  cubic.c   isqrt.c
FILE2 = basicmath_large.c   rad2deg.c  cubic.c   isqrt.c

all: basicmath_small basicmath_large

basicmath_small: ${FILE1} Makefile
	gcc-13 -static -mcpu=sifive-e76  -Os -march=rv64ifd_zca -mabi=lp64d -msave-restore ${FILE1} -o basicmath_small -lm
basicmath_large: ${FILE2} Makefile
	gcc-13 -static -Os -march=rv64ifdc -mabi=lp64d -msave-restore ${FILE2} -o basicmath_large -lm

clean:
	rm -rf basicmath_small basicmath_large output*
