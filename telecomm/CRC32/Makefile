FILE = dynamic_baseISA_crc dynamic_C_crc dynamic_Zca_crc dynamic_Zcb_crc dynamic_Zcd_crc dynamic_Zce_crc dynamic_Zcmp_crc dynamic_Zcmt_crc
objdump: ${FILE} Makefile
	/afs/inf.ed.ac.uk/user/s20/s2011935/llvm_install/bin/llvm-objdump -d dynamic_baseISA_crc > base_crc_objdump.txt
	/afs/inf.ed.ac.uk/user/s20/s2011935/llvm_install/bin/llvm-objdump -d dynamic_C_crc > C_crc_objdump.txt
	/afs/inf.ed.ac.uk/user/s20/s2011935/llvm_install/bin/llvm-objdump -d dynamic_Zca_crc > Zca_crc_objdump.txt
	/afs/inf.ed.ac.uk/user/s20/s2011935/llvm_install/bin/llvm-objdump -d dynamic_Zcd_crc > Zcd_crc_objdump.txt
	/afs/inf.ed.ac.uk/user/s20/s2011935/llvm_install/bin/llvm-objdump -d dynamic_Zcb_crc > Zcb_crc_objdump.txt
	/afs/inf.ed.ac.uk/user/s20/s2011935/llvm_install/bin/llvm-objdump -d dynamic_Zcmp_crc > Zcmp_crc_objdump.txt
	/afs/inf.ed.ac.uk/user/s20/s2011935/llvm_install/bin/llvm-objdump -d dynamic_Zcmt_crc > Zcmt_crc_objdump.txt
	/afs/inf.ed.ac.uk/user/s20/s2011935/llvm_install/bin/llvm-objdump -d dynamic_Zce_crc > Zce_crc_objdump.txt

crc: crc_32.c Makefile
	/afs/inf.ed.ac.uk/user/s20/s2011935/llvm_install/bin/clang -static -Os -march=rv64ifd_zcmt -mabi=lp64d -msave-restore  crc_32.c -o crc 
	mv crc static_Zcmt_crc
clean:
	rm -rf crc output*
