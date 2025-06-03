# Importamos la librería requests, que nos permite hacer peticiones HTTP fácilmente
import requests

# Para practicar usaremos una de tantas APIs públicas básicas.
# URL base de la API. A esta dirección le agregaremos los distintos endpoints.
BASE_URL = "https://jsonplaceholder.typicode.com/posts"

#                       METODO GET
# Hacemos una petición GET para obtener todos los posts
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

# Hacemos un GET específico para un post con ID = 1
def get_single_post(post_id):
    print(f"\n[GET] Obtener un solo post (id={post_id}):")
    response = requests.get(f"{BASE_URL}/{post_id}")
    
    # Evaluamos que el código de estado sea el esperado (va a depender del método que estemos usando)
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

# Hacemos un GET con los atributos específicos para un post con ID = 1
def get_specific_attributes(post_id):
    print(f"\n[GET] Obtener atributos especificos para el post (id={post_id}):")
    response = requests.get(f"{BASE_URL}/{post_id}")
    
    # Evaluamos que el código de estado sea el esperado (va a depender del método que estemos usando)
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
        
#                   METODO POST
# Paso 4: Enviamos un POST para "crear" un nuevo post
def create_post():
    print("\n[POST] Crear un nuevo post:")
    new_post = {
        "title": "Mi primer post",
        "body": "Contenido del post de prueba",
        "userId": 1
    }
    # Enviamos la petición con el JSON
    response = requests.post(BASE_URL, json=new_post)
    
    # Evaluamos que el código de estado sea el esperado (va a depender del método que estemos usando)
    if response.status_code==201:
        print("Código de respuesta:", response.status_code)
        print("Post creado (respuesta simulada):")
        print(response.json())
    else:
        print(f"❌ Error al crear el post posts (Código: {response.status_code})")


#               METODO PUT
# Usamos PUT para actualizar completamente un post existente
def update_post(post_id):
    print(f"\n[PUT] Actualizar completamente el post con id={post_id}:")
    updated_post = {
        "id": post_id,
        "title": "Título actualizado",
        "body": "Contenido nuevo del post",
        "userId": 1
    }
    response = requests.put(f"{BASE_URL}/{post_id}", json=updated_post)
    
    # Evaluamos que el código de estado sea el esperado (va a depender del método que estemos usando)
    if response.status_code== 200:
        print("Código de respuesta:", response.status_code)
        print("Respuesta de la API:")
        print(response.json())
    else:
        print(f"❌ Error al actualizar el post posts (Código: {response.status_code})")

#               METODO PATCH
# Paso 6: Usamos PATCH para modificar solo una parte del post
def patch_post(post_id):
    print(f"\n[PATCH] Modificar parcialmente el post con id={post_id}:")
    partial_update = {
        "title": "Título modificado con PATCH"
    }
    response = requests.patch(f"{BASE_URL}/{post_id}", json=partial_update)
    
    # Evaluamos que el código de estado sea el esperado (va a depender del método que estemos usando)
    if response.status_code==200:
        print("Código de respuesta:", response.status_code)
        print("Respuesta:")
        print(response.json())
    else:
        print(f"❌ Error al crear el actualizar posts (Código: {response.status_code})")

#                   METODO DELETE
# Usamos DELETE para "eliminar" el post (aunque no se elimina realmente en esta API)
def delete_post(post_id):
    print(f"\n[DELETE] Eliminar el post con id={post_id}:")
    response = requests.delete(f"{BASE_URL}/{post_id}")
    
    # Evaluamos que el código de estado sea el esperado (va a depender del método que estemos usando)
    if response.status_code==200:
        print("Código de respuesta:", response.status_code)
        print("Contenido eliminado")
    else:
        print("No se pudo eliminar")


if __name__ == "__main__":
    # Ejecutamos cada función una por una, como si fuera una guía práctica
    get_all_posts()
    get_single_post(1)
    get_specific_attributes(1)
    create_post()
    update_post(1)
    patch_post(1)
    delete_post(1)
