rijndael: aes.c aes.h aestab.h aesxam.c Makefile
	/afs/inf.ed.ac.uk/user/s20/s2011935/llvm_install/bin/clang -Os -march=rv64ifd_zce -mabi=lp64d -msave-restore -o rijndael aes.c aesxam.c
	mv rijndael dynamic_Zce_rijndael
clean:
	rm -rf rijndael output*
