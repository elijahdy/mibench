FILE = dymaic_baseISA_dijkstra_large dymaic_C_dijkstra_large dymaic_Zca_dijkstra_large dymaic_Zcb_dijkstra_large dymaic_Zcd_dijkstra_large dymaic_Zce_dijkstra_large dymaic_Zcmp_dijkstra_large dymaic_Zcmt_dijkstra_large
objdump: ${FILE} Makefile
	/afs/inf.ed.ac.uk/user/s20/s2011935/llvm_install/bin/llvm-objdump -d -M no-aliases dymaic_baseISA_dijkstra_large > base_dijkstra_large_objdump.txt
	/afs/inf.ed.ac.uk/user/s20/s2011935/llvm_install/bin/llvm-objdump -d -M no-aliases dymaic_C_dijkstra_large > C_dijkstra_large_objdump.txt
	/afs/inf.ed.ac.uk/user/s20/s2011935/llvm_install/bin/llvm-objdump -d -M no-aliases dymaic_Zca_dijkstra_large > Zca_dijkstra_large_objdump.txt
	/afs/inf.ed.ac.uk/user/s20/s2011935/llvm_install/bin/llvm-objdump -d -M no-aliases dymaic_Zcd_dijkstra_large > Zcd_dijkstra_large_objdump.txt
	/afs/inf.ed.ac.uk/user/s20/s2011935/llvm_install/bin/llvm-objdump -d -M no-aliases dymaic_Zcb_dijkstra_large > Zcb_dijkstra_large_objdump.txt
	/afs/inf.ed.ac.uk/user/s20/s2011935/llvm_install/bin/llvm-objdump -d -M no-aliases dymaic_Zcmp_dijkstra_large > Zcmp_dijkstra_large_objdump.txt
	/afs/inf.ed.ac.uk/user/s20/s2011935/llvm_install/bin/llvm-objdump -d -M no-aliases dymaic_Zcmt_dijkstra_large > Zcmt_dijkstra_large_objdump.txt
	/afs/inf.ed.ac.uk/user/s20/s2011935/llvm_install/bin/llvm-objdump -d -M no-aliases dymaic_Zce_dijkstra_large > Zce_dijkstra_large_objdump.txt

all:  dijkstra_large dijkstra_small

dijkstra_large: dijkstra_large.c Makefile
	/afs/inf.ed.ac.uk/user/s20/s2011935/llvm_install/bin/clang -Os  dijkstra_large.c -march=rv64ifd_zce -mabi=lp64d -msave-restore -o dijkstra_large
	mv dijkstra_large dymaic_Zce_dijkstra_large
dijkstra_small: dijkstra_small.c Makefile
	gcc -static dijkstra_small.c -O3 -o dijkstra_small 

clean:
	rm -rf dijkstra_large dijkstra_small output*
