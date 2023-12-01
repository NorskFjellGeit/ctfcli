#!/usr/bin/env python
import codecs


def encrypt(string):
    enc = codecs.getencoder("rot-13")
    return enc(string)[0]


def main():
    with open("src/flag.txt", encoding="utf-8") as f:
        print(encrypt(f.read()))


if __name__ == "__main__":
    main()
