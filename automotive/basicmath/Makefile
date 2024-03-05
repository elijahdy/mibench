FILE1 = basicmath_small.c   rad2deg.c  cubic.c   isqrt.c
FILE2 = basicmath_large.c   rad2deg.c  cubic.c   isqrt.c
FILE3 = dynamic_baseISA_basicmath_large dynamic_C_basicmath_large dynamic_Zca_basicmath_large dynamic_Zcb_basicmath_large dynamic_Zcd_basicmath_large dynamic_Zce_basicmath_large dynamic_Zcmp_basicmath_large dynamic_Zcmt_basicmath_large

all: basicmath_small basicmath_large

basicmath_small: ${FILE1} Makefile
	/afs/inf.ed.ac.uk/user/s20/s2011935/llvm_install/bin/clang -static -O -march=rv64ifd -mabi=lp64d -msave-restore ${FILE1} -o basicmath_small -lm
basicmath_large: ${FILE2} Makefile
	/afs/inf.ed.ac.uk/user/s20/s2011935/llvm_install/bin/clang -static -march=rv64ifd_zce -mabi=lp64d -msave-restore ${FILE2} -o basicmath_large -lm
	mv basicmath_large non_os_test_zce
objdump_all: ${FILE3} Makefile
	/afs/inf.ed.ac.uk/user/s20/s2011935/llvm_install/bin/llvm-objdump -d dynamic_baseISA_basicmath_large > base_basicmath_objdump.txt
	/afs/inf.ed.ac.uk/user/s20/s2011935/llvm_install/bin/llvm-objdump -d dynamic_C_basicmath_large > C_basicmath_objdump.txt
	/afs/inf.ed.ac.uk/user/s20/s2011935/llvm_install/bin/llvm-objdump -d dynamic_Zca_basicmath_large > Zca_basicmath_objdump.txt
	/afs/inf.ed.ac.uk/user/s20/s2011935/llvm_install/bin/llvm-objdump -d dynamic_Zcd_basicmath_large > Zcd_basicmath_objdump.txt
	/afs/inf.ed.ac.uk/user/s20/s2011935/llvm_install/bin/llvm-objdump -d dynamic_Zcb_basicmath_large > Zcb_basicmath_objdump.txt
	/afs/inf.ed.ac.uk/user/s20/s2011935/llvm_install/bin/llvm-objdump -d dynamic_Zcmp_basicmath_large > Zcmp_basicmath_objdump.txt
	/afs/inf.ed.ac.uk/user/s20/s2011935/llvm_install/bin/llvm-objdump -d dynamic_Zcmt_basicmath_large > Zcmt_basicmath_objdump.txt
	/afs/inf.ed.ac.uk/user/s20/s2011935/llvm_install/bin/llvm-objdump -d dynamic_Zce_basicmath_large > Zce_basicmath_objdump.txt
clean:
	rm -rf basicmath_small basicmath_large output*
