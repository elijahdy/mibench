FILE = dynamic_baseISA_bf dynamic_C_bf dynamic_Zca_bf dynamic_Zcb_bf dynamic_Zcd_bf dynamic_Zce_bf dynamic_Zcmp_bf dynamic_Zcmt_bf
objdump: ${FILE} Makefile
	/afs/inf.ed.ac.uk/user/s20/s2011935/llvm_install/bin/llvm-objdump -d -M no-aliases dynamic_baseISA_bf > base_bf_objdump.txt
	/afs/inf.ed.ac.uk/user/s20/s2011935/llvm_install/bin/llvm-objdump -d -M no-aliases dynamic_C_bf > C_bf_objdump.txt
	/afs/inf.ed.ac.uk/user/s20/s2011935/llvm_install/bin/llvm-objdump -d -M no-aliases dynamic_Zca_bf > Zca_bf_objdump.txt
	/afs/inf.ed.ac.uk/user/s20/s2011935/llvm_install/bin/llvm-objdump -d -M no-aliases dynamic_Zcd_bf > Zcd_bf_objdump.txt
	/afs/inf.ed.ac.uk/user/s20/s2011935/llvm_install/bin/llvm-objdump -d -M no-aliases dynamic_Zcb_bf > Zcb_bf_objdump.txt
	/afs/inf.ed.ac.uk/user/s20/s2011935/llvm_install/bin/llvm-objdump -d -M no-aliases dynamic_Zcmp_bf > Zcmp_bf_objdump.txt
	/afs/inf.ed.ac.uk/user/s20/s2011935/llvm_install/bin/llvm-objdump -d -M no-aliases dynamic_Zcmt_bf > Zcmt_bf_objdump.txt
	/afs/inf.ed.ac.uk/user/s20/s2011935/llvm_install/bin/llvm-objdump -d -M no-aliases dynamic_Zce_bf > Zce_bf_objdump.txt
# Targets
# make          - twidle the options yourself :-)
# make cc       - standard cc options
# make gcc      - standard gcc options
# make x86-elf  - linux-elf etc
# make x86-out  - linux-a.out, FreeBSD etc
# make x86-solaris
# make x86-bdsi

# use BF_PTR2 for intel boxes,
# BF_PTR for sparc and MIPS/SGI
# use nothing for Alpha and HP.

# There are 3 possible performance options, experiment :-)
#OPTS= -d -M no-aliasesBF_PTR  # usr for sparc and MIPS/SGI
#OPTS= -d -M no-aliasesBF_PTR2 # use for pentium
OPTS=		 # use for pentium pro, Alpha and HP

MAKE=make -f Makefile
#CC=
#CFLAG= 

CC=/afs/inf.ed.ac.uk/user/s20/s2011935/llvm_install/bin/clang
CFLAG= -Os -march=rv64ifd_zce -mabi=lp64d -msave-restore -fomit-frame-pointer

CFLAGS=$(OPTS) $(CFLAG)
CPP=$(CC) -E
AS=as

# Assember version of bf_encrypt().
BF_ENC=bf_enc.o		# normal C version
#BF_ENC=asm/bx86-elf.o	# elf format x86
#BF_ENC=asm/bx86-out.o	# a.out format x86
#BF_ENC=asm/bx86-sol.o	# solaris format x86 
#BF_ENC=asm/bx86bsdi.o	# bsdi format x86 

LIBDIR=/usr/local/lib
BINDIR=/usr/local/bin
INCDIR=/usr/local/include
MANDIR=/usr/local/man
MAN1=1
MAN3=3
SHELL=/bin/sh
LIBOBJ=bf_skey.o bf_ecb.o $(BF_ENC) bf_cbc.o bf_cfb64.o bf_ofb64.o
LIBSRC=bf_skey.c bf_ecb.c bf_enc.c bf_cbc.c bf_cfb64.c bf_ofb64.c

GENERAL=Makefile Makefile.ssl Makefile.uni asm bf_locl.org README \
	COPYRIGHT INSTALL blowfish.doc

TESTING=    bftest bfspeed bf
TESTING_SRC=bftest.c bfspeed.c bf.c
HEADERS=bf_locl.h blowfish.h bf_pi.hbaseISA

ALL=	$(GENERAL) $(TESTING_SRC) $(LIBSRC) $(HEADERS)

BLIB=	libblowfish.a

all: $(BLIB) $(TESTING)

cc:
	$(MAKE) CC=cc CFLAGS="-O $(OPTS) $(CFLAG)" all

gcc:
	$(MAKE) CC=gcc CFLAGS="-O3 -fomit-frame-pointer $(OPTS) $(CFLAG)" all

x86-elf:
	$(MAKE) BF_ENC='asm/bx86-elf.o' CC=$(CC) CFLAGS="-d -M no-aliasesELF $(OPTS) $(CFLAG)" all

x86-out:
	$(MAKE) BF_ENC='asm/bx86-out.o' CC=$(CC) CFLAGS="-d -M no-aliasesOUT $(OPTS) $(CFLAG)" all

x86-solaris:
	$(MAKE) BF_ENC='asm/bx86-sol.o' CC=$(CC) CFLAGS="-d -M no-aliasesSOL $(OPTS) $(CFLAG)" all

x86-bsdi:
	$(MAKE) BF_ENC='asm/bx86bsdi.o' CC=$(CC) CFLAGS="-d -M no-aliasesBSDI $(OPTS) $(CFLAG)" all

# elf
asm/bx86-elf.o: asm/bx86-cpp.s asm/bx86unix.cpp
	$(CPP) -d -M no-aliasesELF asm/bx86unix.cpp | $(AS) -o asm/bx86-elf.o

# solaris
asm/bx86-sol.o: asm/bx86-cpp.s asm/bx86unix.cpp
	$(CC) -E -d -M no-aliasesSOL asm/bx86unix.cpp | sed 's/^#.*//' > asm/bx86-sol.s
	as -o asm/bx86-sol.o asm/bx86-sol.s
	rm -f asm/bx86-sol.s

# a.out
asm/bx86-out.o: asm/bx86-cpp.s asm/bx86unix.cpp
	$(CPP) -d -M no-aliasesOUT asm/bx86unix.cpp | $(AS) -o asm/bx86-out.o

# bsdi
asm/bx86bsdi.o: asm/bx86-cpp.s asm/bx86unix.cpp
	$(CPP) -d -M no-aliasesBSDI asm/bx86unix.cpp | $(AS) -o asm/bx86bsdi.o

test:	all
	./bftest

$(BLIB): $(LIBOBJ)
	/bin/rm -f $(BLIB)
	ar cr $(BLIB) $(LIBOBJ)
	-if test -s ranlib; then ssbig-na-sstrix-ranlib $(BLIB); \
	else if test -s ranlib; then ssbig-na-sstrix-ranlib $(BLIB); \
	else exit 0; fi; fibaseISA

bf: bf.o $(BLIB)
	$(CC) $(CFLAGS) -o bf bf.o $(BLIB)
	mv bf dynamic_Zce_bf

bftest: bftest.o $(BLIB)
	$(CC) $(CFLAGS) -o bftest bftest.o $(BLIB)

bfspeed: bfspeed.o $(BLIB)
	$(CC) $(CFLAGS) -o bfspeed bfspeed.o $(BLIB)

tags:
	ctags $(TESTING_SRC) $(LIBBF)

tar:
	tar chf libbf.tar $(ALL)

shar:
	shar $(ALL) >libbf.shar

depend:
	makedepend $(LIBBF) $(TESTING_SRC)

clean:
	/bin/rm -f *.o tags core $(TESTING) $(BLIB) .nfs* *.old *.bak asm/*.o output*

dclean:
	sed -e '/^# DO NOT DELETE THIS LINE/ q' Makefile >Makefile.new
	mv -f Makefile.new Makefile

# Eric is probably going to choke when he next looks at this --tjh
install: $(BLIB)
	if test $(INSTALLTOP); then \
	    echo SSL style install; \
	    cp $(BLIB) $(INSTALLTOP)/lib; \
	    if test -s /bin/ranlib; then \
	        /bin/ranlib $(INSTALLTOP)/lib/$(BLIB); \
	    else \
		if test -s /usr/bin/ranlib; then \
		/usr/bin/ranlib $(INSTALLTOP)/lib/$(BLIB); \
	    fi; fi; \
	    chmod 644 $(INSTALLTOP)/lib/$(BLIB); \
	    cp blowfish.h $(INSTALLTOP)/include; \
	    chmod 644 $(INSTALLTOP)/include/blowfish.h; \
	else \
	    echo Standalone install; \
	    cp $(BLIB) $(LIBDIR)/$(BLIB); \
	    if test -s /bin/ranlib; then \
	      /bin/ranlib $(LIBDIR)/$(BLIB); \
	    else \
	      if test -s /usr/bin/ranlib; then \
		/usr/bin/ranlib $(LIBDIR)/$(BLIB); \
	      fi; \
	    fi; \
	    chmod 644 $(LIBDIR)/$(BLIB); \
	    cp blowfish.h $(INCDIR)/blowfish.h; \
	    chmod 644 $(INCDIR)/blowfish.h; \
	fi
# DO NOT DELETE THIS LINE -- make depend depends on it.
