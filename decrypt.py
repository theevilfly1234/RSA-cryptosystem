import rsa
import stdio
import sys


# Entry point.
def main():
    # Get private-key n and d from command-line arguments.
    n = int(sys.argv[1])
    d = int(sys.argv[2])

    # Get the number of bits per character.
    width = rsa.bitLength(n)

    # Read the message from standard input.
    while not stdio.isEmpty():
        message = stdio.readString()
        
    # Decrypt each character in the message and write it to standard output.
    length = len(message)
    for i in range(0, length, width):
        s = message[i:i+width]
        y = rsa.bin2dec(s)
        x = rsa.decrypt(y, n, d)
        stdio.writef('%c', chr(x))


if __name__ == '__main__':
    main()
