# Importamos la librería requests, que nos permite hacer peticiones HTTP fácilmente
import requests

# Para practicar usaremos una de tantas APIs públicas básicas.
# URL base de la API. A esta dirección le agregaremos los distintos endpoints.
BASE_URL = "https://jsonplaceholder.typicode.com/posts"


# Paso 1: Hacemos una petición GET para obtener todos los posts
def get_all_posts():
    print("\n[GET] Obtener todos los posts:")
    response = requests.get(BASE_URL)  # Hacemos una petición GET
    
    # Evaluamos que el código de estado sea el esperado (va a depender del método que estemos usando)
    if response.status_code == 200: 
        print("✅ Código de respuesta:", response.status_code)
        print("Contenido:")
        print(response.json()[:2])  # Mostrar los primeros 2
    else:
        print(f"❌ Error al obtener los posts (Código: {response.status_code})")

# Paso 2: Hacemos un GET específico para un post con ID = 1
def get_single_post(post_id):
    print(f"\n[GET] Obtener un solo post (id={post_id}):")
    response = requests.get(f"{BASE_URL}/{post_id}")
    
    if response.status_code == 200: 
        print("✅ Código de respuesta:", response.status_code)
        print("Respuesta:")
        print(response.json())
    else:
        print(f"❌ Error al obtener los posts (Código: {response.status_code})")
    
"""
Al ejecutar la función get_single_post() observamos que cada post, tiene distintos atributos, como:
userID, id, title, body
Los cuales podemos capturar individualmente
""" 

# Paso 3: Hacemos un GET con los atributos específicos para un post con ID = 1
def get_specific_attributes(post_id):
    print(f"\n[GET] Obtener atributos especificos para el post (id={post_id}):")
    response = requests.get(f"{BASE_URL}/{post_id}")
    
    if response.status_code == 200: 
        print("✅ Código de respuesta:", response.status_code)
        print("Respuesta:")
        post=response.json()
        print("User ID:", post['userId'])
        print("Post ID:", post['id'])
        print("Título:", post['title'])
        print("Contenido:", post['body'])
    else:
        print(f"❌ Error al obtener los posts (Código: {response.status_code})")
        
        



# Esta parte se ejecuta solo si corres el archivo directamente (no si lo importás)
if __name__ == "__main__":
    # Ejecutamos cada función una por una, como si fuera una guía práctica
    get_all_posts()
    get_single_post(1)
    get_specific_attributes(1)
