all:  dijkstra_large dijkstra_small

dijkstra_large: dijkstra_large.c Makefile
	/afs/inf.ed.ac.uk/user/s20/s2011935/llvm_install/bin/clang -Os  dijkstra_large.c -march=rv64ifd_zce -mabi=lp64d -msave-restore -o dijkstra_large
	mv dijkstra_large dymaic_Zce_dijkstra_large
dijkstra_small: dijkstra_small.c Makefile
	gcc -static dijkstra_small.c -O3 -o dijkstra_small 

clean:
	rm -rf dijkstra_large dijkstra_small output*
