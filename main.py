traduccion={
    "ALA LAU": "Hace frío o está frío",
    "PALTA": "Fruta que tambien lleva el nombre de aguacate en algunos países",
    "JUICIOSO": "Una persona responsable",
    "ESFERO":"También conocido como bolígrafo o lapicero"
}
word = input("Escribe una palabra que no entiendas (¡con mayúsculas!): ")
if word in traduccion.keys():
    print("El significado de la palabra seleccionada es: ",traduccion[word])
else:
    print("Esas palabras no están en nuestro diccionario")
