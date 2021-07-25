# fotoalpes-microservices-examples - sync

## Instalación

Los servicios de este ejemplo requieren de *docker* y *docker-compose*. Se debe ejecutar el archivo install.sh para instalar las librerías y los servicios. Después de ejecutar el archivo se debe reiniciar la máquina virtual.

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

Esta rama (sync) muestra la comunicación entre servicios de manera síncrona. El ejemplo implementa tres servicios:

#### Ordenes

Este servicio expone tres operaciones:

- Listar todas las órdenes: OrderListResource - get
- Crear una nueva orden: OrderListResource - post
- Consultar una orden específica: OrderResource - get

Se puede observar que la operación que crea una nueva orden valida que el producto y el usuario sean válidos. Para esto, utiliza las operaciones de consulta expuestas por los servicios Usuarios y Productos de manera síncrona.

```python
user = requests.get(f"http://users:5000/users/{request.json['user']}")
product = requests.get(f"http://products:5000/products/{request.json['product']}")
```

#### Productos

Este servicio expone cuatro operaciones:

- Listar todos los productos: ProductListResource - get
- Crear un nuevo producto: ProductListResource - post
- Consultar un producto específico: ProductResource - get
- Modificar un producto: ProductResource - put

#### Usuarios

Este servicio expone tres operaciones:

- Listar todos los usuarios: UserListResource - get
- Crear un nuevo usuario: UserListResource - post
- Consultar un usuario específico: UserResource - get

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

