# File Name : pdfpasscracker.py
# Version   : 1.0
# Author    : PawanKumar {SmartxCodes}
# Youtube   : "https://www.youtube.com/SmartXCodes"
# Website   : "https://www.smartxcodes.blogspot.com"
# Language  : Python version3.8
# Useage    : To crack pdf files password .

import os, pikepdf # to install pikepdf type pip install pikepdf in terminal
from time import sleep
from tqdm import tqdm # to install tqdm type pip install tqdm in terminal

sleep(1);
print("Cracker Info :")
print("         Name      : PDF Cracker")
print("         Version   : 1.0")
print("         Author    : PawanKumar {SmartxCodes}")
print("         Youtube   : https://www.youtube.com/SmartXCodes")
print("         Website   : https://www.smartxcodes.blogspot.com")
print("         Language  : Python version3.8")
print("         Useage    : To crack pdf files password .")
sleep(3);

pdf_file = input("Pdf File <path//file.pdf> : ")
wlt_file = input("Wordlist <path//file.txt> : ")
passwords = [line.strip() for line in open(wlt_file)]
n_words = len(list(open(wlt_file,"rb")))

sleep(1);
print("[+]Total passwords to test [+] ",n_words," [+]")
sleep(1);

for password in tqdm(passwords, "[+]Decrypting PDF "):
    try:
        with pikepdf.open(pdf_file, password=password) as pdf:
            print("[+] Password Found ! ",password," ![+]")
            break
    except pikepdf._qpdf.PasswordError as e:
        continue
