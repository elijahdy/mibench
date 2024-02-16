rijndael: aes.c aes.h aestab.h aesxam.c Makefile
	clang -static -Os -march=rv64ifd_zca0p70_zcf0p70_zcd0p70 -mabi=lp64d -msave-restore -menable-experimental-extensions -o rijndael aes.c aesxam.c

clean:
	rm -rf rijndael output*
