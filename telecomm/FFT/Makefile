FILE1 = dynamic_baseISA_fft dynamic_C_fft dynamic_Zca_fft dynamic_Zcb_fft dynamic_Zcd_fft dynamic_Zce_fft dynamic_Zcmp_fft dynamic_Zcmt_fft
objdump: ${FILE1} Makefile
	/afs/inf.ed.ac.uk/user/s20/s2011935/llvm_install/bin/llvm-objdump -d dynamic_baseISA_fft > base_fft_objdump.txt
	/afs/inf.ed.ac.uk/user/s20/s2011935/llvm_install/bin/llvm-objdump -d dynamic_C_fft > C_fft_objdump.txt
	/afs/inf.ed.ac.uk/user/s20/s2011935/llvm_install/bin/llvm-objdump -d dynamic_Zca_fft > Zca_fft_objdump.txt
	/afs/inf.ed.ac.uk/user/s20/s2011935/llvm_install/bin/llvm-objdump -d dynamic_Zcd_fft > Zcd_fft_objdump.txt
	/afs/inf.ed.ac.uk/user/s20/s2011935/llvm_install/bin/llvm-objdump -d dynamic_Zcb_fft > Zcb_fft_objdump.txt
	/afs/inf.ed.ac.uk/user/s20/s2011935/llvm_install/bin/llvm-objdump -d dynamic_Zcmp_fft > Zcmp_fft_objdump.txt
	/afs/inf.ed.ac.uk/user/s20/s2011935/llvm_install/bin/llvm-objdump -d dynamic_Zcmt_fft > Zcmt_fft_objdump.txt
	/afs/inf.ed.ac.uk/user/s20/s2011935/llvm_install/bin/llvm-objdump -d dynamic_Zce_fft > Zce_fft_objdump.txt

OBJ = main.o fftmisc.o  fourierf.o
FILE = main.c fftmisc.c  fourierf.c
CFLAGS = -Os -march=rv64ifd_zce -mabi=lp64d -msave-restore -g

fft: ${OBJ} Makefile
	/afs/inf.ed.ac.uk/user/s20/s2011935/llvm_install/bin/clang  ${CFLAGS} ${OBJ} -o fft -lm
	mv fft dynamic_Zce_fft
fftmisc.o: fftmisc.c
	/afs/inf.ed.ac.uk/user/s20/s2011935/llvm_install/bin/clang ${CFLAGS} -c fftmisc.c
fourierf.o: fourierf.c
	/afs/inf.ed.ac.uk/user/s20/s2011935/llvm_install/bin/clang ${CFLAGS} -c fourierf.c
main.o: main.c
	/afs/inf.ed.ac.uk/user/s20/s2011935/llvm_install/bin/clang ${CFLAGS} -c main.c

clean:
	rm -rf *.o fft output*
