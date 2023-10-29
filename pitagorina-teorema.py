#Ovaj program je napravio boris smiljanić
#kk znači kvadratni koren
import math
def ptrougao():
    a = float(input("Unesi stranicu u cm a: "))
    b = float(input("Unesi stranicu u cm b: "))
    a *= a
    b *= b
    c = a+b
    c_kk = math.sqrt(c)
    a_kk = math.sqrt(a)
    b_kk = math.sqrt(b)
    obim = a_kk + b_kk + c_kk
    povrsina =(a_kk*b_kk)/2
    print("C kvadrirano ", c, " ,C ", c_kk," ,obim ",obim," i povrsina ",povrsina)

def pravugaonik():
    a = float(input("Unesi stranicu u cm a: "))
    b = float(input("Unesi stranicu u cm b: "))
    a *= a
    b *= b
    c = a+b
    c_kk = math.sqrt(c)
    a_kk = math.sqrt(a)
    b_kk = math.sqrt(b)
    obim = (a_kk*2)+(b_kk*2)
    povrsina = a_kk*b_kk
    print("D kvadrirano ", c, " ,D ", c_kk," ,obim ",obim," i povrsina ",povrsina)
    

def kvadrat():
    a = float(input("Unesi stranicu u cm a: "))
    a *= a
    c = a*2
    c_kk = math.sqrt(2*(a*a))
    a_kk = math.sqrt(a)
    obim = a_kk * 4
    povrsina = a_kk * a_kk
    print("D kvadrirano ", c, " ,D ", c_kk," ,obim ",obim," i povrsina ",povrsina)

def jedkrak():
    a = float(input("Unesi stranicu u cm a: "))
    ha = float(input("Unesi visinu u cm ha: "))
    a /= 2
    a *= a
    ha *= ha
    c = a+ha
    c_kk = math.sqrt(c)
    a_kk = math.sqrt(a)
    a_kk *= 2
    ha_kk = math.sqrt(ha)
    obim = a_kk + (2*c_kk)
    povrsina =(a_kk*ha_kk)/2
    print("B kvadrirano ", c, " ,B ", c_kk," ,obim ",obim," i povrsina ",povrsina)
while True:
    unos = int(input("Izaberi: 0)izađi;1)pravougli trougao;2)pravugaonik;3)kvadrat;4)jednakokraki trougao; "))

    if unos == 1:
        ptrougao()
    elif unos == 2:
        pravugaonik()
    elif unos == 3:
        kvadrat()
    elif unos == 4:
        jedkrak()
    elif unos == 0:
        break
    else:
        print("Opcija nije validna")
    


