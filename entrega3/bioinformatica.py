
tabla = {
         "E": ["GAA", "GAG"],
         "M": ["AUG"],
         "H": ["CAU", "CAC"],
         "V": ["GUU", "GUC", "GUA", "GUG"],
         "Y": ["AUA", "UAC"], 
         "F": ["UUU", "UUC"],
         "G": ["GGU", "GGC", "GGA", "GGG"],
         "P": ["CCU", "CCC", "CCA", "CCG"],
         "D": ["GAU", "GAC"],
         "A": ["GCU", "GCC", "GCA", "GCG", ],
         "R": ["CGU", "CGC", "CGA", "CGG", "AGA", "AGG"],
         "N": ["AAU", "AAC"],
         "C": ["UGU", "UGC"],
         "Q": ["CAA", "CAG"], 
         "I": ["AUU", "AUC", "AUA"],
         "L": ["UUA", "UUG", "CUU", "CUC", "CUA", "CUG"], 
         "K": ["AAA", "AAG"],
         "S": ["UCU", "UCC", "UCA", "UCG", "AGU", "AGC"],
         "T": ["ACU", "ACC", "ACA", "ACG"],
         "W": ["UGG"] 
         }

# RETO II

def procesar_cadena_de_aminoacidos(cadena: str): 

    lista_de_codones = []
    for subCadena in cadena:
        lista_de_codones.append(tabla[subCadena.upper()][0])

    return lista_de_codones



# RETO III

def identificar_regiones_promotoras(cadena: str):
    regiones_promotoras = []

    cadena_para_identificar = cadena

    while len(cadena_para_identificar) > 6:
        posible_caja_tata = cadena_para_identificar[:6]
        cadena_para_identificar = cadena_para_identificar[6:]

        if 'TATAAA' == posible_caja_tata:
            
            region, resto_de_cadena_a_identificar = encontrar_region(cadena_para_identificar)
            regiones_promotoras.append(region)
            cadena_para_identificar = resto_de_cadena_a_identificar

    return regiones_promotoras


def encontrar_region(cadena: str):
    indice_donde_comienza = cadena.upper().index("M")
    
    region = ""
    resto_de_cadena = cadena[indice_donde_comienza:]
  

    while len(resto_de_cadena) > 6:
        posible_caja_tata = resto_de_cadena[:6]
        resto_de_cadena = resto_de_cadena[6:]
        if 'TATAAA' == posible_caja_tata:
            break
        else:
            region = region + posible_caja_tata
            
    return region, resto_de_cadena

    

def identificar_regiones_promotoras2(cadena: str):
    regiones_promotoras = []

    cadena_para_identificar = cadena.upper()

    while cadena_para_identificar:
        try:
            index_de_comienzo_caja_tata = cadena_para_identificar.index("TATAAA")
            cadena_para_identificar = cadena_para_identificar[index_de_comienzo_caja_tata:]
            index_de_comienzo_de_region = cadena_para_identificar.index("M") + 1
            cadena_para_identificar = cadena_para_identificar[index_de_comienzo_de_region:]
            index_de_fin_de_region = cadena_para_identificar.index("TATAAA")

            regiones_promotoras.append(cadena_para_identificar[:index_de_fin_de_region])
            cadena_para_identificar = cadena_para_identificar[index_de_fin_de_region:]
        except Exception as ex:
            # Puede pasar por aca por varias razones:
            # 1- No hay mas tata box en la cadena
            # 2- la cadena puede estar mal formada
            break
    
    return regiones_promotoras
        