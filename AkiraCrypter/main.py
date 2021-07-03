from hashlib import sha256

print("AkiraCrypte Easy Crypter by AKIRA. \n-------------------------------------------------------------\nDiscord : AKIRA.#1854\n")

entree = input("enter the name of the file to encrypt / decrypt : ")
sortie = input("enter the name of the final file : ")
key = input("ente the key : ")
keys = sha256(key.encode('utf-8')).digest()
with open(entree, 'rb') as f_entree:
    with open(sortie,'wb') as f_sortie:
        i = 0
        while f_entree.peek():
            c = ord(f_entree.read(1))
            j = i % len(keys)
            b = bytes([c^keys[j]])
            f_sortie.write(b)
            i = i + 1