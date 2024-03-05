crc: crc_32.c Makefile
	/afs/inf.ed.ac.uk/user/s20/s2011935/llvm_install/bin/clang -static -Os -march=rv64ifd_zcmt -mabi=lp64d -msave-restore  crc_32.c -o crc 
	mv crc static_Zcmt_crc
clean:
	rm -rf crc output*
