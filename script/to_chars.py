import sys
import argparse


def run(
        f,
        segmented,
        max_size,
        output_type,
        split_by_newline,
):
    count = 0
    chars = []

    for line in f:
        line = line.rstrip(' \t\n\r')
        if not line:
            if split_by_newline and chars:
                if output_type == 'raw':
                    out = ''.join(chars)
                else:
                    out = ' '.join(chars)
                print(out)
                chars = []

            continue

        if segmented:
            array = line.split(' ')
            for word in array:
                if output_type == 'unigram':
                    chars.extend([c for c in word])
                elif output_type == 'bigram':
                    print('Not implemented')
                    sys.exit()
                else:
                    chars.append(word)
        else:
            line = line.replace(' ', '')
            if output_type == 'unigram':
                chars.extend([c for c in line])
            elif output_type == 'bigram':
                sen_len = len(line)
                chars.extend([line[i:i+2] for i in range(sen_len-1)])
                chars.append(line[sen_len-1]+'<E>')
            else:
                print('Invalid type')
                sys.exit()

        if len(chars) > max_size:
            if output_type == 'raw':
                out = ''.join(chars)
            else:
                out = ' '.join(chars)
            print(out)
            chars = []

    if chars:
        if output_type == 'raw':
            out = ''.join(chars)
        else:
            out = ' '.join(chars)
        print(out)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--input_path', '-i')
    parser.add_argument('--output_type', '-t', required=True) # unigram, bigram, word, raw
    parser.add_argument('--segmented', '-s', action='store_true')
    parser.add_argument('--max_size', '-m', type=int, default=1000)
    parser.add_argument('--split_by_newline', '-n', action='store_true')
    args = parser.parse_args()
    # print(args, '\n', file=sys.stderr)

    if args.input_path:
        f = open(args.input_path, 'r')
    else:
        f = iter(sys.stdin.readline, '')

    run(f,
        args.segmented,
        args.max_size,
        args.output_type,
        args.split_by_newline)

    if args.input_path:
        f.close()
