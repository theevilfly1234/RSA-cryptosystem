import rsa
import stdio
import sys


# Entry point.
def main():
    # Get n and e from command-line arguments.
    n = int(sys.argv[1])
    e = int(sys.argv[2])

    # Get the number of bits per character needed for encryption.
    width = rsa.bitLength(n)

    # Read message from standard input.
    message = stdio.readAll()

    # Encrypt each character and write the encrypted value as a width-long binary string.
    for c in message:
        # Turn character c into an integer x.
        x = ord(c)

        # Encrypt x.
        encrypted = rsa.encrypt(x, n, e)

        # Write the encrypted value as a width-long binary string.
        encrypted_binary = rsa.dec2bin(encrypted, width)
        stdio.writef('%s', encrypted_binary)

    # Write a newline character.
    stdio.writeln()


if __name__ == '__main__':
    main()
