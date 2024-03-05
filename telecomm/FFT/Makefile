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
