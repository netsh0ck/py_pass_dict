#!/usr/bin/python
# -*- coding: utf-8 -*-
import crypt


def testPass(cryptHash):
    hash = cryptHash[0:2]
    dictfile = open('dictionary.txt', 'r')
    for lump in dictfile.readlines():
        lump = lump.strip('\n')
        cryptword = crypt.crypt(lump, salt)
        if cryptW == cryptP:
            print '[SUCCESS] Password found: ' + lump + '\n'
            return
    print '[FAILURE] No password found.\n'
    return


def main():
    passfile = open('passwords.txt')
    for line in passfile.readlines():
        if ':' in line:
            user = line.split(':')[0]
            cryptHash = line.split(':')[1].strip(' ')
            print '[***] Cracking Password For: ' + user
            testPass(cryptHash)


if __name__ == '__main__':
    main()
