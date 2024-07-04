import random
personas =()

persona =[]

dic_persona={}


def grabar_datos():
    
    nif = input("ingresa nif, 8 digitos, guion y 3 caracteres")
    nombre = input("ingresa nombre, minimo 8 caracteres")
    edad = int(input("ingresa edad"))
    
         
    persona={
            "nif" : nif, 
            "nombre" : nombre,
            "edad" : edad   
            }
    personas.append(persona)     
    
def buscar_persona():
    nif = input("ingresa nif") 
    encontrado = False
    for persona in personas:
        if persona["nif"] == nif:
            print(persona)
            encontrado = True
    if not encontrado:
        print("nif no encontrado")
        
def imprimir_certificados():
    nif = input("ingresa nif")
    for persona in personas:
        if persona["nif"] == nif:
            certificado_nacimiento = random.randint(1500, 5000)
            estado_conyugal = random.randint(1500, 5000)
            pertenencia_europea = random.randint(1500, 5000)
            
            print("certificado nacimiento")
            print(f"nif : {persona["nif"]}")
            print(f"nombre : {persona["nombre"]}")
            print(f"edad : {persona["edad"]}")
            print(f"valor certificado : {certificado_nacimiento}")
            
            
            print("estado conyugal")
            print(f"nif : {persona["nif"]}")
            print(f"nombre : {persona["nombre"]}")
            print(f"edad : {persona["edad"]}")
            print(f"valor certificado : {estado_conyugal}")  
            
            print("pertenencia a la union europea")
            print(f"nif : {persona["nif"]}")
            print(f"nombre : {persona["nombre"]}")
            print(f"edad : {persona["edad"]}")
            print(f"valor certificado : {pertenencia_europea}")  

def salir():
    print("macarena muñoz")
    print("version 1")
    print("finalizado")            
                    
    
while True:
    print("1. grabar datos")
    print("2. buscar datos")
    print("3. imprimir certificado")
    print("4. salir")
    
    opcion = int(input("seleccionar opcion : "))
    
    if opcion == 1:
        grabar_datos()
    elif opcion == 2:
        buscar_persona()
    elif opcion == 3:
        imprimir_certificados()
    elif opcion == 4:
        salir()
        break                                  
    