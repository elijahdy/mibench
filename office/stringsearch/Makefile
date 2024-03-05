FILE1 = bmhasrch.c  bmhisrch.c  bmhsrch.c  pbmsrch_small.c 
FILE2 = bmhasrch.c  bmhisrch.c  bmhsrch.c  pbmsrch_large.c 
FILE = dynamic_baseISA_search_large dynamic_C_search_large dynamic_Zca_search_large dynamic_Zcb_search_large dynamic_Zcd_search_large dynamic_Zce_search_large dynamic_Zcmp_search_large dynamic_Zcmt_search_large
objdump: ${FILE} Makefile
	/afs/inf.ed.ac.uk/user/s20/s2011935/llvm_install/bin/llvm-objdump -d dynamic_baseISA_search_large > base_search_large_objdump.txt
	/afs/inf.ed.ac.uk/user/s20/s2011935/llvm_install/bin/llvm-objdump -d dynamic_C_search_large > C_search_large_objdump.txt
	/afs/inf.ed.ac.uk/user/s20/s2011935/llvm_install/bin/llvm-objdump -d dynamic_Zca_search_large > Zca_search_large_objdump.txt
	/afs/inf.ed.ac.uk/user/s20/s2011935/llvm_install/bin/llvm-objdump -d dynamic_Zcd_search_large > Zcd_search_large_objdump.txt
	/afs/inf.ed.ac.uk/user/s20/s2011935/llvm_install/bin/llvm-objdump -d dynamic_Zcb_search_large > Zcb_search_large_objdump.txt
	/afs/inf.ed.ac.uk/user/s20/s2011935/llvm_install/bin/llvm-objdump -d dynamic_Zcmp_search_large > Zcmp_search_large_objdump.txt
	/afs/inf.ed.ac.uk/user/s20/s2011935/llvm_install/bin/llvm-objdump -d dynamic_Zcmt_search_large > Zcmt_search_large_objdump.txt
	/afs/inf.ed.ac.uk/user/s20/s2011935/llvm_install/bin/llvm-objdump -d dynamic_Zce_search_large > Zce_search_large_objdump.txt

all: search_small search_large

search_small: ${FILE1} Makefile
	gcc -static ${FILE1} -O3 -o search_small

search_large: ${FILE2} Makefile
	/afs/inf.ed.ac.uk/user/s20/s2011935/llvm_install/bin/clang -Os -march=rv64ifd_zce -mabi=lp64d -msave-restore ${FILE2} -o search_large
	mv search_large dynamic_Zce_search_large
clean:
	rm -rf search_small search_large output*
