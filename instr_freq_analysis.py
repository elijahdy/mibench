import os
from pprint import pprint
import matplotlib.pyplot as plt
import seaborn as sns

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
            'fclass.d':0,
            'nop':0}
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

def CR_n_contribs(sorted_counts_base: dict, sorted_counts_ext: dict) -> float:
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
        num_bytes_ext += value*2
        contribs['zcmt'] += value*2
    cr = num_bytes_ext/num_bytes_base
    totalContribs = 0
    for key in contribs.keys():
        contribs[key] = contribs[key]/num_bytes_base
        totalContribs += contribs[key]
    if contribs['zcmp'] > 0:
        contribs['zcmp'] += 1 - cr - totalContribs
    return (cr,contribs)

def instr_counts_by_category(counts: dict) -> dict:
    base_int_comp = {'lui':0,
            'auipc':0,
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
            'addiw':0,
            'slliw':0,
            'srliw':0,
            'sraiw':0,
            'addw':0,
            'subw':0,
            'sllw':0,
            'srlw':0,
            'sraw':0}
    zca_int_comp = {'c.addi4spn':0,
                    'c.addi':0,
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
                    'c.slli':0,
                    'c.slli64':0,
                    'c.add':0}
    zcb_int_comp = {'c.zext.b':0,
                    'c.sext.b':0,
                    'c.zext.h':0,
                    'c.sext.h':0,
                    'c.zext.w':0,
                    'c.not':0,
                    'c.mul':0}
    base_fp_comp = {'fadd.s':0,
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
    base_cond_CT = {'beq':0,
                'bne':0,
                'blt':0,
                'bge':0,
                'bltu':0,
                'bgeu':0}
    zca_cond_CT = {'c.beqz':0,
                    'c.bnez':0}
    base_uncond_CT = {'jal':0,
                    'jalr':0}
    zca_uncond_CT = {'c.jal':0,
                     'c.jalr':0,
                     'c.jr':0,
                     'c.j':0}
    zcmt_uncond_CT = {'cm.jt':0,
                     'cm.jalt':0}
    base_int_ld_st = {'lb':0,
                    'lh':0,
                    'lw':0,
                    'lbu':0,
                    'lhu':0,
                    'sb':0,
                    'sh':0,
                    'sw':0,
                    'lwu':0,
                    'ld':0,
                    'sd':0}
    zca_int_ld_st = {'c.lw':0,
                    'c.ld':0,
                    'c.sw':0,
                    'c.sd':0,
                    'c.lwsp':0,
                    'c.ldsp':0,
                    'c.swsp':0,
                    'c.sdsp':0}
    zcb_int_ld_st = {'c.lbu':0,
                    'c.lhu':0,
                    'c.lh':0,
                    'c.sb':0,
                    'c.sh':0}
    base_fp_ld_st = {'fld':0,
                    'flw':0,
                    'fsw':0,
                    'fsd':0}
    zcf_fp_ld_st = {'c.flw':0,
               'c.flwsp':0,
               'c.fsw':0,
               'c.fswsp':0}
    zcd_fp_ld_st = {'c.fsd':0,
               'c.fsdsp':0,
               'c.fld':0,
               'c.fldsp':0}
    instr_counts_by_category = {'base_int_comp':base_int_comp,'zca_int_comp':zca_int_comp,'zcb_int_comp':zcb_int_comp,
                            'base_fp_comp':base_fp_comp,'base_cond_CT':base_cond_CT,'zca_cond_CT':zca_cond_CT,'base_uncond_CT':base_uncond_CT,
                            'zca_uncond_CT':zca_uncond_CT,'zcmt_uncond_CT':zcmt_uncond_CT,'base_int_ld_st':base_int_ld_st,'zca_int_ld_st':zca_int_ld_st,
                            'zcb_int_ld_st':zcb_int_ld_st,'base_fp_ld_st':base_fp_ld_st,'zcf_fp_ld_st':zcf_fp_ld_st,'zcd_fp_ld_st':zcd_fp_ld_st}
    for entry in counts.keys():
        for ext in instr_counts_by_category.values():
            if entry in ext:
                ext[entry] = counts[entry]
    return instr_counts_by_category

def category_CRs_n_contribs(sorted_counts_base: dict, sorted_counts_ext: dict) -> dict:
    num_bytes_base = {'int_comp':0,'fp_comp':0,'cond_CT':0,'uncond_CT':0,'int_ld_st':0,'fp_ld_st':0}
    num_bytes_ext = {'int_comp':0,'fp_comp':0,'cond_CT':0,'uncond_CT':0,'int_ld_st':0,'fp_ld_st':0}
    CRs = {'int_comp':0,'cond_CT':0,'uncond_CT':0,'int_ld_st':0,'fp_ld_st':0}
    for value in sorted_counts_base['base_int_comp'].values():
        num_bytes_base['int_comp'] += value*4
    for value in sorted_counts_base['base_fp_comp'].values():
        num_bytes_base['fp_comp'] += value*4
    for value in sorted_counts_base['base_cond_CT'].values():
        num_bytes_base['cond_CT'] += value*4
    for value in sorted_counts_base['base_uncond_CT'].values():
        num_bytes_base['uncond_CT'] += value*4
    for value in sorted_counts_base['base_int_ld_st'].values():
        num_bytes_base['int_ld_st'] += value*4
    for value in sorted_counts_base['base_fp_ld_st'].values():
        num_bytes_base['fp_ld_st'] += value*4
    for value in sorted_counts_ext['base_int_comp'].values():
        num_bytes_ext['int_comp'] += value*4
    for value in sorted_counts_ext['base_fp_comp'].values():
        num_bytes_ext['fp_comp'] += value*4
    for value in sorted_counts_ext['base_cond_CT'].values():
        num_bytes_ext['cond_CT'] += value*4
    for value in sorted_counts_ext['base_uncond_CT'].values():
        num_bytes_ext['uncond_CT'] += value*4
    for value in sorted_counts_ext['base_int_ld_st'].values():
        num_bytes_ext['int_ld_st'] += value*4
    for value in sorted_counts_ext['base_fp_ld_st'].values():
        num_bytes_ext['fp_ld_st'] += value*4
    for value in sorted_counts_ext['zca_int_comp'].values():
        num_bytes_ext['int_comp'] += value*2
    for value in sorted_counts_ext['zcb_int_comp'].values():
        num_bytes_ext['int_comp'] += value*2
    for value in sorted_counts_ext['zca_cond_CT'].values():
        num_bytes_ext['cond_CT'] += value*2
    for value in sorted_counts_ext['zca_uncond_CT'].values():
        num_bytes_ext['uncond_CT'] += value*2
    for value in sorted_counts_ext['zcmt_uncond_CT'].values():
        num_bytes_ext['uncond_CT'] += value*2
    for value in sorted_counts_ext['zca_int_ld_st'].values():
        num_bytes_ext['int_ld_st'] += value*2
    for value in sorted_counts_ext['zcb_int_ld_st'].values():
        num_bytes_ext['int_ld_st'] += value*2
    for value in sorted_counts_ext['zcf_fp_ld_st'].values():
        num_bytes_ext['fp_ld_st'] += value*2
    for value in sorted_counts_ext['zcd_fp_ld_st'].values():
        num_bytes_ext['fp_ld_st'] += value*2
    for key in CRs.keys():
        if num_bytes_base[key] > 0:
            CRs[key] = num_bytes_ext[key] / num_bytes_base[key]
        else:
            CRs[key] = 'NA'
    return CRs

def calculate_total_instrs(counts:dict):
    totals = {}
    for key in counts.keys():
        totals[key] = 0
        for instr in counts[key].keys():
            totals[key] += counts[key][instr]
    return totals

def all_individual_file_stats(outfile: str):
    instr_counts = {'basicmath':{},'qsort':{},'rijndael':{},'dijkstra':{},'bitcount':{},'cjpeg':{},'djpeg':{},'stringsearch':{},'whetstone':{},'susan':{},'fft':{},'lame':{},'crc':{},'sha':{},'blowfish':{}}
    totals = {'basicmath':{},'qsort':{},'rijndael':{},'dijkstra':{},'bitcount':{},'cjpeg':{},'djpeg':{},'stringsearch':{},'whetstone':{},'susan':{},'fft':{},'lame':{},'crc':{},'sha':{},'blowfish':{}}
    CRs = {'basicmath':{},'qsort':{},'rijndael':{},'dijkstra':{},'bitcount':{},'cjpeg':{},'djpeg':{},'stringsearch':{},'whetstone':{},'susan':{},'fft':{},'lame':{},'crc':{},'sha':{},'blowfish':{}}
    category_CRs = {'basicmath':{},'qsort':{},'rijndael':{},'dijkstra':{},'bitcount':{},'cjpeg':{},'djpeg':{},'stringsearch':{},'whetstone':{},'susan':{},'fft':{},'lame':{},'crc':{},'sha':{},'blowfish':{}}
    categories = ['int_comp','fp_comp','cond_CT','uncond_CT','int_ld_st','fp_ld_st']
    objdumpdir = './stripped_objdumps/'
    for root, dirs, files in os.walk(objdumpdir):
        for dir in dirs:
            currdr = os.path.join(objdumpdir,dir)
            for rt, drs, fls in os.walk(currdr):
                fls = sorted(fls)
                base_counts = instr_counts_by_extension(count_space_separated_strings(os.path.join(rt,fls[0])))
                base_counts_by_category = instr_counts_by_category(count_space_separated_strings(os.path.join(rt,fls[0])))
                instr_counts[dir]['rv64ifd'] = base_counts
                totals[dir]['rv64ifd'] = calculate_total_instrs(base_counts)
                C_counts = instr_counts_by_extension(count_space_separated_strings(os.path.join(rt,fls[1])))
                C_counts_by_category = instr_counts_by_category(count_space_separated_strings(os.path.join(rt,fls[1])))
                instr_counts[dir]['rv64ifdc'] = C_counts
                totals[dir]['rv64ifdc'] = calculate_total_instrs(C_counts)
                CRs[dir]['rv64ifdc'] = CR_n_contribs(base_counts,C_counts)
                category_CRs[dir]['rv64ifdc'] = category_CRs_n_contribs(base_counts_by_category,C_counts_by_category)
                Zca_counts = instr_counts_by_extension(count_space_separated_strings(os.path.join(rt,fls[2])))
                Zca_counts_by_category = instr_counts_by_category(count_space_separated_strings(os.path.join(rt,fls[2])))
                instr_counts[dir]['rv64ifd_zca'] = Zca_counts
                totals[dir]['rv64ifd_zca'] = calculate_total_instrs(Zca_counts)
                CRs[dir]['rv64ifd_zca'] = CR_n_contribs(base_counts,Zca_counts)
                category_CRs[dir]['rv64ifd_zca'] = category_CRs_n_contribs(base_counts_by_category,Zca_counts_by_category)
                Zcb_counts = instr_counts_by_extension(count_space_separated_strings(os.path.join(rt,fls[3])))
                Zcb_counts_by_category = instr_counts_by_category(count_space_separated_strings(os.path.join(rt,fls[3])))
                instr_counts[dir]['rv64ifd_zcb'] = Zcb_counts
                totals[dir]['rv64ifd_zcb'] = calculate_total_instrs(Zcb_counts)
                CRs[dir]['rv64ifd_zcb'] = CR_n_contribs(base_counts,Zcb_counts)
                category_CRs[dir]['rv64ifd_zcb'] = category_CRs_n_contribs(base_counts_by_category,Zcb_counts_by_category)
                Zcd_counts = instr_counts_by_extension(count_space_separated_strings(os.path.join(rt,fls[4])))
                Zcd_counts_by_category = instr_counts_by_category(count_space_separated_strings(os.path.join(rt,fls[4])))
                instr_counts[dir]['rv64ifd_zcd'] = Zcd_counts
                totals[dir]['rv64ifd_zcd'] = calculate_total_instrs(Zcd_counts)
                CRs[dir]['rv64ifd_zcd'] = CR_n_contribs(base_counts,Zcd_counts)
                category_CRs[dir]['rv64ifd_zcd'] = category_CRs_n_contribs(base_counts_by_category,Zcd_counts_by_category)
                Zce_counts = instr_counts_by_extension(count_space_separated_strings(os.path.join(rt,fls[5])))
                Zce_counts_by_category = instr_counts_by_category(count_space_separated_strings(os.path.join(rt,fls[5])))
                instr_counts[dir]['rv64ifd_zce'] = Zce_counts
                totals[dir]['rv64ifd_zce'] = calculate_total_instrs(Zce_counts)
                CRs[dir]['rv64ifd_zce'] = CR_n_contribs(base_counts,Zce_counts)
                category_CRs[dir]['rv64ifd_zce'] = category_CRs_n_contribs(base_counts_by_category,Zce_counts_by_category)
                Zcmp_counts = instr_counts_by_extension(count_space_separated_strings(os.path.join(rt,fls[6])))
                Zcmp_counts_by_category = instr_counts_by_category(count_space_separated_strings(os.path.join(rt,fls[6])))
                instr_counts[dir]['rv64ifd_zcmp'] = Zcmp_counts
                totals[dir]['rv64ifd_zcmp'] = calculate_total_instrs(Zcmp_counts)
                CRs[dir]['rv64ifd_zcmp'] = CR_n_contribs(base_counts,Zcmp_counts)
                category_CRs[dir]['rv64ifd_zcmp'] = category_CRs_n_contribs(base_counts_by_category,Zcmp_counts_by_category)
                Zcmt_counts = instr_counts_by_extension(count_space_separated_strings(os.path.join(rt,fls[7])))
                Zcmt_counts_by_category = instr_counts_by_category(count_space_separated_strings(os.path.join(rt,fls[7])))
                instr_counts[dir]['rv64ifd_zcmt'] = Zcmt_counts
                totals[dir]['rv64ifd_zcmt'] = calculate_total_instrs(Zcmt_counts)
                CRs[dir]['rv64ifd_zcmt'] = CR_n_contribs(base_counts,Zcmt_counts)
                category_CRs[dir]['rv64ifd_zcmt'] = category_CRs_n_contribs(base_counts_by_category,Zcmt_counts_by_category)
    print("Total instructions from each extension",file=outfile)
    print("---------------------------",file=outfile)
    pprint(totals, stream=outfile)
    print("---------------------------",file=outfile)
    print(file=outfile)
    print("Instruction Counts",file=outfile)
    print("---------------------------",file=outfile)
    pprint(instr_counts, stream=outfile)
    print("---------------------------",file=outfile)
    print(file=outfile)
    print("Compression Ratios",file=outfile)                
    print("---------------------------",file=outfile)
    pprint(CRs, stream=outfile)
    print("---------------------------",file=outfile)
    print(file=outfile)
    print("Category Compression Ratios",file=outfile)                
    print("---------------------------",file=outfile)
    pprint(category_CRs, stream=outfile)
    print("---------------------------",file=outfile)
    return (instr_counts, totals, CRs, category_CRs)

def mean_CRs(CRsnContribs: dict, outfile):
    totalCRs = {'rv64ifdc':0,'rv64ifd_zca':0,'rv64ifd_zcd':0,'rv64ifd_zcb':0,'rv64ifd_zcmp':0,'rv64ifd_zcmt':0,'rv64ifd_zce':0,}
    totalContribs = {'rv64ifdc':{'zca':0,'zcf':0,'zcd':0,'zcb':0,'zcmp':0,'zcmt':0},
                      'rv64ifd_zca':{'zca':0,'zcf':0,'zcd':0,'zcb':0,'zcmp':0,'zcmt':0},
                      'rv64ifd_zcd':{'zca':0,'zcf':0,'zcd':0,'zcb':0,'zcmp':0,'zcmt':0},
                      'rv64ifd_zcb':{'zca':0,'zcf':0,'zcd':0,'zcb':0,'zcmp':0,'zcmt':0},
                      'rv64ifd_zcmp':{'zca':0,'zcf':0,'zcd':0,'zcb':0,'zcmp':0,'zcmt':0},
                      'rv64ifd_zcmt':{'zca':0,'zcf':0,'zcd':0,'zcb':0,'zcmp':0,'zcmt':0},
                      'rv64ifd_zce':{'zca':0,'zcf':0,'zcd':0,'zcb':0,'zcmp':0,'zcmt':0}}
    numComps = 15
    meanCRs = {'rv64ifdc':0,'rv64ifd_zca':0,'rv64ifd_zcd':0,'rv64ifd_zcb':0,'rv64ifd_zcmp':0,'rv64ifd_zcmt':0,'rv64ifd_zce':0,}
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
    meanCRs = dict(zip(keys, values))
    print(file=outfile)
    print("--------------------------------------------------------------",file=outfile)
    print("--------------------------------------------------------------",file=outfile)
    print("AVERAGE COMPRESSION RATIOS OVER ALL BENCHMARKS:",file=outfile)
    pprint(meanCRs, stream=outfile)
    print("--------------------------------------------------------------",file=outfile)
    print("--------------------------------------------------------------",file=outfile)
    return meanCRs

#probably easiest to do this when the benchmarks have been grouped by type in someway
def meanCRsByApplication(CRsnContribs: dict, outfile):
    totalCRsByAppType = {'automotive':{},'consumer':{},'office':{},'network':{},'security':{},'telecomm':{},'FP':{}}
    meanCrsByAppType = {'automotive':{},'consumer':{},'office':{},'network':{},'security':{},'telecomm':{},'FP':{}}
    totalContribsByAppType = {'automotive':{},'consumer':{},'office':{},'network':{},'security':{},'telecomm':{},'FP':{}}
    meanContribsByAppType = {'automotive':{},'consumer':{},'office':{},'network':{},'security':{},'telecomm':{},'FP':{}}
    numComps = {'automotive':4,'consumer':3,'office':1,'network':1,'security':3,'telecomm':2,'FP':1}
    for key in totalCRsByAppType.keys():
        totalCRsByAppType[key] = {'rv64ifdc':0,'rv64ifd_zca':0,'rv64ifd_zcd':0,'rv64ifd_zcb':0,'rv64ifd_zcmp':0,'rv64ifd_zcmt':0,'rv64ifd_zce':0,}
        meanCrsByAppType[key] = {'rv64ifdc':0,'rv64ifd_zca':0,'rv64ifd_zcd':0,'rv64ifd_zcb':0,'rv64ifd_zcmp':0,'rv64ifd_zcmt':0,'rv64ifd_zce':0,}
        totalContribsByAppType[key] = {'rv64ifdc':{'zca':0,'zcf':0,'zcd':0,'zcb':0,'zcmp':0,'zcmt':0},
                        'rv64ifd_zca':{'zca':0,'zcf':0,'zcd':0,'zcb':0,'zcmp':0,'zcmt':0},
                        'rv64ifd_zcd':{'zca':0,'zcf':0,'zcd':0,'zcb':0,'zcmp':0,'zcmt':0},
                        'rv64ifd_zcb':{'zca':0,'zcf':0,'zcd':0,'zcb':0,'zcmp':0,'zcmt':0},
                        'rv64ifd_zcmp':{'zca':0,'zcf':0,'zcd':0,'zcb':0,'zcmp':0,'zcmt':0},
                        'rv64ifd_zcmt':{'zca':0,'zcf':0,'zcd':0,'zcb':0,'zcmp':0,'zcmt':0},
                        'rv64ifd_zce':{'zca':0,'zcf':0,'zcd':0,'zcb':0,'zcmp':0,'zcmt':0}}
        meanContribsByAppType[key] = {'rv64ifdc':{'zca':0,'zcf':0,'zcd':0,'zcb':0,'zcmp':0,'zcmt':0},
                        'rv64ifd_zca':{'zca':0,'zcf':0,'zcd':0,'zcb':0,'zcmp':0,'zcmt':0},
                        'rv64ifd_zcd':{'zca':0,'zcf':0,'zcd':0,'zcb':0,'zcmp':0,'zcmt':0},
                        'rv64ifd_zcb':{'zca':0,'zcf':0,'zcd':0,'zcb':0,'zcmp':0,'zcmt':0},
                        'rv64ifd_zcmp':{'zca':0,'zcf':0,'zcd':0,'zcb':0,'zcmp':0,'zcmt':0},
                        'rv64ifd_zcmt':{'zca':0,'zcf':0,'zcd':0,'zcb':0,'zcmp':0,'zcmt':0},
                        'rv64ifd_zce':{'zca':0,'zcf':0,'zcd':0,'zcb':0,'zcmp':0,'zcmt':0}}
    for bm in ['basicmath','bitcount','qsort','susan']:
        for ext in totalCRsByAppType['automotive'].keys():
            totalCRsByAppType['automotive'][ext] += CRsnContribs[bm][ext][0]
            for contrib in CRsnContribs[bm][ext][1].keys():
                totalContribsByAppType['automotive'][ext][contrib] += CRsnContribs[bm][ext][1][contrib]
    for bm in ['cjpeg','djpeg','lame']:
        for ext in totalCRsByAppType['consumer'].keys():
            totalCRsByAppType['consumer'][ext] += CRsnContribs[bm][ext][0]
            for contrib in CRsnContribs[bm][ext][1].keys():
                totalContribsByAppType['consumer'][ext][contrib] += CRsnContribs[bm][ext][1][contrib]
    for bm in ['blowfish','rijndael','sha']:
        for ext in totalCRsByAppType['security'].keys():
            totalCRsByAppType['security'][ext] += CRsnContribs[bm][ext][0]
            for contrib in CRsnContribs[bm][ext][1].keys():
                totalContribsByAppType['security'][ext][contrib] += CRsnContribs[bm][ext][1][contrib]
    for bm in ['crc','fft']:
        for ext in totalCRsByAppType['telecomm'].keys():
            totalCRsByAppType['telecomm'][ext] += CRsnContribs[bm][ext][0]
            for contrib in CRsnContribs[bm][ext][1].keys():
                totalContribsByAppType['telecomm'][ext][contrib] += CRsnContribs[bm][ext][1][contrib]
    for ext in totalCRsByAppType['office'].keys():
        totalCRsByAppType['office'][ext] += CRsnContribs['stringsearch'][ext][0]
        for contrib in CRsnContribs['stringsearch'][ext][1].keys():
            totalContribsByAppType['office'][ext][contrib] += CRsnContribs['stringsearch'][ext][1][contrib]
    for ext in totalCRsByAppType['network'].keys():
        totalCRsByAppType['network'][ext] += CRsnContribs['dijkstra'][ext][0]
        for contrib in CRsnContribs['dijkstra'][ext][1].keys():
            totalContribsByAppType['network'][ext][contrib] += CRsnContribs['dijkstra'][ext][1][contrib]
    for ext in totalCRsByAppType['FP'].keys():
        totalCRsByAppType['FP'][ext] += CRsnContribs['whetstone'][ext][0]
        for contrib in CRsnContribs['whetstone'][ext][1].keys():
            totalContribsByAppType['FP'][ext][contrib] += CRsnContribs['whetstone'][ext][1][contrib]
    for key in meanContribsByAppType.keys():
        for ext in meanCrsByAppType[key].keys():
            meanCrsByAppType[key][ext] = totalCRsByAppType[key][ext] / numComps[key]
            for contrib in CRsnContribs[bm][ext][1].keys():
                meanContribsByAppType[key][ext][contrib] = totalContribsByAppType[key][ext][contrib] / numComps[key]
        keys = meanCrsByAppType[key].keys()
        values = zip(meanCrsByAppType[key].values(), meanContribsByAppType[key].values())
        meanCrsByAppType[key] = dict(zip(keys, values))
        print(file=outfile)
        print("--------------------------------------------------------------",file=outfile)
        print("--------------------------------------------------------------",file=outfile)
        print(f"AVERAGE COMPRESSION RATIOS OVER {key.upper()} APPLICATIONS:",file=outfile)
        pprint(meanCrsByAppType[key], stream=outfile)
        print("--------------------------------------------------------------",file=outfile)
        print("--------------------------------------------------------------",file=outfile)
    return meanCrsByAppType
    
def mean_category_CRs(categoryCRs: dict, outfile):
    totalCRs = {'rv64ifdc':{'int_comp':0,'cond_CT':0,'uncond_CT':0,'int_ld_st':0,'fp_ld_st':0},'rv64ifd_zca':{'int_comp':0,'cond_CT':0,'uncond_CT':0,'int_ld_st':0,'fp_ld_st':0},'rv64ifd_zcd':{'int_comp':0,'cond_CT':0,'uncond_CT':0,'int_ld_st':0,'fp_ld_st':0},'rv64ifd_zcb':{'int_comp':0,'cond_CT':0,'uncond_CT':0,'int_ld_st':0,'fp_ld_st':0},'rv64ifd_zcmp':{'int_comp':0,'cond_CT':0,'uncond_CT':0,'int_ld_st':0,'fp_ld_st':0},'rv64ifd_zcmt':{'int_comp':0,'cond_CT':0,'uncond_CT':0,'int_ld_st':0,'fp_ld_st':0},'rv64ifd_zce':{'int_comp':0,'cond_CT':0,'uncond_CT':0,'int_ld_st':0,'fp_ld_st':0}}
    meanCRs = {'rv64ifdc':{'int_comp':0,'cond_CT':0,'uncond_CT':0,'int_ld_st':0,'fp_ld_st':0},'rv64ifd_zca':{'int_comp':0,'cond_CT':0,'uncond_CT':0,'int_ld_st':0,'fp_ld_st':0},'rv64ifd_zcd':{'int_comp':0,'cond_CT':0,'uncond_CT':0,'int_ld_st':0,'fp_ld_st':0},'rv64ifd_zcb':{'int_comp':0,'cond_CT':0,'uncond_CT':0,'int_ld_st':0,'fp_ld_st':0},'rv64ifd_zcmp':{'int_comp':0,'cond_CT':0,'uncond_CT':0,'int_ld_st':0,'fp_ld_st':0},'rv64ifd_zcmt':{'int_comp':0,'cond_CT':0,'uncond_CT':0,'int_ld_st':0,'fp_ld_st':0},'rv64ifd_zce':{'int_comp':0,'cond_CT':0,'uncond_CT':0,'int_ld_st':0,'fp_ld_st':0}}
    numComps = {'rv64ifdc':{'int_comp':15,'cond_CT':15,'uncond_CT':15,'int_ld_st':15,'fp_ld_st':15},'rv64ifd_zca':{'int_comp':15,'cond_CT':15,'uncond_CT':15,'int_ld_st':15,'fp_ld_st':15},'rv64ifd_zcd':{'int_comp':15,'cond_CT':15,'uncond_CT':15,'int_ld_st':15,'fp_ld_st':15},'rv64ifd_zcb':{'int_comp':15,'cond_CT':15,'uncond_CT':15,'int_ld_st':15,'fp_ld_st':15},'rv64ifd_zcmp':{'int_comp':15,'cond_CT':15,'uncond_CT':15,'int_ld_st':15,'fp_ld_st':15},'rv64ifd_zcmt':{'int_comp':15,'cond_CT':15,'uncond_CT':15,'int_ld_st':15,'fp_ld_st':15},'rv64ifd_zce':{'int_comp':15,'cond_CT':15,'uncond_CT':15,'int_ld_st':15,'fp_ld_st':15}}
    for bm in categoryCRs.keys():
        for ext in totalCRs.keys():
            for cat in totalCRs[ext].keys():
                if not(isinstance(categoryCRs[bm][ext][cat], str)):
                    totalCRs[ext][cat] += categoryCRs[bm][ext][cat]
                else:
                    numComps[ext][cat] -= 1
    for ext in totalCRs.keys():
        for cat in totalCRs[ext].keys():
            meanCRs[ext][cat] = totalCRs[ext][cat] / numComps[ext][cat]
    print(file=outfile)
    print("--------------------------------------------------------------",file=outfile)
    print("--------------------------------------------------------------",file=outfile)
    print("AVERAGE CATEGORY COMPRESSION RATIOS OVER ALL BENCHMARKS:",file=outfile)
    pprint(meanCRs, stream=outfile)
    print("--------------------------------------------------------------",file=outfile)
    print("--------------------------------------------------------------",file=outfile)
    return meanCRs

def plotCRHeatMap(CRs: dict):
    crTable = [[0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0]]
    y_labels = ['basicmath','qsort','rijndael','dijkstra','bitcount','cjpeg','djpeg','stringsearch','whetstone','susan','fft','lame','crc32','sha','blowfish']
    x_labels = ['RVC','Zca','Zcb','Zcd','Zce','Zcmp','Zcmt']
    for i,bm in enumerate(CRs.keys()):
        print(i, bm)
        for j,ext in enumerate(CRs[bm].keys()):
            crTable[i][j] = CRs[bm][ext][0]
            if i == 0:
                print(j, ext)
    hm = sns.heatmap(crTable,annot=True,vmax=0.6,vmin=0.85,xticklabels=x_labels,yticklabels=y_labels,linewidths=1,linecolor='white')
    hm.set_title('All Compression Ratios')
    plt.show()

def plotMeanCRs(meanCRsnContribs: dict):
    colours = sns.color_palette('pastel',16)
    coloursByContrib = {'zca':3,'zcd':8,'zcb':9,'zcmp':4,'zcmt':5}
    chartProportions = {'rv64ifdc':[],'rv64ifd_zca':[],'rv64ifd_zcd':[],'rv64ifd_zcb':[],'rv64ifd_zcmp':[],'rv64ifd_zcmt':[],'rv64ifd_zce':[]}
    chartLabels = {'rv64ifdc':[],'rv64ifd_zca':[],'rv64ifd_zcd':[],'rv64ifd_zcb':[],'rv64ifd_zcmp':[],'rv64ifd_zcmt':[],'rv64ifd_zce':[]}
    chartColours = {'rv64ifdc':[],'rv64ifd_zca':[],'rv64ifd_zcd':[],'rv64ifd_zcb':[],'rv64ifd_zcmp':[],'rv64ifd_zcmt':[],'rv64ifd_zce':[]}
    for key in meanCRsnContribs.keys():
        chartProportions[key].append(meanCRsnContribs[key][0])
        chartLabels[key].append('')
        chartColours[key].append(colours[2])
        for contrib in meanCRsnContribs[key][1].keys():
            if meanCRsnContribs[key][1][contrib] > 0:
                chartProportions[key].append(meanCRsnContribs[key][1][contrib])
                chartLabels[key].append(contrib)
                chartColours[key].append(colours[coloursByContrib[contrib]])
    fig, ax = plt.subplots(2,4,figsize=(25,25),squeeze=True)
    fig.suptitle('Mean Compression Ratios Over All Benchmarks')
    print(chartProportions)
    print(chartLabels)
    ax[0][0].pie(chartProportions['rv64ifdc'],labels=chartLabels['rv64ifdc'],colors=chartColours['rv64ifdc'],autopct='%.2f')
    ax[0][0].set_title('RVC')
    ax[0][1].pie(chartProportions['rv64ifd_zca'],labels=chartLabels['rv64ifd_zca'],colors=chartColours['rv64ifd_zca'],autopct='%.2f')
    ax[0][1].set_title('Zca')
    ax[0][2].pie(chartProportions['rv64ifd_zcd'],labels=chartLabels['rv64ifd_zcd'],colors=chartColours['rv64ifd_zcd'],autopct='%.2f')
    ax[0][2].set_title('Zcd')
    ax[0][3].pie(chartProportions['rv64ifd_zcb'],labels=chartLabels['rv64ifd_zcb'],colors=chartColours['rv64ifd_zcb'],autopct='%.2f')
    ax[0][3].set_title('Zcb')
    ax[1][0].pie(chartProportions['rv64ifd_zcmp'],labels=chartLabels['rv64ifd_zcmp'],colors=chartColours['rv64ifd_zcmp'],autopct='%.2f')
    ax[1][0].set_title('Zcmp')
    ax[1][1].pie(chartProportions['rv64ifd_zcmt'],labels=chartLabels['rv64ifd_zcmt'],colors=chartColours['rv64ifd_zcmt'],autopct='%.2f')
    ax[1][1].set_title('Zcmt')
    ax[1][2].pie(chartProportions['rv64ifd_zce'],labels=chartLabels['rv64ifd_zce'],colors=chartColours['rv64ifd_zce'],autopct='%.2f')
    ax[1][2].set_title('Zce')
    ax[1][3].remove()
    plt.show()

def plotMeanCRsByApplication(meanCRsnContribsByApp: dict):
    dataByAppType = {'automotive':[],'consumer':[],'office':[],'network':[],'security':[],'telecomm':[],'FP':[]}
    palette = sns.color_palette('bright',16)
    colours = [palette[2],palette[3],palette[9],palette[7],palette[4]]
    plt.rcParams['axes.spines.top'] = False
    plt.rcParams['axes.spines.right'] = False
    fig, ax = plt.subplots(4,2,figsize=(15,50),squeeze=True)
    for appType in meanCRsnContribsByApp.keys():
        print(type(meanCRsnContribsByApp[appType]))
        print(meanCRsnContribsByApp[appType])
        crs = []
        zcaContribs = []
        zcdContribs = []
        zcbContribs = []
        zcmpContribs = []
        for key in meanCRsnContribsByApp[appType].keys():
            print(key)
            crs.append(meanCRsnContribsByApp[appType][key][0]*100)
            zcaContribs.append(meanCRsnContribsByApp[appType][key][1]['zca']*100)
            zcdContribs.append(meanCRsnContribsByApp[appType][key][1]['zcd']*100)
            zcbContribs.append(meanCRsnContribsByApp[appType][key][1]['zcb']*100)
            zcmpContribs.append(meanCRsnContribsByApp[appType][key][1]['zcmp']*100)
        dataByAppType[appType].append(crs)
        dataByAppType[appType].append(zcaContribs)
        dataByAppType[appType].append(zcmpContribs)
        dataByAppType[appType].append(zcdContribs)
        dataByAppType[appType].append(zcbContribs)
    labels = ['RVC','Zca','Zcd','Zcb','Zcmp','Zcmt','Zce']
    ticks = [0,1,2,3,4,5,6]
    bottom = [0,0,0,0,0,0,0]
    ax[0][0].bar(ticks,dataByAppType['automotive'][0],width=0.5,align='center',color=colours[0],tick_label=labels)
    for i in range(1,5):
        bottom = [bottom[j]+dataByAppType['automotive'][i-1][j] for j in range(7)]
        ax[0][0].bar(ticks,dataByAppType['automotive'][i],bottom=bottom,width=0.5,align='center',color=colours[i],tick_label=labels)
    ax[0][0].set_ylabel('Automotive')
    bottom = [0,0,0,0,0,0,0]
    ax[0][1].bar(ticks,dataByAppType['consumer'][0],width=0.5,align='center',color=colours[0],tick_label=labels)
    for i in range(1,5):
        bottom = [bottom[j]+dataByAppType['consumer'][i-1][j] for j in range(7)]
        ax[0][1].bar(ticks,dataByAppType['consumer'][i],bottom=bottom,width=0.5,align='center',color=colours[i],tick_label=labels)
    ax[0][1].set_ylabel('Consumer')
    bottom = [0,0,0,0,0,0,0]
    ax[1][0].bar(ticks,dataByAppType['office'][0],width=0.5,align='center',color=colours[0],tick_label=labels)
    for i in range(1,5):
        bottom = [bottom[j]+dataByAppType['office'][i-1][j] for j in range(7)]
        ax[1][0].bar(ticks,dataByAppType['office'][i],bottom=bottom,width=0.5,align='center',color=colours[i],tick_label=labels)
    ax[1][0].set_ylabel('Office')
    bottom = [0,0,0,0,0,0,0]
    ax[1][1].bar(ticks,dataByAppType['network'][0],width=0.5,align='center',color=colours[0],tick_label=labels)
    for i in range(1,5):
        bottom = [bottom[j]+dataByAppType['network'][i-1][j] for j in range(7)]
        ax[1][1].bar(ticks,dataByAppType['network'][i],bottom=bottom,width=0.5,align='center',color=colours[i],tick_label=labels)
    ax[1][1].set_ylabel('Network')
    bottom = [0,0,0,0,0,0,0]
    ax[2][0].bar(ticks,dataByAppType['security'][0],width=0.5,align='center',color=colours[0],tick_label=labels)
    for i in range(1,5):
        bottom = [bottom[j]+dataByAppType['security'][i-1][j] for j in range(7)]
        ax[2][0].bar(ticks,dataByAppType['security'][i],bottom=bottom,width=0.5,align='center',color=colours[i],tick_label=labels)
    ax[2][0].set_ylabel('Security')
    bottom = [0,0,0,0,0,0,0]
    ax[2][1].bar(ticks,dataByAppType['telecomm'][0],width=0.5,align='center',color=colours[0],tick_label=labels)
    for i in range(1,5):
        bottom = [bottom[j]+dataByAppType['telecomm'][i-1][j] for j in range(7)]
        ax[2][1].bar(ticks,dataByAppType['telecomm'][i],bottom=bottom,width=0.5,align='center',color=colours[i],tick_label=labels)
    ax[2][1].set_ylabel('Telecomm')
    bottom = [0,0,0,0,0,0,0]
    ax[3][0].bar(ticks,dataByAppType['FP'][0],width=0.5,align='center',color=colours[0],tick_label=labels)
    for i in range(1,5):
        bottom = [bottom[j]+dataByAppType['FP'][i-1][j] for j in range(7)]
        ax[3][0].bar(ticks,dataByAppType['FP'][i],bottom=bottom,width=0.5,align='center',color=colours[i],tick_label=labels)
    ax[3][0].set_ylabel('FP')
    fig.legend(['CR','Zca','Zcmp','Zcd','Zcb'])
    ax[3][1].remove()
    plt.show()

def plotAppCRHeatMap(meanCRsnContribsByApp: dict):
    crTable = [[0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0]]
    y_labels = ['Automotive','Consumer','Office','Network','Security','Telecomm','FP']
    x_labels = ['RVC','Zca','Zcd','Zcb','Zcmp','Zcmt','Zce']
    for i,app in enumerate(meanCRsnContribsByApp.keys()):
        print(i,app)
        for j,ext in enumerate(meanCRsnContribsByApp[app].keys()):
            crTable[i][j] = meanCRsnContribsByApp[app][ext][0]
            if i == 0:
                print(j,ext)
    hm = sns.heatmap(crTable,annot=True,vmax=0.7,vmin=0.85,xticklabels=x_labels,yticklabels=y_labels,linewidths=1,linecolor='white')
    hm.set_title('Mean Compression Ratios Over Each Application Type')
    plt.show()
    

def plotCategoryCRHeatMap(CategoryCRs: dict):
    catCrTable = [[0,0,0,0,0,0,0],
                  [0,0,0,0,0,0,0],
                  [0,0,0,0,0,0,0],
                  [0,0,0,0,0,0,0],
                  [0,0,0,0,0,0,0]]
    y_labels = ['Int Comp','Cond CT','Uncond CT','Int Ld/St','FP Ld/St']
    x_labels = ['RVC','Zca','Zcd','Zcb','Zcmp','Zcmt','Zce']
    for i,ext in enumerate(CategoryCRs.keys()):
        for j,cat in enumerate(CategoryCRs[ext].keys()):
            catCrTable[j][i] = CategoryCRs[ext][cat]
    hm = sns.heatmap(catCrTable,annot=True,vmax=0.9,vmin=0.5,xticklabels=x_labels,yticklabels=y_labels,linewidths=1,linecolor='white')
    hm.set_title('Mean Category Compression Ratios')
    plt.show()
    
if __name__ == "__main__":
    with open('./stats.txt', 'w') as f:
        individualStats = all_individual_file_stats(f)
        meanCR = mean_CRs(individualStats[2], f)
        meansByApp = meanCRsByApplication(individualStats[2],f)
        meanCategoryCRs = mean_category_CRs(individualStats[3],f)
        plotCRHeatMap(individualStats[2])
        plotMeanCRs(meanCR)
        plotMeanCRsByApplication(meansByApp)
        plotAppCRHeatMap(meansByApp)
        plotCategoryCRHeatMap(meanCategoryCRs)
