# By default, the code is compiled for a "big endian" machine.
# To compile on a "little endian" machine set the LITTLE_ENDIAN flag.
# To make smaller object code, but run a little slower, don't use UNROLL_LOOPS.
# To use NIST's modified SHA of 7/11/94, define USE_MODIFIED_SHA

CC = /afs/inf.ed.ac.uk/user/s20/s2011935/llvm_install/bin/clang
CFLAGS = -Os -march=rv64ifd_zce -mabi=lp64d -msave-restore 

sha:	sha_driver.o sha.o
	$(CC) -o $@ sha_driver.o sha.o
	mv sha dynamic_Zce_sha

clean:
	rm -rf *.o sha output*
