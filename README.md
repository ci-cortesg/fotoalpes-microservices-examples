# fotoalpes-microservices-examples - main

## Instalación

Si usted descargó la imagen de la máquina virtual para Virtual Box omita esta sección y pase a la sección Ejecución. Los servicios de este ejemplo requieren de *flask*, *redis*, *docker* y *docker-compose*. Se debe clonar este repositorio y, en caso de usar Linux Ubuntu ejecutar el archivo install.sh para instalar las librerías y los servicios. Después de ejecutar el archivo se debe reiniciar la máquina virtual. Si usa un sistema operativo distinto, debe instalar las librerías requeridas de manera manual.

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

Esta rama (main) muestra la comunicación entre servicios de manera asíncrona e implementa el patrón CQRS. Para la comunicación asíncrona se utiliza Redis como plataforma de mensajería.

El ejemplo implementa tres servicios:

#### Ordenes

Al implemetar el patrón CQRS las operaciones que expone este servicio se implementan en dos partes:   comandos (api_commands.py) y consultas (api_queries.py). En el archivo api_comands se tienen las siguientes operaciones:

- Crear una nueva orden: Esta operación se implementa en la función OrderListResource a través del método post.

Se puede observar que una vez creada la orden se coloca en la cola el id de la orden para que esta sea procesada.

```python
# add to queue to process order
q.enqueue(process_order, new_order.id)
```

En el archivo api_queries se tienen las siguientes operaciones:

- Listar todas las órdenes: Esta operación se implementa en la función OrderListResource a través del método get.
- Consultar una orden específica: Esta operación se implementa en la función OrderResource a través del método get.

#### Productos

Al implemetar el patrón CQRS las operaciones que expone este servicio se implementan en dos partes:   comandos (api_commands.py) y consultas (api_queries.py). En el archivo api_comands se tienen las siguientes operaciones:

- Crear un nuevo producto: Esta operación se implementa en la función ProductListResource a través del método post.
- Modificar un producto: Esta operación se implementa en la función ProductResource a través del método put.

En el archivo api_queries se tienen las siguientes operaciones:

- Listar todos los productos: Esta operación se implementa en la función ProductListResource a través del método get.
- Consultar un producto específico: Esta operación se implementa en la función ProductResource a través del método get.

#### Usuarios

Al implemetar el patrón CQRS las operaciones que expone este servicio se implementan en dos partes:   comandos (api_commands.py) y consultas (api_queries.py). En el archivo api_comands se tienen las siguientes operaciones:

- Crear un nuevo usuario: Esta operación se implementa en la función UserListResource a través del método post.

En el archivo api_queries se tienen las siguientes operaciones:

- Listar todos los usuarios: Esta operación se implementa en la función UserListResource a través del método get.
- Consultar un usuario específico: Esta operación se implementa en la función UserResource a través del método get.

#### API Gateway

En este ejemplo se utiliza la configuración proxy del servidor Ngnix para implementar el componente API Gateway. Esta configuración permite que todas las solicitudes se hagan al servidor Ngnix y este redireccione al servicio correspondiente de acuerdo a la operación y ruta especificada en el url, por ejemplo http://localhost/api-commands/users:

```
location /api-commands/users {
  proxy_pass http://users-commands:5000;
  proxy_set_header X-Real-IP  $remote_addr;
  proxy_set_header X-Forwarded-For $remote_addr;
  proxy_set_header Host $host;
}
location /api-commands/products {
  proxy_pass http://products-commands:5000;
  proxy_set_header X-Real-IP  $remote_addr;
  proxy_set_header X-Forwarded-For $remote_addr;
  proxy_set_header Host $host;
}
location /api-commands/orders {
  proxy_pass http://orders-commands:5000;
  proxy_set_header X-Real-IP  $remote_addr;
  proxy_set_header X-Forwarded-For $remote_addr;
  proxy_set_header Host $host;
}
location /api-queries/users {
  proxy_pass http://users-queries:5000;
  proxy_set_header X-Real-IP  $remote_addr;
  proxy_set_header X-Forwarded-For $remote_addr;
  proxy_set_header Host $host;
}
location /api-queries/products {
  proxy_pass http://products-queries:5000;
  proxy_set_header X-Real-IP  $remote_addr;
  proxy_set_header X-Forwarded-For $remote_addr;
  proxy_set_header Host $host;
}
location /api-queries/orders {
  proxy_pass http://orders-queries:5000;
  proxy_set_header X-Real-IP  $remote_addr;
  proxy_set_header X-Forwarded-For $remote_addr;
  proxy_set_header Host $host;
}
```

#### Comunicación asíncrona

En esta rama, cada servicio tene una copia de la estructura de la BD de los demás servicios por lo que se debe actualizar la información en cada BD cuando se hace una actualización en alguno de los servicios. Por lo anterior, cada servicio usa la cola de mensajería para notificar a los demás los cambios realizados en su respectiva BD o para actualizar la BD con los cambios realizados por los otros servicios. A continuación se muestra el esquema descrito anteriormente para el servicio Productos:

###### Notificar cambios

En el archivo api_commands.py, el cual implementa las operaciones de creación y actualización de productos, se publica en la cola el id del producto creado o modificado para que los demás servicios actualicen su respectiva BD.

```python
#Publicación en la cola en la creación de un producto
def post(self):
    ...
	q.enqueue(send_product, product_schema.dump(new_product))
#Publicación en la cola en la creación de un producto
def put(self):
    ...
	q.enqueue(put_product, product_schema.dump(product))
```

El archivo sender.py publica en la cola el id de un nuevo producto. El archivo putter.py publica en la cola el id del producto modificado.

###### Actualizar cambios

Para el ejemplo, la actualización de un producto se realiza por parte del servicio de órdenes, el cual modifica la cantidad en stock del producto. Por lo anterior, el archivo updater.py implementa la actualización del producto cuyo id publica el servicio de órdenes en la cola. En la carpeta ordenes, en el archivo base.py se define la función process_order la cual verifica que el producto sea válido y si es así cambia el estado de la orden y publica en la cola el id del producto incluído en la orden.

```python
def process_order(order_id):
	...
	q2.enqueue(update_product, {
		'id': product.id,
		'quantity': order.quantity
	})
```
