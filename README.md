# RSA Cryptosystem Implementation

This project is a Python-based implementation of the RSA encryption and decryption algorithm, designed primarily for educational purposes. It demonstrates the core concepts behind RSA cryptography, including key generation, encryption, and decryption processes.

## Background

The RSA algorithm is a cornerstone of modern cryptographic techniques. It's a public-key cryptosystem that is widely used for secure data transmission. Unlike symmetric key algorithms, which use the same key for both encryption and decryption, RSA employs a pair of keys — a public key for encryption and a private key for decryption.

## Features

- **Key Generation**: Generates RSA key pairs suitable for encryption and decryption.
- **Encryption**: Allows for encrypting messages using the public key.
- **Decryption**: Enables the decryption of messages with the private key, ensuring that only the intended recipient can read the message content.

## Getting Started

### Prerequisites

Ensure you have Python (version 3.x or newer) installed on your system to run this project.

### Installation

Clone the repository to your local machine:

```bash
git clone https://github.com/theevilfly1234/RSA-cryptosystem.git
cd RSA-cryptosystem

No additional Python libraries or dependencies are required to run this project.

Usage

Key Generation
To generate a new RSA key pair, run:
python keygen.py <low_primes_range> <high_primes_range>
Replace <low_primes_range> and <high_primes_range> with the desired range for prime number selection.

Encryption

To encrypt a message using a generated public key:
python encrypt.py <public_key_n> <public_key_e>
Enter the message you wish to encrypt when prompted.

Decryption
To decrypt a message using your private key:
python decrypt.py <private_key_n> <private_key_d>
Input the encrypted message to retrieve the original content.

Contributing
Contributions to this project are welcome! Please feel free to fork the repository, make changes, and submit a pull request with your improvements.

License
This RSA Cryptosystem project is made available under the MIT License. Feel free to use, modify, and distribute the code as you see fit.

Acknowledgments
Thanks to the RSA algorithm's inventors, Rivest, Shamir, and Adleman, for their groundbreaking work in cryptography.
This project was inspired by the desire to understand and implement fundamental cryptographic techniques in Python
