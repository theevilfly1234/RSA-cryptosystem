import rsa
import stdio
import sys


# Entry point.
def main():
    if len(sys.argv) < 3:
        stdio.writeln("Usage: python keygen.py <lo> <hi>")
        sys.exit(1)

    lo = int(sys.argv[1])
    hi = int(sys.argv[2])

    n, e, d = rsa.keygen(lo, hi)

    stdio.writef("%d %d %d\n", n, e, d)


if __name__ == '__main__':
    main()
