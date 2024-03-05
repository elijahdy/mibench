susan: susan.c Makefile
	/afs/inf.ed.ac.uk/user/s20/s2011935/llvm_install/bin/clang -Os -march=rv64ifd_zce -mabi=lp64d -msave-restore -o susan susan.c -lm 
	mv susan dynamic_Zce_susan
clean:
	rm -rf susan output*
