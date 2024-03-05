FILE = dynamic_baseISA_susan dynamic_C_susan dynamic_Zca_susan dynamic_Zcb_susan dynamic_Zcd_susan dynamic_Zce_susan dynamic_Zcmp_susan dynamic_Zcmt_susan
objdump: ${FILE} Makefile
	/afs/inf.ed.ac.uk/user/s20/s2011935/llvm_install/bin/llvm-objdump -d dynamic_baseISA_susan > base_susan_objdump.txt
	/afs/inf.ed.ac.uk/user/s20/s2011935/llvm_install/bin/llvm-objdump -d dynamic_C_susan > C_susan_objdump.txt
	/afs/inf.ed.ac.uk/user/s20/s2011935/llvm_install/bin/llvm-objdump -d dynamic_Zca_susan > Zca_susan_objdump.txt
	/afs/inf.ed.ac.uk/user/s20/s2011935/llvm_install/bin/llvm-objdump -d dynamic_Zcd_susan > Zcd_susan_objdump.txt
	/afs/inf.ed.ac.uk/user/s20/s2011935/llvm_install/bin/llvm-objdump -d dynamic_Zcb_susan > Zcb_susan_objdump.txt
	/afs/inf.ed.ac.uk/user/s20/s2011935/llvm_install/bin/llvm-objdump -d dynamic_Zcmp_susan > Zcmp_susan_objdump.txt
	/afs/inf.ed.ac.uk/user/s20/s2011935/llvm_install/bin/llvm-objdump -d dynamic_Zcmt_susan > Zcmt_susan_objdump.txt
	/afs/inf.ed.ac.uk/user/s20/s2011935/llvm_install/bin/llvm-objdump -d dynamic_Zce_susan > Zce_susan_objdump.txt

susan: susan.c Makefile
	/afs/inf.ed.ac.uk/user/s20/s2011935/llvm_install/bin/clang -Os -march=rv64ifd_zce -mabi=lp64d -msave-restore -o susan susan.c -lm 
	mv susan dynamic_Zce_susan
clean:
	rm -rf susan output*
