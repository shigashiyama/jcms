import sys


def read_sentence(input_text):
    with open(input_text) as f:
        for line in f:
            line = line.strip('\n')
            yield line


def run(input_masked, input_text):
    g = read_sentence(input_text)
    sid = -1
    org_sen = ''
    words = []
    next_begin = 0

    with open(input_masked) as f:
        for line in f:
            line = line.strip('\n')

            if line.startswith('#'):
                sid = line.split(' ')[1].split('=')[1]
                org_sen = g.__next__()
                words = []
                next_begin = 0

            elif line:
                array = line.split('\t')
                dummy = array[0]
                pos   = array[1]
                attr  = array[2] if len(array) > 2 else ''

                if attr.startswith('org_str:'):
                    org_str = attr.split(':')[1]
                    begin = next_begin
                    end = begin + len(org_str)
                    next_begin = end
                    surf = dummy

                else:
                    begin = next_begin
                    end = begin + len(dummy)
                    next_begin = end
                    surf = org_sen[begin:end]

                words.append((surf, pos, attr))
                
            else:
                new_sen = ''.join([word[0] for word in words])

                if org_sen and next_begin != len(org_sen):
                    print('Error. total_word_len={} VS org_sen_len={}. \norg_sen={}\nnew_sen={}'.format(next_begin, len(org_sen), org_sen, new_sen), file=sys.stderr)                        
                    sys.exit()

                print('# ID={} TEXT={}'.format(sid, new_sen))
                for word in words:
                    print('\t'.join(word))
                print()


if __name__ == '__main__':
    input_masked = sys.argv[1]
    input_text = sys.argv[2]
    run(input_masked, input_text)
