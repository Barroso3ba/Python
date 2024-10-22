"""
Enunciado 3️⃣
Estás leyendo un libro 📖 de 300 páginas y te has propuesto leer un cierto número de páginas
cada día. Crea un programa que te permita registrar cuántas páginas lees cada día 
y te avise cuando hayas terminado el libro. 😁"""
paginas=300
dias=0
print("Control de Lectura de Libros.....📕📖📕")
while (paginas>0):
    paginas_leidas=int(input("Ingresa la Cantidad de paginas 📖 leidas hoy: "))
    paginas-=paginas_leidas
    dias+=1
    print(f'Faltan por leer {paginas} paginas 👍')
print(f"Felicitaciones has alcanzado leer un libro 📕 de 300 paginas 🎉🎉 en {dias} dias")