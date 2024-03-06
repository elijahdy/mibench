patricia: patricia.c patricia_test.c
	/afs/inf.ed.ac.uk/user/s20/s2011935/llvm_install/bin/clang -Os -march=rv64ifd -mabi=lp64d -msave-restore patricia.c -o patricia
	mv patricia static_baseISA_patricia
clean:
	rm -rf patricia output*
