"""
Enunciado 2️⃣
Estás usando tu teléfono 📱 y la batería comienza a agotarse. 
El teléfono tiene una batería inicial del 100%, y cada acción que realizas
(ver un video, jugar, etc.) consume un porcentaje de batería. 
Crea un programa que simule la reducción de batería hasta que llegue a 0 o menos.
"""
bateria=100
consumo=0
while (bateria>0):
    accion=input("Ingresa la acciòn que ejecutada en el telefono: 📲 (video 📹,jugar 🎮,wsp ,llamada 📞,instagram) :")
    if accion.upper() == "VIDEO":
        consumo=20
    elif accion.upper() == "JUGAR":
        cosumo=45
    elif accion.upper() == "WSP":
        consumo=35
    elif accion.upper() == "LLAMADA":
        consumo=15
    elif accion.upper() == "INSTAGRAM":
        consumo=40
    else:
        consumo=5
    bateria-=consumo
    print((bateria)*"🔋"+ str(bateria) + "%")
print(f"🔋 BATERIA AGOTADA CON {bateria} %")