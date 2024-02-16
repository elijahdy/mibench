patricia: patricia.c patricia_test.c
	clang -static -Os -march=rv64ifd_zca0p70_zcf0p70_zcd0p70 -mabi=lp64d -menable-experimental-extensions patricia.c patricia_test.c -O3 -o patricia

clean:
	rm -rf patricia output*
