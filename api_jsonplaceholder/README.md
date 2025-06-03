# 🧪 Practicando métodos HTTP con JSONPlaceholder

Estos días estuve practicando cómo hacer peticiones HTTP desde Python usando la librería `requests`. Para eso me apoyé en [JSONPlaceholder](https://jsonplaceholder.typicode.com), una API falsa que simula el comportamiento de una real. Me pareció ideal para probar sin romper nada.

El objetivo principal es practicar los métodos HTTP que usamos todo el tiempo en desarrollo web:
`GET`, `POST`, `PUT`, `PATCH` y `DELETE`.

---

## Métodos HTTP que estoy explorando

### 🔹 GET

Este método se usa para **consultar información**. No modifica nada en el servidor, solo pide datos.

Por ejemplo, podría usarse para obtener un listado de usuarios, los detalles de un producto, o los comentarios de un artículo.

- **Uso típico:** leer información.
- **Respuesta esperada:** `200 OK` si todo salió bien.

---

### 🔹 POST

Con `POST` se **envían datos al servidor para crear algo nuevo**. Es como decir: “esto es algo nuevo, guardalo”.

Se usa mucho para registrar usuarios, cargar formularios, subir comentarios, etc.

- **Uso típico:** crear un recurso nuevo.
- **Respuesta esperada:** `201 Created` si se creó correctamente.

---

### 🔹 PUT

El método `PUT` se usa para **actualizar un recurso existente de forma completa**. Es decir, reemplaza toda la información de ese recurso.

Imaginá que tenés los datos de un producto y querés reemplazarlos por completo con nuevos valores.

- **Uso típico:** actualizar todo un recurso.
- **Respuesta esperada:** `200 OK` o `204 No Content`.

---

### 🔹 PATCH

Similar a `PUT`, pero más específico. `PATCH` sirve para **modificar una parte del recurso**, sin necesidad de enviar toda la información.

Ideal para hacer cambios puntuales, como actualizar solo el correo electrónico de un usuario o cambiar el estado de una tarea.

- **Uso típico:** actualizar parcialmente.
- **Respuesta esperada:** `200 OK` o `204 No Content`.

---

### 🔹 DELETE

Este método le indica al servidor que **elimine un recurso**. Es definitivo y no requiere enviar datos complejos, solo la identificación del elemento a borrar.

Puede usarse, por ejemplo, para eliminar una cuenta, borrar un archivo, o eliminar un comentario.

- **Uso típico:** borrar un recurso.
- **Respuesta esperada:** `200 OK`, `202 Accepted` o `204 No Content`.

---

## Códigos de estado

Es importante evaluar siempre el `status_code` de cada respuesta para entender cómo salió la petición.  
Algunos códigos comunes:

| Código | Significado                                                  |
| ------ | ------------------------------------------------------------ |
| 200    | OK — Todo salió bien                                         |
| 201    | Created — Se creó correctamente                              |
| 204    | No Content — Sin errores, pero no hay contenido para mostrar |
| 400    | Bad Request — Petición mal formulada                         |
| 401    | Unauthorized — Falta autenticación                           |
| 404    | Not Found — Recurso no encontrado                            |
| 500    | Internal Server Error — Fallo del servidor                   |

---

## Cómo lo estoy probando

Escribí un archivo en Python con funciones separadas para cada método.  
Ejecuto el script desde la terminal con:

```
python api_jsonplaceholder.py
```
