import re
import random
import os,sys
import time

time.sleep (2)
os.system('clear')
banner = """
░█████╗░██╗░░██╗░█████╗░████████╗
██╔══██╗██║░░██║██╔══██╗╚══██╔══╝
██║░░╚═╝███████║███████║░░░██║░░░
██║░░██╗██╔══██║██╔══██║░░░██║░░░
╚█████╔╝██║░░██║██║░░██║░░░██║░░░
░╚════╝░╚═╝░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░V1.0"""
print(banner)
ga = "================================="
se = "---------------"
print(ga)
print ("[+] Author \t: Mr-Gabut")
print ("[+] Youtube\t: FireMe")
print(ga)
print(se)
print ("[1]. Laki-laki\n[2]. Perempuan")
print(se)
kelamin = int(input("[+]Pilih : "))
if kelamin == 1:
  nama = input("Siapa namanya ganteng : ")
else :
  nama = input("Siapa namanya cantik : ")
bales = ["Hayy", "Hai", "Hallo"]
bales2 = ["Makkasih", "Ok dah", "Sipp"]
bales3 = ["Aku mesin jadi gak makan....", "Sayanya kan mesin jadi gak makan...."]
bales4 = ["Dilarang pacaran", "Aq gak punya pacar"]
bales5 = ["Jangan pergi aku masih ingin chatt sama kamu", "Secepat itukah kamu meninggalkanku"]

print("Silakan ngobrol ama bot", nama, "\nCTRL + c untuk keluar")
while True:
  x = input("User\t: ")
  if re.findall(r'hai|hallo|hay|halo', x):
    print("Bot\t\t:", random.choice(bales))
  elif re.findall(r'ok|iya', x):
    print("Bot\t\t:", random.choice(bales2))
  elif re.findall(r'udah makan|makan', x):
    print("Bot\t\t:", random.choice(bales3), nama)
  elif re.findall(r'pacar|ayyang|ayang|ayank', x):
    print("Bot\t\t:", random.choice(bales4))
  elif re.findall(r'udah|dah|sudah', x):
    print("Bot\t\t:", random.choice(bales5))
  else:
    print("Bot\t\t: Maff ", nama, " coba kamu mulai dengan sapaan 'hay atau hallo' yahh....")
