lineas=[]
linea = "no vacio"
while(linea != ""):
    linea = raw_input("ingrese una linea de texto")
    lineas.append(linea.upper())
    
for l in lineas:
    print l
