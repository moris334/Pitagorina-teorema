#Ovaj program je napravio boris smiljanić
import math
def ptrougao():
    a = int(input("Unesi stranicu a: "))
    b = int(input("Unesi stranicu b: "))
    a *= a
    b *= b
    c = a+b
    c_kk = math.sqrt(c)
    print("C kvadrirano ", c, " ,C ", c_kk)

def pravugaonik():
    a = int(input("Unesi stranicu a: "))
    b = int(input("Unesi stranicu b: "))
    a *= a
    b *= b
    c = a+b
    c_kk = math.sqrt(c)
    print("D kvadrirano ", c, " ,D ", c_kk)

def kvadrat():
    a = int(input("Unesi stranicu a: "))
    a *= a
    c = a*2
    c_kk = math.sqrt(c)
    print("D kvadrirano ", c, " ,D ", c_kk)

def jedkrak():
    a = int(input("Unesi stranicu a: "))
    ha = int(input("Unesi stranicu b: "))
    a /= 2
    a *= a
    ha *= ha
    c = a+b
    c_kk = math.sqrt(c)
    print("Ha kvadrirano ", c, " ,Ha ", c_kk)

unos = int(input("Izaberi: 1)pravougli trougao;2)pravugaonik;3)kvadrat;4)jednakokraki trougao"))

if unos == 1:
    ptrougao()
elif unos == 2:
    pravugaonik()
elif unos == 3:
    kvadrat()
elif unos == 4:
    jedkrak()
else:
    print("Opcija nije validna")
    


