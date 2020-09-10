


tabla = {
         "E": (1.59, 0.52, 1.01),
         "M": (1.30, 1.14, 0.52),
         "H": (1.05, 0.80, 0.81),
         "V": (0.90, 1.87, 0.41),
         "Y": (0.74, 1.45, 0.76),
         "F": (1.16, 1.33, 0.59),
         "G": (0.43, 0.58, 1.77),
         "P": (0.34, 0.31, 1.32),
         "D": (0.99, 0.39, 1.24),
         "A": (1.41, 0.72, 0.82),
         "R": (1.21, 0.84, 0.90),
         "N": (0.76, 0.48, 1.34),
         "C": (0.66, 1.40, 0.54),
         "Q": (1.27, 0.98, 0.84),
         "I": (1.09, 1.67, 0.47),
         "L": (1.34, 1.22, 0.57),
         "K": (1.23, 0.69, 1.07),
         "M": (1.30, 1.14, 0.52),
         "S": (0.57, 0.96, 1.22),
         "T": (0.76, 1.17, 0.90),
         "W": (1.02, 1.35, 0.65) 
         }

estructuras = {
                0: "H",
                1: "B",
                2: "L"
             }


def predecir_un_aminoacido(aminoacido: str):
    tuple_ = tabla[aminoacido]
    return estructuras[tuple_.index(max(tuple_))]


def predecir_estructura(estructura_primaria: str):
    lista_de_tuplas = [tabla[aminoacido.upper()] for aminoacido in estructura_primaria]

    tupla_sumada = (sum([tupla[0] for tupla in lista_de_tuplas]), 
                    sum([tupla[1] for tupla in lista_de_tuplas]),
                    sum([tupla[2] for tupla in lista_de_tuplas]))

    
    return estructuras[tupla_sumada.index(max(tupla_sumada))]
