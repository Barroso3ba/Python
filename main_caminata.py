"""
Enunciado 1️⃣
Un entrenador personal te ha sugerido caminar 10,000 pasos al día 🚶🏽♂️. 
Cada hora, puedes registrar cuántos pasos diste 👣.  
Escribe un programa que permita registrar tus pasos cada hora ⌚
y calcule el total de pasos dados al final del día. """
total_pasos=0
hora=0
pasos=0
# verificamos en el bucle que se cumplan los 10.000 pasos y final del dia 24 horas
while (total_pasos<10000)and(hora<24):
    hora+=1
    pasos=int(input(f'Ingresa la cantidad de pasos 🚶‍♂️ dados en la {hora} ⌚  hora:'))
    total_pasos=total_pasos+pasos
print(f'El total de pasos 🚶‍♂️ dados en ⌚ {hora} horas es de {total_pasos} 🥳 felicitaciones')
    

"""
Enunciado 2️⃣
Estás usando tu teléfono 📱 y la batería comienza a agotarse. 
El teléfono tiene una batería inicial del 100%, y cada acción que realizas
(ver un video, jugar, etc.) consume un porcentaje de batería. 
Crea un programa que simule la reducción de batería hasta que llegue a 0 o menos.
"""

"""
Enunciado 3️⃣
Estás leyendo un libro 📖 de 300 páginas y te has propuesto leer un cierto número de páginas
cada día. Crea un programa que te permita registrar cuántas páginas lees cada día 
y te avise cuando hayas terminado el libro. 😁"""