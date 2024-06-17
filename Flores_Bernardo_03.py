lista=[]
import csv
def menu():
    print("1.-Agregar plan")
    print("2.-Listar planes")
    print("3.-Eliminar plan por ID")
    print("4.-Generar bbdd")
    print("5.-Cargar bbdd")
    print("6.-Estadisticas")
    print("0.-Salir")
def verificacion_porcentaje(x):
        while x<0 or x>100:
            x=int(input("Error!, numero debe ser entre el rango de 0-100, vuelva a ingresarlo \n"))
        else:
            return x
def categoria_interna(x):
    if x<=25:
        return "Chiste"
    elif x>=26 and x<=50:
        return "Anecdota"
    elif x>=51 and x<=75:
        return "Peligro"
    elif x>=76 and x<=99:
        return "Atencion"
    elif x>=100:
        return "Esclavitud"
def verificacion_eliminacion():
    ver=input("Esta seguro que desea eliminarlo? si/no \n").lower()
    return ver
           
def op1():
    ID=int(input("Ingrese ID \n"))
    nombre=input("Ingrese nombre \n")
    porcentaje_ef=int(input("Ingrese porcentaje de efectividad \n"))
    porcentaje_ef_ver=verificacion_porcentaje(porcentaje_ef)
    categoria=categoria_interna(porcentaje_ef)
    lista_datos=[ID,nombre,porcentaje_ef_ver,categoria]
    lista.append(lista_datos)
    
def op2():
    for i in lista:
        print(f"ID: {i[0]}, nombre: {i[1]}, porcentaje de efectividad: {i[2]}, categoria: {i[3]}")

def op3():
    Encontrado=False
    Id_del=int(input("Ingrese la id del plan a eliminar \n"))
    for i in lista:
        if int(i[0])==Id_del:
            Encontrado=True
            print("Plan encontrado!")
            print(f"ID: {i[0]}, nombre: {i[1]}, porcentaje de efectividad: {i[2]}, categoria: {i[3]}")
            confr=verificacion_eliminacion()
            if confr=="si"or confr=="s":
                lista.remove(i)
                print("Plan eliminado correctamente!")
                break
            else:
                print("El plan NO ha sido eliminado!")
                break
    if Encontrado==False:
        print ("Archivo no encontrado")
        
def op4():
    with open("Archivo_laboratorio.csv","w",newline="")as Archivo_laboratorio:
        lectorcsv=csv.writer(Archivo_laboratorio)
        lectorcsv.writerow(["Id","Nombre","porcentaje de efectividad","categoria"])
        lectorcsv.writerows(lista)
def op5():
    lista.clear
    cont=0
    with open("Archivo_laboratorio.csv","r",newline="")as Archivo_laboratorio:
        lectorcsv=csv.reader(Archivo_laboratorio)
        for i in lectorcsv:
            if cont==0:
                cont+=1
                continue
            idnl=int(i[0])
            nom=(i[1])
            poref=int(i[2])
            cat=(i[3])
            listapeke=[idnl,nom,poref,cat]
            lista.append(listapeke)
def op6():
    efectividades=0
    ef_mas_alta=0
    for i in lista:
        efectividades=i[2]+efectividades
        if i[2]>ef_mas_alta:
            ef_mas_alta=i[2]
    cantidad_de_planes=len(lista)
    porcentaje_ef_promedio=efectividades/cantidad_de_planes
    print(f"La efectividad mas alta hasta el momento es de {ef_mas_alta}")
    print(f"El porcentaje promedio de las efectividades es de {porcentaje_ef_promedio}")
def op0():
    print ("Adios!")
def mensaje_de_error():
    print ("Error vuelva a ingresar!")
            
        
            
    
    
    
    
while True:
    try:
        menu()
        op=int(input("Ingrese una opcion \n"))
        if op==1:
            op1()
        elif op==2:
            op2()
        elif op==3:
            op3()
        elif op==4:
            op4()
        elif op==5:
            op5()
        elif op==6:
            op6()
        elif op==0:
            op0()
            break 
        else:
            mensaje_de_error()
    except:
        mensaje_de_error()
        
###Link github https://github.com/bernyFr1/Flores-Bernardo-03.git
    