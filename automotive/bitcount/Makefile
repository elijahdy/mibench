FILE = bitcnt_1.c bitcnt_2.c bitcnt_3.c bitcnt_4.c bitcnts.c bitfiles.c bitstrng.c bstr_i.c 
FILE2 = dynamic_baseISA_bitcnts dynamic_C_bitcnts dynamic_Zca_bitcnts dynamic_Zcb_bitcnts dynamic_Zcd_bitcnts dynamic_Zce_bitcnts dynamic_Zcmp_bitcnts dynamic_Zcmt_bitcnts


bitcnts: ${FILE} Makefile
	/afs/inf.ed.ac.uk/user/s20/s2011935/llvm_install/bin/clang -Os -static -march=rv64ifd -mabi=lp64d -msave-restore ${FILE} -o bitcnts
	mv bitcnts static_baseISA_bitcnts
objdump: ${FILE2} Makefile
	/afs/inf.ed.ac.uk/user/s20/s2011935/llvm_install/bin/llvm-objdump -d dynamic_baseISA_bitcnts > base_bitcnts_objdump.txt
	/afs/inf.ed.ac.uk/user/s20/s2011935/llvm_install/bin/llvm-objdump -d dynamic_C_bitcnts > C_bitcnts_objdump.txt
	/afs/inf.ed.ac.uk/user/s20/s2011935/llvm_install/bin/llvm-objdump -d dynamic_Zca_bitcnts > Zca_bitcnts_objdump.txt
	/afs/inf.ed.ac.uk/user/s20/s2011935/llvm_install/bin/llvm-objdump -d dynamic_Zcd_bitcnts > Zcd_bitcnts_objdump.txt
	/afs/inf.ed.ac.uk/user/s20/s2011935/llvm_install/bin/llvm-objdump -d dynamic_Zcb_bitcnts > Zcb_bitcnts_objdump.txt
	/afs/inf.ed.ac.uk/user/s20/s2011935/llvm_install/bin/llvm-objdump -d dynamic_Zcmp_bitcnts > Zcmp_bitcnts_objdump.txt
	/afs/inf.ed.ac.uk/user/s20/s2011935/llvm_install/bin/llvm-objdump -d dynamic_Zcmt_bitcnts > Zcmt_bitcnts_objdump.txt
	/afs/inf.ed.ac.uk/user/s20/s2011935/llvm_install/bin/llvm-objdump -d dynamic_Zce_bitcnts > Zce_bitcnts_objdump.txt
clean:
	rm -rf bitcnts output*
