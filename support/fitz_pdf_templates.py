# -*- coding: utf-8 -*-

# Cuando no se encuentran los fields (por ejempl, Adobe los elimina al firmar el documento)
# se utiliza pyMuPDF para poder "leer" el pdf y extraer la información
# NOTA: es preferible que lso datos estén en fields, 
# este recurso solo debe ser utilizado si no queda otra opción
# Para ello se necesita una plantilla que indique en que posición está el valor

# La estructura de la plantilla es:
# clave, xmin, ymin, tipo (ver funcion inttype2string), valor por defecto 
PDF_NOFIELDS_FITZ_VALIDATION = [ 
    ('A_Apellidos', 35.3, 103, 7, ''),
    ('A_Nombre', 291.1, 103, 7, ''),
    ('A_NIA', 407, 103, 7, ''),
    ('A_DNI', 492.1, 103, 7, ''),
    ('A_Direccion', 35.5, 125, 7, ''),
    ('A_Telefono', 452.3, 124, 7, ''),
    ('A_Poblacion', 35.6, 147.2, 7, ''),
    ('A_Provincia', 262.7, 1472, 7, ''),
    ('A_CP', 475.0, 147.2, 7, ''),
    ('B_Requisito1', 44.3, 257.6, 2, 'Off'),
    ('B_Requisito2', 44.7, 291.5, 2, 'Off'),
    ('B_Requisito3', 44.35, 323.65, 2, 'Off'),
    ('B_Requisito4', 44.34, 340.6, 2, 'Off'),
    ('B_Requisito5', 44.35, 357.55, 2, 'Off'),
    ('C_Docu1', 44.3, 560.95, 2, 'Off'),
    ('C_Docu2', 44.7, 571.75, 2, 'Off'),
    ('C_Docu3', 44.29, 599.9, 2, 'Off'),
    ('C_Docu4', 44.7, 609.0, 2, 'Off'),
    ('C_Docu5', 44.15, 627.5, 2, 'Off'),
    ('C_Modulo1', 34.55, 453.76, 3, ''),
    ('C_Modulo1AACO', 134.97, 453.75, 3, ''),
    ('C_Modulo2', 169.34, 453.7, 3, ''),
    ('C_Modulo2AACO', 269.75, 453.5, 3, ''),
    ('C_Modulo3', 304.14, 453.55, 3, ''),
    ('C_Modulo3AACO', 404.54, 453.52, 3, ''),
    ('C_Modulo4', 438.9, 453.7, 3, ''),
    ('C_Modulo4AACO', 541.34, 453.5, 3, ''),
    ('C_Modulo5', 34.54, 477, 3, ''),
    ('C_Modulo5AACO', 134.9, 477, 3, ''),
    ('C_Modulo6', 169.34, 477, 3, ''),
    ('C_Modulo6AACO', 269.75, 477, 3, ''),
    ('C_Modulo7', 304.14, 477, 3, ''),
    ('C_Modulo7AACO', 404.54, 477, 3, ''),
    ('C_Modulo8', 438.9, 477, 3, ''),
    ('C_Modulo8AACO', 541.34, 477, 3, ''),
    ('C_Modulo9', 34.55,  500.45, 3, ''),
    ('C_Modulo9AACO', 134.97, 500.45, 3, ''),
    ('C_Modulo10', 169.34, 500.45, 3, ''),
    ('C_Modulo10AACO', 269.75, 500.45, 3, ''),
    ('C_Modulo11', 304.14, 500.45, 3, ''),
    ('C_Modulo11AACO', 404.54, 500.45, 3, ''),
    ('C_Modulo12', 438.9, 500.45, 3, ''),
    ('C_Modulo12AACO', 541.34, 500.45, 3, ''),
    ('C_Modulo13', 34.54, 523, 3, ''),
    ('C_Modulo13AACO', 134.9, 523, 3, ''),
    ('C_Modulo14', 169.34, 523, 3, ''),
    ('C_Modulo14AACO', 269.75, 523, 3, ''),
    ('C_Modulo15', 304.14, 523, 3, ''),
    ('C_Modulo15AACO', 404.54, 523, 3, ''),
    ('C_Modulo16', 438.9, 523, 3, ''),
    ('C_Modulo16AACO', 541.34, 523, 3, ''),
    ('C_Ciudad', 139.54, 652, 7, ''),
    ('C_Dia', 194.44, 651.85, 7, ''),
    ('C_Mes', 242.29, 651.85, 7, ''),
    ('C_Anyo', 313.4, 651.35, 7, ''),
    ]