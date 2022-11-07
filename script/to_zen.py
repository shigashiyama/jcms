import argparse
import sys
import zenhan


def run_from_stdin(normalize_space=False, normalize_tilde=False):
    run(iter(sys.stdin.readline, ''), 
        normalize_space=normalize_space, 
        normalize_tilde=normalize_tilde)


def run_from_file(input_file, normalize_space=False, normalize_tilde=False):
    with open(input_file) as f:
        run(f, normalize_space=normalize_space, normalize_tilde=normalize_tilde)


def run(generator, normalize_space=False, normalize_tilde=False):
    for line in generator:
        line = line.strip('\n')

        if normalize_space:
            line = zenhan.h2z(line, mode=7)
        else:
            line = zenhan.h2z(line, mode=7, ignore=' ')

        if normalize_tilde:
            line = line.replace('～', '〜')

        print(line)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--normalize_space', '-s', action='store_true')
    parser.add_argument('--normalize_tilde', '-t', action='store_true')
    args = parser.parse_args()

    run_from_stdin(normalize_space=args.normalize_space, 
                   normalize_tilde=args.normalize_tilde)
