from hashlib import sha256
import itertools

def decryptor(string,length,Hash):
    if len(Hash) == 64:
        while True:
            for element in itertools.product(string,repeat=length):
                passwd="".join(element)
                if Hash == sha256(passwd.encode()).hexdigest():
                    print(Hash+" : "+ passwd)
                    quit()
            length+=1
    else:
        print("Something wrong with your hash, try againg pleas!")


def main():
    Hash= input("Paste your hash: ")
    length = 1
    string="abcdefghijklmnopqrstuvwxyz1234567890 "
    decryptor(string,length,Hash)

main()
