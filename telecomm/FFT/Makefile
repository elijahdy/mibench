OBJ = main.o fftmisc.o  fourierf.o
FILE = main.c fftmisc.c  fourierf.c
CFLAGS = -static -march=rv64ifd -mabi=lp64d -msave-restore -menable-experimental-extensions -g

fft: ${OBJ} Makefile
	clang  ${CFLAGS} ${OBJ} -o fft -lm
fftmisc.o: fftmisc.c
	clang ${CFLAGS} -c fftmisc.c
fourierf.o: fourierf.c
	clang ${CFLAGS} -c fourierf.c
main.o: main.c
	clang ${CFLAGS} -c main.c

clean:
	rm -rf *.o fft output*
