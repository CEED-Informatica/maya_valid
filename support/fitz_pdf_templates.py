# -*- coding: utf-8 -*-

# Cuando no se encuentran los fields (por ejempl, Adobe los elimina al firmar el documento)
# se utiliza pyMuPDF para poder "leer" el pdf y extraer la información
# NOTA: es preferible que lso datos estén en fields, 
# este recurso solo debe ser utilizado si no queda otra opción
# Para ello se necesita una plantilla que indique en que posición está el valor

# La estructura de la plantilla es:
# clave, xmin, ymin, tipo (ver funcion inttype2string), valor por defecto 
PDF_NOFIELDS_FITZ_VALIDATION = [ 
     ('A_Apellidos', 159.25, 113,47, 7, ''),
     ('A_Nombre', 408.6, 96,3, 7, ''),
     ('A_NIA', 304, 98.27, 7, ''),
     ('A_DNI', 201.80, 98.27, 7, ''),
     ('A_Direccion', 159.9, 130.57, 7, ''),
     ('A_Telefono', 155.9, 163.3, 7, ''),
     ('A_Poblacion', 267.45, 147.12, 7, ''),
     ('A_Provincia', 443.4, 147.12, 7, ''),
     ('A_CP', 175, 146.6, 7, ''),
     ('A_Mail', 350.5, 163.3, 7, ''),
     ('B_Requisito1', 111.55, 362.2, 2, 'Off'),
     ('B_Requisito2', 111.55, 387.9, 2, 'Off'),
     ('B_Requisito3', 111.55, 398.8, 2, 'Off'),
     ('B_Requisito4', 111.55, 409.7, 2, 'Off'),
     ('B_OtrosEstudios', 342.7, 410.4, 7, ''),
     ('C_Docu1', 111.55, 594.45, 2, 'Off'),
     ('C_Docu2', 111.55, 603.8, 2, 'Off'),
     ('C_Docu3', 111.55, 623.1, 2, 'Off'),
     ('C_Docu4', 111.55, 633.5, 2, 'Off'),
     ('C_Docu5', 111.55, 645.75, 2, 'Off'),
     ('C_Docu6', 111.55, 665.95, 2, 'Off'),
     ('C_OtrosDocumentos', 153.7, 646.45, 7, ''),
     ('C_EstudiosCEED', 117.95, 688.1, 7, ''),
     ('C_Modulo1', 36.54, 481.7, 3, ''),
     ('C_Modulo1AACO', 136.9, 481.7, 3, ''),
     ('C_Modulo2', 171.35, 481.7, 3, ''),
     ('C_Modulo2AACO', 271.75, 481.7, 3, ''),
     ('C_Modulo3', 306.15, 481.7, 3, ''),
     ('C_Modulo3AACO', 406.55, 481.7, 3, ''),
     ('C_Modulo4', 440.95, 481.7, 3, ''),
     ('C_Modulo4AACO', 543.34, 481.7, 3, ''),
     ('C_Modulo5', 36.54, 505.2, 3, ''),
     ('C_Modulo5AACO', 136.95, 505.2, 3, ''),
     ('C_Modulo6', 171.35, 505.2, 3, ''),
     ('C_Modulo6AACO', 271.75, 505.2, 3, ''),
     ('C_Modulo7', 306.15, 505.2, 3, ''),
     ('C_Modulo7AACO', 406.55, 505.2, 3, ''),
     ('C_Modulo8', 440.95, 505.2, 3, ''),
     ('C_Modulo8AACO', 543.34, 505.2, 3, ''),
     ('C_Modulo9', 36.54, 528.65, 3, ''),
     ('C_Modulo9AACO', 136.9, 528.65, 3, ''),
     ('C_Modulo10', 171.35, 528.65, 3, ''),
     ('C_Modulo10AACO', 271.75, 528.65, 3, ''),
     ('C_Modulo11', 306.15, 528.65, 3, ''),
     ('C_Modulo11AACO', 406.55, 528.65, 3, ''),
     ('C_Modulo12', 440.95, 528.65, 3, ''),
     ('C_Modulo12AACO', 543.34, 528.65, 3, ''),
     ('C_Modulo13', 36.54, 552.1, 3, ''),
     ('C_Modulo13AACO', 136.9, 552.1, 3, ''),
     ('C_Modulo14', 171.35, 552.1, 3, ''),
     ('C_Modulo14AACO', 271.75, 552.1, 3, ''),
     ('C_Modulo15', 306.15, 552.1, 3, ''),
     ('C_Modulo15AACO', 406.55, 552.1, 3, ''),
     ('C_Modulo16', 440.95, 552.1, 3, ''),
     ('C_Modulo16AACO', 543.34, 552.1, 3, ''),
     ('E_Ciudad', 332.64, 768.25, 7, ''),
     ('E_Dia', 436.54, 768.25, 7, ''),
     ('E_Mes', 488.59, 768.25, 7, ''),
     ('E_Anyo', 537.59, 768.25, 7, ''),
   ]

PDF_NOFIELDS_FITZ_COMPETENCY_VALIDATION = [ 
     ('A_Apellidos', 159.25, 88.97, 7, ''),
     ('A_Nombre', 408.84, 74.07, 7, ''),
     ('A_NIA', 304.6, 74.07, 7, ''),
     ('A_DNI', 202.05, 74.07, 7, ''),
     ('A_Direccion', 160.2, 106.37, 7, ''),
     ('A_Telefono', 156.2, 139.10, 7, ''),
     ('A_Poblacion', 267.7, 122.92, 7, ''),
     ('A_Provincia', 443.44, 122.9, 7, ''),
     ('A_CP', 176.2, 122.4, 7, ''),
     ('A_Mail', 350.7, 139.1, 7, ''),
     ('C_Docu1', 111.55, 441.15, 2, 'Off'),
     ('C_Modulo1', 34.59, 332.7, 3, ''),
     ('C_Modulo1UC', 139.95, 333.95, 3, ''),
     ('C_Modulo2', 218.45, 332.7, 3, ''),
     ('C_Modulo2UC', 323.85, 333.95, 3, ''),
     ('C_Modulo3', 402.34, 332.7, 3, ''),
     ('C_Modulo3UC', 505.75, 333.95, 3, ''),
     ('C_Modulo4', 34.56, 356.15, 3, ''),
     ('C_Modulo4UC', 139.95, 357.35, 3, ''),
     ('C_Modulo5', 218.44, 356.15, 3, ''),
     ('C_Modulo5UC', 323.85, 357.35, 3, ''),
     ('C_Modulo6', 402.35, 356.15, 3, ''),
     ('C_Modulo6UC', 505.75, 357.35, 3, ''),
     ('C_Modulo7', 34.56, 379.55, 3, ''),
     ('C_Modulo7UC', 139.95, 380.75, 3, ''),
     ('C_Modulo8', 218.44, 379.55, 3, ''),
     ('C_Modulo8UC', 323.85, 380.75, 3, ''),
     ('C_Modulo9', 402.35, 379.55, 3, ''),
     ('C_Modulo9UC', 505.75, 380.75, 3, ''),
     ('C_Modulo10', 34.56, 402.9, 3, ''),
     ('C_Modulo10UC', 139.95, 404.15, 3, ''),
     ('C_Modulo11', 218.44, 402.9, 3, ''),
     ('C_Modulo11UC', 323.85, 404.15, 3, ''),
     ('C_Modulo12', 402.35, 402.9, 3, ''),
     ('C_Modulo12UC', 505.75, 404.15, 3, ''),
     ('E_Ciudad', 292.84, 795, 7, ''),
     ('E_Dia', 396.75, 795, 7, ''),
     ('E_Mes', 437.4, 795, 7, ''),
     ('E_Any', 537.84, 795, 7, ''),
   ]