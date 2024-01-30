FILE = bitcnt_1.c bitcnt_2.c bitcnt_3.c bitcnt_4.c bitcnts.c bitfiles.c bitstrng.c bstr_i.c 

bitcnts: ${FILE} Makefile
	clang -static -Os -menable-experimental-extensions -march=rv64ifd_zca0p70_zcf0p70_zcd0p70 -mabi=lp64d -msave-restore ${FILE} -o bitcnts

clean:
	rm -rf bitcnts output*
