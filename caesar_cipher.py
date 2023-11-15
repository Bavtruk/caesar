alfabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
#def e; t=ievaditais teksts; r=rotacijas skaitlis; Katru burtu no ievadita teksta meklē vai ir teksta alfabets,burta ar 0 vertibu iepriekšajo burtu pec alfabeta (A ir 1, B ir 2, C ir 3 un t.t ) 
def e(teksts, rotacija):
  resultats = ""
  for c in teksts:
      if (alfabets.find(c) == -1):
          resultats += c
      else: 
          resultats += (alfabets[(alfabets.find(c) + rotacija) % len(alfabets)])
  return resultats
#def d; t=ievaditais teksts; r=rotacijas skaitlis; Katru burtu no ievadita teksta meklē vai ir teksta alfabets,burta ar 0 vertibu iepriekšajo burtu pec alfabeta (A ir 1, B ir 2, C ir 3 un t.t ) 
#ja ir tad pieraksta rotacijas skaitlis teksta alfabeta burtu vertibu pec alfa
def d(t, o):
  resultats = ""
  for c in t:
      if (alfabets.find(c) == -1):
          resultats += c
      else:
          resultats += (alfabets[(alfabets.find(c) - o) % len(alfabets)])
  return resultats

w = """
1. Encrypt text
2. Decrypt text
3. Bruteforce all rotations
Choose mode: """
mode = int(input(w))
#ja izvēles 1,tad izpildās šāds kods, ja izvēles 2, tad paradas tikai tad kods,kas bija pec pirma teksta
if mode == 1:
  text = input("Enter the text: ")
  rotation = int(input("Enter the rotation: "))
  print("Encrypted: " + e(text, rotation))
  #ja ievada mode '2' tad izpildas šads kods
elif mode == 2:
  text = input("Enter the text: ")
  rotation = int(input("Enter the rotation: "))
  #ja ievada mode=3 tad izvada 2 kodus, ja nav tad izvada 1 kodu
  print("Decrypted: " + d(text, rotation))
elif mode == 3:
  print("Bruteforcing...")
  print("But I don't know how to do it, sorry ¯\_(ツ)_/¯")
