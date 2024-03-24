import os
from pprint import pprint

def count_space_separated_strings(filepath: str) -> dict:
    counts = {}
    with open(filepath, 'r') as file:
        for line in file:
            strings = line.strip().split()
            for string in strings:
                if string in counts:
                    counts[string] += 1
                else:
                    counts[string] = 1
    return counts

def instr_counts_by_extension(counts: dict) -> dict:
    base = {'lui':0,
            'auipc':0,
            'jal':0,
            'jalr':0,
            'beq':0,
            'bne':0,
            'blt':0,
            'bge':0,
            'bltu':0,
            'bgeu':0,
            'lb':0,
            'lh':0,
            'lw':0,
            'lbu':0,
            'lhu':0,
            'sb':0,
            'sh':0,
            'sw':0,
            'addi':0,
            'slti':0,
            'sltiu':0,
            'xori':0,
            'ori':0,
            'andi':0,
            'slli':0,
            'srli':0,
            'srai':0,
            'add':0,
            'sub':0,
            'sll':0,
            'slt':0,
            'sltu':0,
            'xor':0,
            'srl':0,
            'sra':0,
            'or':0,
            'and':0,
            'fence':0,
            'ecall':0,
            'ebreak':0,
            'lwu':0,
            'ld':0,
            'sd':0,
            'addiw':0,
            'slliw':0,
            'srliw':0,
            'sraiw':0,
            'addw':0,
            'subw':0,
            'sllw':0,
            'srlw':0,
            'sraw':0,
            'fld':0,
            'flw':0,
            'fsw':0,
            'fsd':0,
            'fadd.s':0,
            'fsub.s':0,
            'fmul.s':0,
            'fdiv.s':0,
            'fsqrt.s':0,
            'fmadd.s':0,
            'fmadd.d':0,
            'fmsub.s':0,
            'fmsub.d':0,
            'fnmsub.s':0,
            'fnmsub.d':0,
            'fnmadd.s':0,
            'fnmadd.d':0,
            'fmin.s':0,
            'fmax.s':0,
            'fadd.d':0,
            'fsub.d':0,
            'fmul.d':0,
            'fdiv.d':0,
            'fsqrt.d':0,
            'fmin.d':0,
            'fmax.d':0,
            'feq.s':0,
            'flt.s':0,
            'fle.s':0,
            'feq.s':0,
            'flt.s':0,
            'fle.s':0,
            'feq.d':0,
            'flt.d':0,
            'fle.d':0,
            'fcvt.s.d':0,
            'fcvt.d.s':0,
            'fcvt.w.s':0,
            'fcvt.l.s':0,
            'fcvt.s.w':0,
            'fcvt.s.l':0,
            'fcvt.wu.s':0,
            'fcvt.lu.s':0,
            'fcvt.s.wu':0,
            'fcvt.s.lu':0,
            'fcvt.w.d':0,
            'fcvt.l.d':0,
            'fcvt.d.w':0,
            'fcvt.d.l':0,
            'fcvt.wu.d':0,
            'fcvt.lu.d':0,
            'fcvt.d.wu':0,
            'fcvt.d.lu':0,
            'fmv.x.w':0,
            'fmv.w.x':0,
            'fmv.x.d':0,
            'fmv.d.x':0,
            'fsgnj.s':0,
            'fsgnjn.s':0,
            'fsgnjx.s':0,
            'fsgnj.d':0,
            'fsgnjn.d':0,
            'fsgnjx.d':0,
            'fclass.s':0,
            'fclass.d':0}
    C_ext = {'c.addi4spn':0,
             'c.fld':0,
             'c.lw':0,
             'c.flw':0,
             'c.ld':0,
             'c.fsd':0,
             'c.sw':0,
             'c.fsw':0,
             'c.sd':0,
             'c.nop':0,
             'c.addi':0,
             'c.jal':0,
             'c.addiw':0,
             'c.li':0,
             'c.addi16sp':0,
             'c.lui':0,
             'c.srli':0,
             'c.srli64':0,
             'c.srai':0,
             'c.srai64':0,
             'c.andi':0,
             'c.sub':0,
             'c.xor':0,
             'c.or':0,
             'c.and':0,
             'c.subw':0,
             'c.addw':0,
             'c.j':0,
             'c.beqz':0,
             'c.bnez':0,
             'c.slli':0,
             'c.slli64':0,
             'c.fldsp':0,
             'c.lwsp':0,
             'c.flwsp':0,
             'c.ldsp':0,
             'c.jr':0,
             'c.mv':0,
             'c.ebreak':0,
             'c.jalr':0,
             'c.add':0,
             'c.fsdsp':0,
             'c.swsp':0,
             'c.fswsp':0,
             'c.sdsp':0}
    Zca_ext = {'c.addi4spn':0,
             'c.lw':0,
             'c.ld':0,
             'c.sw':0,
             'c.sd':0,
             'c.nop':0,
             'c.addi':0,
             'c.jal':0,
             'c.addiw':0,
             'c.li':0,
             'c.addi16sp':0,
             'c.lui':0,
             'c.srli':0,
             'c.srli64':0,
             'c.srai':0,
             'c.srai64':0,
             'c.andi':0,
             'c.sub':0,
             'c.xor':0,
             'c.or':0,
             'c.and':0,
             'c.subw':0,
             'c.addw':0,
             'c.j':0,
             'c.beqz':0,
             'c.bnez':0,
             'c.slli':0,
             'c.slli64':0,
             'c.lwsp':0,
             'c.ldsp':0,
             'c.jr':0,
             'c.mv':0,
             'c.ebreak':0,
             'c.jalr':0,
             'c.add':0,
             'c.swsp':0,
             'c.sdsp':0}
    Zcf_ext = {'c.flw':0,
               'c.flwsp':0,
               'c.fsw':0,
               'c.fswsp':0}
    Zcd_ext = {'c.fsd':0,
               'c.fsdsp':0,
               'c.fld':0,
               'c.fldsp':0}
    Zcb_ext = {'c.lbu':0,
               'c.lhu':0,
               'c.lh':0,
               'c.sb':0,
               'c.sh':0,
               'c.zext.b':0,
               'c.sext.b':0,
               'c.zext.h':0,
               'c.sext.h':0,
               'c.zext.w':0,
               'c.not':0,
               'c.mul':0}
    Zcmp_ext = {'cm.push':0,
                'cm.pop':0,
                'cm.popretz':0,
                'cm.popret':0,
                'cm.mvsa01':0,
                'cm.mva01s':0}
    Zcmt_ext = {'cm.jt':0,
                'cm.jalt':0}
    Zce_ext = {'c.addi4spn':0,
             'c.lw':0,
             'c.ld':0,
             'c.sw':0,
             'c.sd':0,
             'c.nop':0,
             'c.addi':0,
             'c.jal':0,
             'c.addiw':0,
             'c.li':0,
             'c.addi16sp':0,
             'c.lui':0,
             'c.srli':0,
             'c.srli64':0,
             'c.srai':0,
             'c.srai64':0,
             'c.andi':0,
             'c.sub':0,
             'c.xor':0,
             'c.or':0,
             'c.and':0,
             'c.subw':0,
             'c.addw':0,
             'c.j':0,
             'c.beqz':0,
             'c.bnez':0,
             'c.slli':0,
             'c.slli64':0,
             'c.lwsp':0,
             'c.ldsp':0,
             'c.jr':0,
             'c.mv':0,
             'c.ebreak':0,
             'c.jalr':0,
             'c.add':0,
             'c.swsp':0,
             'c.sdsp':0,
             'c.lbu':0,
            'c.lhu':0,
            'c.lh':0,
            'c.sb':0,
            'c.sh':0,
            'c.zext.b':0,
            'c.sext.b':0,
            'c.zext.h':0,
            'c.sext.h':0,
            'c.zext.w':0,
            'c.not':0,
            'c.mul':0,
            'cm.push':0,
            'cm.pop':0,
            'cm.popretz':0,
            'cm.popret':0,
            'cm.mvsa01':0,
            'cm.mva01s':0,
            'cm.jt':0,
            'cm.jalt':0}
    sorted_ext_instr_counts = {'base_instrs':base,'c_instrs':C_ext,'zca_instrs':Zca_ext,'zcf_instrs':Zcf_ext,'zcd_instrs':Zcd_ext,'zcb_instrs':Zcb_ext,'zcmp_instrs':Zcmp_ext,'zcmt_instrs':Zcmt_ext,'zce_instrs':Zce_ext}
    for entry in counts.keys():
        for ext in sorted_ext_instr_counts.values():
            if entry in ext:
                ext[entry] = counts[entry]
    return sorted_ext_instr_counts

def calculate_instr_CR_n_contribs(sorted_counts_base: dict, sorted_counts_ext: dict) -> float:
    for value in sorted_counts_base['c_instrs'].values():
        assert(value == 0,"unexpected compressed instructions in baseISA file")
    for value in sorted_counts_base['zce_instrs'].values():
        assert(value == 0,"unexpected compressed instructions in baseISA file")
    num_bytes_base = 0
    num_bytes_ext = 0
    contribs = {'zca':0,'zcf':0,'zcd':0,'zcb':0,'zcmp':0,'zcmt':0}
    for value in sorted_counts_base['base_instrs'].values():
        num_bytes_base += value*4
    for value in sorted_counts_ext['base_instrs'].values():
        num_bytes_ext += value*4
    for value in sorted_counts_ext['zca_instrs'].values():
        num_bytes_ext += value*2
        contribs['zca'] += value*2
    for value in sorted_counts_ext['zcf_instrs'].values():
        num_bytes_ext += value*2
        contribs['zcf'] += value*2
    for value in sorted_counts_ext['zcd_instrs'].values():
        num_bytes_ext += value*2
        contribs['zcd'] += value*2
    for value in sorted_counts_ext['zcb_instrs'].values():
        num_bytes_ext += value*2
        contribs['zcb'] += value*2
    for value in sorted_counts_ext['zcmp_instrs'].values():
        num_bytes_ext += value*2
        contribs['zcmp'] += value*2
    for value in sorted_counts_ext['zcmt_instrs'].values():
        print(value)
        num_bytes_ext += value*2
        contribs['zcmt'] += value*2
    cr = num_bytes_ext/num_bytes_base
    totalContribs = 0
    for key in contribs.keys():
        contribs[key] = contribs[key]*100/(num_bytes_base-num_bytes_ext)
        totalContribs += contribs[key]
    if contribs['zcmp'] > 0:
        contribs['zcmp'] += 100 - totalContribs
    return (cr,contribs)

def calculate_total_instrs(counts:dict):
    totals = {}
    for key in counts.keys():
        totals[key] = 0
        for instr in counts[key].keys():
            totals[key] += counts[key][instr]
    return totals

def counts_CRs(outfile: str):
    instr_counts = {'qsort':{},'rijndael':{},'dijkstra':{},'bitcount':{},'cjpeg':{},'djpeg':{},'stringsearch':{},'whetstone':{},'susan':{},'fft':{},'lame':{},'crc':{},'sha':{},'blowfish':{}}
    totals = {'qsort':{},'rijndael':{},'dijkstra':{},'bitcount':{},'cjpeg':{},'djpeg':{},'stringsearch':{},'whetstone':{},'susan':{},'fft':{},'lame':{},'crc':{},'sha':{},'blowfish':{}}
    CRs = {'qsort':{},'rijndael':{},'dijkstra':{},'bitcount':{},'cjpeg':{},'djpeg':{},'stringsearch':{},'whetstone':{},'susan':{},'fft':{},'lame':{},'crc':{},'sha':{},'blowfish':{}}
    objdumpdir = './stripped_objdumps/'
    for root, dirs, files in os.walk(objdumpdir):
        for dir in dirs:
            currdr = os.path.join(objdumpdir,dir)
            for rt, drs, fls in os.walk(currdr):
                fls = sorted(fls)
                base_counts = instr_counts_by_extension(count_space_separated_strings(os.path.join(rt,fls[0])))
                instr_counts[dir]['rv64ifd'] = base_counts
                totals[dir]['rv64ifd'] = calculate_total_instrs(base_counts)
                C_counts = instr_counts_by_extension(count_space_separated_strings(os.path.join(rt,fls[1])))
                instr_counts[dir]['rv64ifdc'] = C_counts
                totals[dir]['rv64ifdc'] = calculate_total_instrs(C_counts)
                CRs[dir]['rv64ifdc'] = calculate_instr_CR_n_contribs(base_counts,C_counts)
                Zca_counts = instr_counts_by_extension(count_space_separated_strings(os.path.join(rt,fls[2])))
                instr_counts[dir]['rv64ifd_zca'] = Zca_counts
                totals[dir]['rv64ifd_zca'] = calculate_total_instrs(Zca_counts)
                CRs[dir]['rv64ifd_zca'] = calculate_instr_CR_n_contribs(base_counts,Zca_counts)
                Zcb_counts = instr_counts_by_extension(count_space_separated_strings(os.path.join(rt,fls[3])))
                instr_counts[dir]['rv64ifd_zcb'] = Zcb_counts
                totals[dir]['rv64ifd_zcb'] = calculate_total_instrs(Zcb_counts)
                CRs[dir]['rv64ifd_zcb'] = calculate_instr_CR_n_contribs(base_counts,Zcb_counts)
                Zcd_counts = instr_counts_by_extension(count_space_separated_strings(os.path.join(rt,fls[4])))
                instr_counts[dir]['rv64ifd_zcd'] = Zcd_counts
                totals[dir]['rv64ifd_zcd'] = calculate_total_instrs(Zcd_counts)
                CRs[dir]['rv64ifd_zcd'] = calculate_instr_CR_n_contribs(base_counts,Zcd_counts)
                Zce_counts = instr_counts_by_extension(count_space_separated_strings(os.path.join(rt,fls[5])))
                instr_counts[dir]['rv64ifd_zce'] = Zce_counts
                totals[dir]['rv64ifd_zce'] = calculate_total_instrs(Zce_counts)
                CRs[dir]['rv64ifd_zce'] = calculate_instr_CR_n_contribs(base_counts,Zce_counts)
                Zcmp_counts = instr_counts_by_extension(count_space_separated_strings(os.path.join(rt,fls[6])))
                instr_counts[dir]['rv64ifd_zcmp'] = Zcmp_counts
                totals[dir]['rv64ifd_zcmp'] = calculate_total_instrs(Zcmp_counts)
                CRs[dir]['rv64ifd_zcmp'] = calculate_instr_CR_n_contribs(base_counts,Zcmp_counts)
                Zcmt_counts = instr_counts_by_extension(count_space_separated_strings(os.path.join(rt,fls[7])))
                instr_counts[dir]['rv64ifd_zcmt'] = Zcmt_counts
                totals[dir]['rv64ifd_zcmt'] = calculate_total_instrs(Zcmt_counts)
                CRs[dir]['rv64ifd_zcmt'] = calculate_instr_CR_n_contribs(base_counts,Zcmt_counts)
    print("Total instructions from each extension",file=outfile)
    print("---------------------------",file=outfile)
    pprint(totals, stream=outfile)
    print("---------------------------",file=outfile)
    print("Compression Ratios",file=outfile)                
    print("---------------------------",file=outfile)
    pprint(CRs, stream=outfile)
    print("---------------------------",file=outfile)
    print("Instruction Counts",file=outfile)
    print("---------------------------",file=outfile)
    pprint(instr_counts, stream=outfile)
    print("---------------------------",file=outfile)
    return (instr_counts, totals, CRs)

###TODO rewrite this function with contribs
def mean_CRs(CRsnContribs: dict, outfile):
    totalCRs = {'rv64ifdc':0,'rv64ifd_zca':0,'rv64ifd_zcd':0,'rv64ifd_zcb':0,'rv64ifd_zcmp':0,'rv64ifd_zcmt':0,'rv64ifd_zce':0,}
    totalContribs = {'rv64ifdc':{'zca':0,'zcf':0,'zcd':0,'zcb':0,'zcmp':0,'zcmt':0},
                      'rv64ifd_zca':{'zca':0,'zcf':0,'zcd':0,'zcb':0,'zcmp':0,'zcmt':0},
                      'rv64ifd_zcd':{'zca':0,'zcf':0,'zcd':0,'zcb':0,'zcmp':0,'zcmt':0},
                      'rv64ifd_zcb':{'zca':0,'zcf':0,'zcd':0,'zcb':0,'zcmp':0,'zcmt':0},
                      'rv64ifd_zcmp':{'zca':0,'zcf':0,'zcd':0,'zcb':0,'zcmp':0,'zcmt':0},
                      'rv64ifd_zcmt':{'zca':0,'zcf':0,'zcd':0,'zcb':0,'zcmp':0,'zcmt':0},
                      'rv64ifd_zce':{'zca':0,'zcf':0,'zcd':0,'zcb':0,'zcmp':0,'zcmt':0}}
    numComps = 14
    meanCRs = {'rv64ifdc':{},'rv64ifd_zca':0,'rv64ifd_zcd':0,'rv64ifd_zcb':0,'rv64ifd_zcmp':0,'rv64ifd_zcmt':0,'rv64ifd_zce':0,}
    meanContribs = {'rv64ifdc':{'zca':0,'zcf':0,'zcd':0,'zcb':0,'zcmp':0,'zcmt':0},
                      'rv64ifd_zca':{'zca':0,'zcf':0,'zcd':0,'zcb':0,'zcmp':0,'zcmt':0},
                      'rv64ifd_zcd':{'zca':0,'zcf':0,'zcd':0,'zcb':0,'zcmp':0,'zcmt':0},
                      'rv64ifd_zcb':{'zca':0,'zcf':0,'zcd':0,'zcb':0,'zcmp':0,'zcmt':0},
                      'rv64ifd_zcmp':{'zca':0,'zcf':0,'zcd':0,'zcb':0,'zcmp':0,'zcmt':0},
                      'rv64ifd_zcmt':{'zca':0,'zcf':0,'zcd':0,'zcb':0,'zcmp':0,'zcmt':0},
                      'rv64ifd_zce':{'zca':0,'zcf':0,'zcd':0,'zcb':0,'zcmp':0,'zcmt':0}}
    for bm in CRsnContribs.keys():
        for ext in totalCRs.keys():
            totalCRs[ext] += CRsnContribs[bm][ext][0]
            for contrib in CRsnContribs[bm][ext][1].keys():
                totalContribs[ext][contrib] += CRsnContribs[bm][ext][1][contrib]
    for ext in totalCRs.keys():
        meanCRs[ext] = totalCRs[ext] / numComps
        for contrib in CRsnContribs[bm][ext][1].keys():
            meanContribs[ext][contrib] = totalContribs[ext][contrib] / numComps
    keys = meanCRs.keys()
    values = zip(meanCRs.values(), meanContribs.values())
    meanPrint = dict(zip(keys, values))
    print(file=outfile)
    print("--------------------------------------------------------------",file=outfile)
    print("--------------------------------------------------------------",file=outfile)
    print("AVERAGE COMPRESSION RATIOS:",file=outfile)
    pprint(meanPrint, stream=outfile)
    print("--------------------------------------------------------------",file=outfile)
    print("--------------------------------------------------------------",file=outfile)
    return meanCRs

if __name__ == "__main__":
    with open('./stats.txt', 'w') as f:
        countsAndCRs = counts_CRs(f)
        print(countsAndCRs[2])
        meanCR = mean_CRs(countsAndCRs[2], f)
