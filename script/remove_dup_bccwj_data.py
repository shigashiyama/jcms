import sys


def read_duplicated_sentences(path):
    dsens = {}

    with open(path) as f:
        for line in f:
            if not line:
                continue

            line = line.strip('\n')
            dsens[line] = 0

    return dsens


def read_and_write_notdup_sentences(path, dsens, use_pos=False):
    words = []

    with open(path) as f:
        for line in f:
            line = line.strip('\n')
            if not line:
                if use_pos:
                    sen = ' '.join([f'{word[1]}_{word[0]}' for word in words])
                else:
                    sen = ''.join([word[0] for word in words])
                if sen in dsens:
                    if dsens[sen] == 0:
                        # print('duplicated sentence (1st)', file=sys.stderr)
                        print_words(words)
                        words = []
                        dsens[sen] = 1
                    else:
                        # print('duplicated sentence (2nd)', sen, file=sys.stderr)
                        words = []

                else:
                    print_words(words)
                    words = []

                continue

            array = line.split('\t')
            words.append(array)

        if words:
            sen = ''.join([word[0] for word in words])
            if sen in dsens:
                if dsens[sen] == 0:
                    # print('duplicated sentence (1st)', file=sys.stderr)
                    print_words(words)
                    words = []
                    dsens[sen] = 1
                else:
                    # print('duplicated sentence (2nd)', sen, file=sys.stderr)
                    words = []

            else:
                print_words(words)
                words = []


def print_words(words):
    for word in words:
        print('\t'.join(word))
    print()


if __name__ == '__main__':
    tsv_path = sys.argv[1]
    dup_path = sys.argv[2]
    use_pos = False
    if len(sys.argv) > 3 and sys.argv[3] == 'use_pos':
        use_pos = True

    dsens = read_duplicated_sentences(dup_path)
    # print(len(dsens), file=sys.stderr)
    read_and_write_notdup_sentences(tsv_path, dsens, use_pos=use_pos)
