FILE = bitcnt_1.c bitcnt_2.c bitcnt_3.c bitcnt_4.c bitcnts.c bitfiles.c bitstrng.c bstr_i.c 

bitcnts: ${FILE} Makefile
	/afs/inf.ed.ac.uk/user/s20/s2011935/llvm_install/bin/clang -Os -static -march=rv64ifd -mabi=lp64d -msave-restore ${FILE} -o bitcnts
	mv bitcnts static_baseISA_bitcnts
clean:
	rm -rf bitcnts output*
