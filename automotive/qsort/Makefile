FILE1 = qsort_small.c
FILE2 = qsort_large.c
FILE2 = dynamic_baseISA_qsort_large dynamic_C_qsort_large dynamic_Zca_qsort_large dynamic_Zcb_qsort_large dynamic_Zcd_qsort_large dynamic_Zce_qsort_large dynamic_Zcmp_qsort_large dynamic_Zcmt_qsort_large


all: qsort_small qsort_large

qsort_small: qsort_small.c Makefile
	clang -static -Os -menable-experimental-extensions  -march=rv64ifd_zca0p70_zcf0p70_zcd0p70 -mabi=lp64d qsort_small.c -o qsort_small -lm
qsort_large: qsort_large.c Makefile
	/afs/inf.ed.ac.uk/user/s20/s2011935/llvm_install/bin/clang -Os -march=rv64ifd_zce -mabi=lp64d -msave-restore qsort_large.c -o qsort_large -lm
	mv qsort_large dynamic_Zce_qsort_large
objdump: ${FILE2} Makefile
	/afs/inf.ed.ac.uk/user/s20/s2011935/llvm_install/bin/llvm-objdump -d -M no-aliases dynamic_baseISA_qsort_large > base_qsort_large_objdump.txt
	/afs/inf.ed.ac.uk/user/s20/s2011935/llvm_install/bin/llvm-objdump -d -M no-aliases dynamic_C_qsort_large > C_qsort_large_objdump.txt
	/afs/inf.ed.ac.uk/user/s20/s2011935/llvm_install/bin/llvm-objdump -d -M no-aliases dynamic_Zca_qsort_large > Zca_qsort_large_objdump.txt
	/afs/inf.ed.ac.uk/user/s20/s2011935/llvm_install/bin/llvm-objdump -d -M no-aliases dynamic_Zcd_qsort_large > Zcd_qsort_large_objdump.txt
	/afs/inf.ed.ac.uk/user/s20/s2011935/llvm_install/bin/llvm-objdump -d -M no-aliases dynamic_Zcb_qsort_large > Zcb_qsort_large_objdump.txt
	/afs/inf.ed.ac.uk/user/s20/s2011935/llvm_install/bin/llvm-objdump -d -M no-aliases dynamic_Zcmp_qsort_large > Zcmp_qsort_large_objdump.txt
	/afs/inf.ed.ac.uk/user/s20/s2011935/llvm_install/bin/llvm-objdump -d -M no-aliases dynamic_Zcmt_qsort_large > Zcmt_qsort_large_objdump.txt
	/afs/inf.ed.ac.uk/user/s20/s2011935/llvm_install/bin/llvm-objdump -d -M no-aliases dynamic_Zce_qsort_large > Zce_qsort_large_objdump.txt
clean:
	rm -rf qsort_small qsort_large output*
