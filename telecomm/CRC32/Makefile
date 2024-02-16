crc: crc_32.c Makefile
	clang -static -Os -march=rv64ifd_zca0p70_zcf0p70_zcd0p70 -mabi=lp64d -msave-restore -menable-experimental-extensions  crc_32.c -O3 -o crc 

clean:
	rm -rf crc output*
