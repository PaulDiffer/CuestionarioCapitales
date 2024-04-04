capitals = {
    "Argentina": "Buenos Aires",
    "México": "Ciudad de México",
    "Colombia": "Bogotá",
    "Perú": "Lima",
    "Chile": "Santiago",
    "España": "Madrid"
}

def cuestionario_capitales():
    print("Bienvenido al cuestionario de capitales del mundo!")
    score = 0
    
    for country, capital in capitals.items():
        
        print(f"Pregunta: ¿Cual es la capital de {country}? ")
        user_answer = input("Tu respuesta: ")
        
        if user_answer.lower() == capital.lower():
            print("Correcto. Has ganado un punto")
            score += 1
        else:
            print(f"Respuesta incorrecta. La capital de {country} es {capital}.\n")
    print(f"Tu puntuación es: {score}/{len(capitals)}")
    
cuestionario_capitales()
