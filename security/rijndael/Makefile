FILE = dynamic_baseISA_rijndael dynamic_C_rijndael dynamic_Zca_rijndael dynamic_Zcb_rijndael dynamic_Zcd_rijndael dynamic_Zce_rijndael dynamic_Zcmp_rijndael dynamic_Zcmt_rijndael
objdump: ${FILE} Makefile
	/afs/inf.ed.ac.uk/user/s20/s2011935/llvm_install/bin/llvm-objdump -d -M no-aliases dynamic_baseISA_rijndael > base_rijndael_objdump.txt
	/afs/inf.ed.ac.uk/user/s20/s2011935/llvm_install/bin/llvm-objdump -d -M no-aliases dynamic_C_rijndael > C_rijndael_objdump.txt
	/afs/inf.ed.ac.uk/user/s20/s2011935/llvm_install/bin/llvm-objdump -d -M no-aliases dynamic_Zca_rijndael > Zca_rijndael_objdump.txt
	/afs/inf.ed.ac.uk/user/s20/s2011935/llvm_install/bin/llvm-objdump -d -M no-aliases dynamic_Zcd_rijndael > Zcd_rijndael_objdump.txt
	/afs/inf.ed.ac.uk/user/s20/s2011935/llvm_install/bin/llvm-objdump -d -M no-aliases dynamic_Zcb_rijndael > Zcb_rijndael_objdump.txt
	/afs/inf.ed.ac.uk/user/s20/s2011935/llvm_install/bin/llvm-objdump -d -M no-aliases dynamic_Zcmp_rijndael > Zcmp_rijndael_objdump.txt
	/afs/inf.ed.ac.uk/user/s20/s2011935/llvm_install/bin/llvm-objdump -d -M no-aliases dynamic_Zcmt_rijndael > Zcmt_rijndael_objdump.txt
	/afs/inf.ed.ac.uk/user/s20/s2011935/llvm_install/bin/llvm-objdump -d -M no-aliases dynamic_Zce_rijndael > Zce_rijndael_objdump.txt
rijndael: aes.c aes.h aestab.h aesxam.c Makefile
	/afs/inf.ed.ac.uk/user/s20/s2011935/llvm_install/bin/clang -Os -march=rv64ifd_zce -mabi=lp64d -msave-restore -o rijndael aes.c aesxam.c
	mv rijndael dynamic_Zce_rijndael
clean:
	rm -rf rijndael output*
