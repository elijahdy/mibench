FILE = dynamic_baseISA_sha dynamic_C_sha dynamic_Zca_sha dynamic_Zcb_sha dynamic_Zcd_sha dynamic_Zce_sha dynamic_Zcmp_sha dynamic_Zcmt_sha
objdump: ${FILE} Makefile
	/afs/inf.ed.ac.uk/user/s20/s2011935/llvm_install/bin/llvm-objdump -d -M no-aliases dynamic_baseISA_sha > base_sha_objdump.txt
	/afs/inf.ed.ac.uk/user/s20/s2011935/llvm_install/bin/llvm-objdump -d -M no-aliases dynamic_C_sha > C_sha_objdump.txt
	/afs/inf.ed.ac.uk/user/s20/s2011935/llvm_install/bin/llvm-objdump -d -M no-aliases dynamic_Zca_sha > Zca_sha_objdump.txt
	/afs/inf.ed.ac.uk/user/s20/s2011935/llvm_install/bin/llvm-objdump -d -M no-aliases dynamic_Zcd_sha > Zcd_sha_objdump.txt
	/afs/inf.ed.ac.uk/user/s20/s2011935/llvm_install/bin/llvm-objdump -d -M no-aliases dynamic_Zcb_sha > Zcb_sha_objdump.txt
	/afs/inf.ed.ac.uk/user/s20/s2011935/llvm_install/bin/llvm-objdump -d -M no-aliases dynamic_Zcmp_sha > Zcmp_sha_objdump.txt
	/afs/inf.ed.ac.uk/user/s20/s2011935/llvm_install/bin/llvm-objdump -d -M no-aliases dynamic_Zcmt_sha > Zcmt_sha_objdump.txt
	/afs/inf.ed.ac.uk/user/s20/s2011935/llvm_install/bin/llvm-objdump -d -M no-aliases dynamic_Zce_sha > Zce_sha_objdump.txt

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
