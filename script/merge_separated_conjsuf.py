import sys


## conversion rules from SUW-SC -> SUW
#
# 動詞-特殊型-*   -> 動詞-*
# 形容詞-特殊型   -> 形容詞-一般 (「～ねえ」「～ネエ」）
# 助動詞-特殊型   -> 助動詞
#
# 動詞-語幹-*         + 活用語尾-動詞型   -> 動詞-*
# 形容詞-語幹-*       + 活用語尾-形容詞型 -> 形容詞-*
# 接尾辞-動詞型語幹   + 活用語尾-動詞型   -> 接尾辞-動詞的
# 接尾辞-形容詞型語幹 + 活用語尾-形容詞型 -> 接尾辞-形容詞的
# 助動詞-動詞型語幹   + 活用語尾-動詞型   -> 助動詞
# 助動詞-形容詞型語幹 + 活用語尾-形容詞型 -> 助動詞


IDX_TOK = 0
IDX_POS = 1
IDX_REST = 2

def get_npos_from_ppos(ppos):
    if ppos.startswith('動詞-語幹') or ppos.startswith('形容詞-語幹'):
        npos = ppos.replace('-語幹', '')
                
    elif ppos.startswith('接尾辞-動詞型語幹') or ppos.startswith('接尾辞-形容詞型語幹'):
        npos = ppos.replace('型語幹', '的')

    elif ppos.startswith('助動詞'):
        npos = '助動詞'

    else:
        npos = '{}'.format(ppos)

    return npos


def run(generator):
    ntok = npos = nrest = ''
    ptok = ppos = prest = ''

    for line in generator:
        line = line.strip('\n')
        if not line:
            if ptok:
                ntok = ptok
                npos = get_npos_from_ppos(ppos)
                nrest = prest
                print('{}\t{}\t{}'.format(ntok, npos, nrest))
                ptok = ppos = prest = ''
            print()
            continue

        elif line[0] == '#':
            print(line)
            continue

        array = line.split('\t')
        tok = array[IDX_TOK]
        pos = array[IDX_POS]
        rest = array[IDX_REST]
        # rest = '\t'.join(array[IDX_REST:])

        # 直前の単語 (活用語語幹) の処理

        flag_cs = False
        if ptok:
            if pos.startswith('活用語尾'):
                flag_cs = True
                ntok = ptok + tok
            else:
                ntok = ptok

            npos = get_npos_from_ppos(ppos)
            # if npos.startswith('['):
            #    print(ptok, ppos, file=sys.stderr)
            #    print(line, file=sys.stderr)
            nrest = '{}+{}'.format(prest, rest).strip('+')
            print('{}\t{}\t{}'.format(ntok, npos, nrest))
            ptok = ppos = prest = ''
            if flag_cs:
                continue

        # 現在の単語の処理
        
        if pos.startswith('動詞'):
            if pos.startswith('動詞-特殊型'):
                npos = pos.replace('-特殊型', '')

            else:               # 動詞-語幹-一般/非自立可能
                ptok = tok
                ppos = pos
                prest = rest
                continue

        elif pos.startswith('形容詞'):
            if pos.startswith('形容詞-特殊型'):
                npos = pos.replace('-特殊型', '-非自立可能')

            else:               # 形容詞-語幹-一般/非自立可能
                ptok = tok
                ppos = pos
                prest = rest
                continue

        elif pos.startswith('助動詞'):
            if pos.startswith('助動詞-特殊型'):
                npos = pos.replace('-特殊型', '')

            else:               # 助動詞-動詞型語幹/形容詞型語幹
                ptok = tok
                ppos = pos
                prest = rest
                continue

        elif pos.startswith('接尾辞'):
            if pos.startswith('接尾辞-名詞型') or pos == '接尾辞-形状詞型':
                npos = pos.replace('型', '的')

            else:               # 接尾辞-形容詞型語幹/動詞型語幹
                ptok = tok
                ppos = pos
                prest = rest
                continue

        else:
            npos = pos

        ntok = tok
        nrest = rest
        print('{}\t{}\t{}'.format(ntok, npos, nrest))
        ntok = npos = nrest = ''


def run_from_file(input_file):
    with open(input_file) as f:
        run(f)


def run_from_stdin():
    run(iter(sys.stdin.readline, ''))

            
if __name__ == '__main__':
    if len(sys.argv) > 1:
        run_from_file(sys.argv[1])

    else:
        run_from_stdin()
