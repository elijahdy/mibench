all:  dijkstra_large dijkstra_small

dijkstra_large: dijkstra_large.c Makefile
	clang -static -Os  dijkstra_large.c -march=rv64ifdc -mabi=lp64d -msave-restore -o dijkstra_large

dijkstra_small: dijkstra_small.c Makefile
	gcc -static dijkstra_small.c -O3 -o dijkstra_small 

clean:
	rm -rf dijkstra_large dijkstra_small output*
