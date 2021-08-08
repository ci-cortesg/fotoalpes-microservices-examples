# fotoalpes-microservices-examples - sync

## Instalación

Los servicios de este ejemplo requieren de *flask*, *redis*, *docker* y *docker-compose*. Se debe clonar este repositorio y, en caso de usar Linux Ubuntu ejecutar el archivo install.sh para instalar las librerías y los servicios. Después de ejecutar el archivo se debe reiniciar la máquina virtual. Si usa un sistema operativo distinto, debe instalar las librerías requeridas de manera manual.

```
sh install.sh
```

## Ejecución

Para correr la aplicación se debe ejecutar el siguiente comando:


```
docker-compose up
```

O si prefiere correr la aplicación en background se debe ejecutar el siguiente comando:

```
docker-compose up -d
```



## Descripción de los servicios

Esta rama (sync-sec) muestra la comunicación entre servicios de manera síncrona. Para la seguridad se utiliza un certificado SSL para asegurar la comunicación entre los servicios y se implementa un componente encargado de la gestión de tokens para autenticar el llamado de los servicios expuestos. El ejemplo implementa cuatro componentes:

#### Ordenes

Este servicio expone tres operaciones, lasd cuales se encuentran definidas en el archivo api.py:

- Listar todas las órdenes: Esta operación se implementa en la función OrderListResource a través del método get.
- Crear una nueva orden: Esta operación se implementa en la función OrderListResource a través del método post.
- Consultar una orden específica: Esta operación se implementa en la función OrderResource a través del método get.

Se puede observar que la operación que crea una nueva orden valida que el producto y el usuario sean válidos. Para esto, utiliza las operaciones de consulta expuestas por los servicios Usuarios y Productos de manera síncrona.

```python
user = requests.get(f"http://users:5000/users/{request.json['user']}")
product = requests.get(f"http://products:5000/products/{request.json['product']}")
```

#### Productos

Este servicio expone cuatro operaciones:

- Listar todos los productos: Esta operación se implementa en la función ProductListResource a través del método get.
- Crear un nuevo producto: Esta operación se implementa en la función ProductListResource a través del método post.
- Consultar un producto específico: Esta operación se implementa en la función ProductResource a través del método get.
- Modificar un producto: Esta operación se implementa en la función ProductResource a través del método put.

#### Usuarios

Este servicio expone tres operaciones:

- Listar todos los usuarios: Esta operación se implementa en la función UserListResource a través del método get.
- Crear un nuevo usuario: Esta operación se implementa en la función UserListResource a través del método post.
- Consultar un usuario específico: Esta operación se implementa en la función UserResource a través del método get.

#### Jwt

Este servicio expone una sola operación:

- Crear token: Esta operación se implementa en la función AuthResource a través del método get, la cual retorna un token el cual se debe incluir en el llamado de cualquiera de los otros servicios descritos anteriormente. Se puede observar que antes de la definición de cada función en todos los servicios, se especifica una instrucción (@jwt_required) que obliga a la validación del token generado por la operación Crear token:

```python
class OrderListResource(Resource):
    @jwt_required()
    def get(self):
```

#### API Gateway

En este ejemplo se utiliza la configuración proxy del servidor Ngnix para implementar el componente API Gateway. Este configuración permite que todas las solicitudes se hagan al servidor Ngnix y este redireccione al servicio correspondiente de acuerdo a la ruta especificada en el url, por ejemplo http://localhost/users:

```
location /users {
  proxy_pass http://users:5000;
  proxy_set_header X-Real-IP  $remote_addr;
  proxy_set_header X-Forwarded-For $remote_addr;
  proxy_set_header Host $host;
}
location /products {
  proxy_pass http://products:5000;
  proxy_set_header X-Real-IP  $remote_addr;
  proxy_set_header X-Forwarded-For $remote_addr;
  proxy_set_header Host $host;
}
location /orders {
  proxy_pass http://orders:5000;
  proxy_set_header X-Real-IP  $remote_addr;
  proxy_set_header X-Forwarded-For $remote_addr;
  proxy_set_header Host $host;
}
```
Adicionalmente se configura el servidor Ngnix para utilizar un certificado SSL autogenerado para cifrar la información que fluye entre los servicios y entre el usuario y el servidor Nginx, por lo que ahora se utiliza el protocolo https a diferencia de la rama sync en donde se utiliza el protocolo http.
