# fotoalpes-microservices-examples

## Instalación

El ejemplo del caso Foto Alpes es un proyecto en Flask que implementa microservicios y las tácticas vistas en el curso Arquitecturas ágiles de software. El presente repositorio contiene el código del ejemplo en diferentes ramas de acuerdo a los temas vistos. Las ramas del proyecto son:

- main: Rama que implementa CQRS y comunicación asíncrona
- sync: Rama que implementa comunicación síncrona
- sync-sec: Rama que implementa el uso de tokens y certificados de seguridad con  comunicación síncrona
- async-sec: Rama que implementa el uso de tokens y certificados de seguridad con  comunicación asíncrona

Para ejecutar el proyecto localmente, es necesario instalar [Oracle VirtualBox](https://www.virtualbox.org/wiki/Downloads) en su pc. Una vez instalado, se debe descargar la imagen de la máquina virtual ([MISW4202-FotoAlpes-Microservicios.zip](https://uniandes-my.sharepoint.com/:u:/g/personal/ci_cortesg_uniandes_edu_co/EQMbaoWx1yZOl5cMyrQ-8rgBqzCjd4HWqfLmfYs1vbWFZQ?e=16NHt7)) e importarla en Virtualbox. Para importar la imagen se deben seguir los siguientes pasos:

1. Descargar el archivo MISW4202-FotoAlpes-Microservicios.zip

2. Descomprimir el archivo descargado en el paso anterior

3. Abrir Oracle Virtualbox e ir al menú Máquina --> Añadir

   <img src="https://github.com/ci-cortesg/fotoalpes-microservices-examples/blob/main/img/Agregar_VM.png" alt="Agregar_VM" style="zoom:75%;" />

4. Ubicar la carpeta donde se descomprimió el archivo zip y seleccionar el archivo MISW4202-FotoAlpes-Microservicios-New.ovdx

   <img src="https://github.com/ci-cortesg/fotoalpes-microservices-examples/blob/main/img/Seleccionar_Archivo_VM.png" alt="Seleccionar_Archivo_VM" style="zoom:75%;" />

5. En el menú izquierdo debe aparecer la máquina con el nombre del archivo seleccionado

6. Dar clic en el botón Configuración en la parte superior

7. En el menú izquierdo dar clic sobre la opción Sistema

8. En la opción Chipset seleccionar la opción ICH9

   <img src="https://github.com/ci-cortesg/fotoalpes-microservices-examples/blob/main/img/Change_Chipset_CH9.png" alt="Change_Chipset_CH9" style="zoom:75%;" />
   
9. En el menú izquierdo dar clic sobre la opción USB y desmarcar la opción "Habilitar Controlador USB"

   <img src="https://github.com/ci-cortesg/fotoalpes-microservices-examples/blob/main/img/Disable_USB.png" alt="Disable_USB" style="zoom:75%;" />
   
10. Dar clic en el botón Aceptar en la parte inferior derecha

11. Dar clic de nuevo en el botón Configuración en la parte superior

12. En el menú izquierdo dar clic otra vez sobre la opción Sistema

13. En la opción Chipset seleccionar la opción PIIX3

   <img src="https://github.com/ci-cortesg/fotoalpes-microservices-examples/blob/main/img/Change_Chipset_PIIX3.png" alt="Change_Chipset_PIIX3" style="zoom:75%;" />

14. Dar clic en el botón Aceptar en la parte inferior derecha

15. Dar clic en el botón Iniciar ubicado en la parte superior

   <img src="https://github.com/ci-cortesg/fotoalpes-microservices-examples/blob/main/img/Iniciar_VM.png" alt="Iniciar_VM" style="zoom:75%;" />

16. Una vez la máquina termine de cargar, debe visualizar la pantalla de inicio

   <img src="https://github.com/ci-cortesg/fotoalpes-microservices-examples/blob/main/img/Pantalla_Inicio_VM.png" alt="Pantalla_Inicio_VM" style="zoom:75%;" />

17. Ingresar con el usuario **estudiante** y la contraseña **Estudiante2021**

18. Ejecutar el siguiente comando:

   ```
   ifconfig
   ```

19. Tomar nota de la dirección ip que se despliega en pantalla, como aparece en la siguiente imagen:

    <img src="https://github.com/ci-cortesg/fotoalpes-microservices-examples/blob/main/img/Direccion_IP_VM.png" alt="Direccion_IP_VM" style="zoom:75%;" />

20. La dirección IP obtenida en el paso anterior corresponde a la dirección asociada al adaptador de red de la máquina virtual. Tome nota de esta dirección porque se utilizará para acceder a los servicios desde su pc local

21. Ubíquese en el directorio fotoalpes-microservices-examples ejecutando el siguiente comando:

    ```
    cd fotoalpes-microservices-examples
    ```

22. Para ejecutar los servicios, corra el siguiente comando:

    ```
    sudo docker-compose up
    ```

## Pruebas

Una vez los servicios se estén ejecutando podemos hacer pruebas de las funciones expuestas por estos. El ejemplo no implementa una interfaz de usuario por lo que debemos utilizar un programa que permita consumir servicios REST. Se sugiere utilizar [Postman](https://www.postman.com/downloads/) para ejecutar los servicios del ejemplo, por lo que debe descargarlo haciendo clic sobre el enlace anterior.

Una vez haya descargado e instalado Postman, ejecute este programa y deshabilite la opción de verificación del certificado SSL. Para esto, siga los siguientes pasos:

1. Haga clic en el menú File --> Settings

2. Se despliega una ventana con las opciones de configuración

3. Deslice el botón SSL certification verification a la opción Off como se ve en la siguiente imagen.

   <img src="https://github.com/ci-cortesg/fotoalpes-microservices-examples/blob/main/img/Postman_Settings.png" alt="Crear_Coleccion" style="zoom:75%;" />

Para consumir alguno de los servicios implementados en el presente ejemplo, siga los siguientes pasos:

1. Haga clic en el botón New

2. Seleccione la opción Collection

3. En el campo Name ingrese el nombre para el conjunto de pruebas o servicios, por ejemplo Ejemplo FotoAlpes. Luego haga clic en el botón Create

   <img src="https://github.com/ci-cortesg/fotoalpes-microservices-examples/blob/main/img/Crear_Coleccion.png" alt="Crear_Coleccion" style="zoom:75%;" />

4. Nuevamente haga clic en el botón New

5. Seleccione la opción Request

6. En el campo Request name ingrese un nombre para la prueba a ejecutar, por ejemplo listar usuarios

7. En el campo Select a collection or folder to save escriba el nombre de la colección que definió en el paso 3 y seleccione la opción que aparece en el cuadro de abajo

8. Haga clic el el botón Save to ....

   <img src="https://github.com/ci-cortesg/fotoalpes-microservices-examples/blob/main/img/Crear_Request.png" alt="Crear_Request" style="zoom:75%;" />

9. Dependiendo del servicio a probar seleccione el método requerido. Para las operaciones de consulta, el método es Get. Para las operaciones de creación el método es Post y para las operaciones de modificación el método es Put. El ejemplo no implementa ningún otro tipo de operaciones.

10. Ingrese el url del servicio y la operación a probar. Por ejemplo, para el caso de listar los usuarios, en la rama main, el url sería el siguiente: http://XXX.XXX.XXX.XXX/api-queries/users. Reemplace XXX.XXX.XXX.XXX por la dirección IP de la máquina virtual obtenida en el paso 19 de la sección **Instalación**.

11. Haga clic en el botón Send

12. En la opción Body de la respuesta recibida se puede ver la información que retorna el servicio

    <img src="https://github.com/ci-cortesg/fotoalpes-microservices-examples/blob/main/img/Listar_Usuarios.png" alt="Listar_Usuarios" style="zoom:75%;" />


Para el caso de las operaciones que usan los métodos Post y Put se debe especificar la información requerida por el servicio. Esta información se debe definir en formato Json en la opción Body del Request. La siguiente imagen muestra la definición de los datos para crear un nuevo usuario:

<img src="https://github.com/ci-cortesg/fotoalpes-microservices-examples/blob/main/img/Crear_Usuario.png" alt="Postman_Settings" style="zoom:75%;" />

## Pruebas para las ramas de seguridad

Para los servicios de las ramas sync-sec y async-sec se deben tener en cuenta lo siguiente:

Antes de consumir cualquiera de los servcios implementados, es obligatorio obtener el token de seguridad del componente jwt. Para esto, ejecute los pasos 1 a 11 descritos anteriormente y en el paso 10 especifique el siguiente url: https://XXX.XXX.XXX.XXX/api-queries/jwt. Reemplace XXX.XXX.XXX.XXX por la dirección IP de la máquina virtual obtenida en el paso 19 de la sección Instalación.

<img src="https://github.com/ci-cortesg/fotoalpes-microservices-examples/blob/main/img/Get_Jwt_Token.png" alt="Get_Jwt_Token" style="zoom:75%;" />

Todos los servicios implementados esperan un token en el header de la solicitud, por lo que se debe incluir el token obtenido del componente jwt. Para incluir el token en la solicitud, siga los siguientes pasos 1 a 10 descritos anteriormente y antes de ejecutar el paso 11 haga clic en la opción Headers e incluya una nueva opción llamada Authorization y en la columna ubicada al frente incluya el token obtenido del componente jwt antecedido de la palabra Bearer más un espacio en blanco como se se muestra en la siguiente imagen:

<img src="https://github.com/ci-cortesg/fotoalpes-microservices-examples/blob/main/img/Include_Token.png" alt="Include_Token" style="zoom:75%;" />

## Descripción de los parámetros para las pruebas 

A contiuación se describen los parámetros requeridos por cada servicio, los cuales deben ser tenidos en cuenta al momento de realizar las pruebas, como se mencionó en la sección anterior:

##### Ordenes

Este servicio expone tres operaciones, las cuales se exponen de la siguiente manera para las ramas sync y sync-sec (reemplazar http por https):

- Listar todas las órdenes: El url para consumir este servicio, a través de una operación Get, es como sigue: http://XXX.XXX.XXX.XXX:5000/orders y no requiere de ningún parámetro adicional.
- Crear una nueva orden:  El url para consumir este servicio, a través de una operación Post, es como sigue: http://XXX.XXX.XXX.XXX:5000/orders y se debe especificar en el Body del request la información de la nueva orden. El formato para la información de la nueva orden es un JSON similar al que sigue (los atributos user y producto se deben definir con el id de un usuario y un producto creados previamente):
```json
{
    "user":1,
    "product":1,
    "quantity":10
}
```
- Consultar una orden específica: El url para consumir este servicio, a través de una operación Get, es como sigue: http://XXX.XXX.XXX.XXX:5000/orders/<<id-orden>>, donde <<id-orden>> representa el id de la orden a consultar.

Para las ramas async y async-sec (reemplazar http por https), al implemetar el patrón CQRS las operaciones que expone este servicio se exponen en dos partes: comandos y consultas:

- Listar todas las órdenes: El url para consumir este servicio, a través de una operación Get, es como sigue: http://XXX.XXX.XXX.XXX:5000/api-queries/orders y no requiere de ningún parámetro adicional.
- Crear una nueva orden:  El url para consumir este servicio, a  través de una operación Post, es como sigue: http://XXX.XXX.XXX.XXX:5000/api-commands/orders y se debe especificar en el Body del request la información de la nueva orden. El formato para la información de la nueva orden es un JSON similar al que sigue:
```json
{
    "user":1,
    "product":1,
    "quantity":10
}
```
- Consultar una orden específica: El url para consumir este servicio, através de una operación Get, es como sigue: http://XXX.XXX.XXX.XXX:5000/api-queries/orders/<<id-orden>>, donde <<id-orden>> representa el id de la orden a consultar.

##### Productos

Este servicio expone cuatro operaciones, las cuales se exponen de la siguiente manera para las ramas sync y sync-sec (reemplazar http por https):

- Listar todos los productos: El url para consumir este servicio, a través de una operación Get, es como sigue: http://XXX.XXX.XXX.XXX:5000/products y no requiere de ningún parámetro adicional.
- Crear un nuevo producto: El url para consumir este servicio, a través de una operación Post, es como sigue: http://XXX.XXX.XXX.XXX:5000/products y se debe especificar en el Body del request la información del nuevo producto. El formato para la información del nuevo producto es un JSON similar al que sigue:
```json
{
    "name":"Nombre del producto",
    "description":"Descripción del producto",
    "value":0,
    "stock":0
}
```
- Consultar un producto específico: El url para consumir este servicio, a través de una operación Get, es como sigue: http://XXX.XXX.XXX.XXX:5000/products/<<id-producto>>, donde <<id-producto>> representa el id del producto a consultar.
- Modificar un producto: El url para consumir este servicio, a través de una operación Put, es como sigue: http://XXX.XXX.XXX.XXX:5000/products/<<id-producto>>, donde <<id-producto>> corresponde al id del producto a modificar, y se debe especificar en el Body del request la información nueva información del producto. El formato para la información del producto es un JSON similar al que sigue:
```json
{
    "name":"Nombre del producto",
    "description":"Descripción del producto",
    "value":0,
    "stock":0
}
```
Para las ramas async y async-sec (reemplazar http por https), al implemetar el patrón CQRS las operaciones que expone este servicio se exponen en dos partes: comandos y consultas:

- Listar todos los productos: El url para consumir este servicio, a través de una operación Get, es como sigue: http://XXX.XXX.XXX.XXX:5000/api-queries/products y no requiere de ningún parámetro adicional.
- Crear un nuevo producto: El url para consumir este servicio, a través de una operación Post, es como sigue: http://XXX.XXX.XXX.XXX:5000/api-commands/products y se debe especificar en el Body del request la información del nuevo producto. El formato para la información del nuevo producto es un JSON similar al que sigue:
```json
{
    "name":"Nombre del producto",
    "description":"Descripción del producto",
    "value":0,
    "stock":0
}
```
- Consultar un producto específico: El url para consumir este servicio, a través de una operación Get, es como sigue: http://XXX.XXX.XXX.XXX:5000/api-queries/products/<<id-producto>>, donde <<id-producto>> representa el id del producto a consultar.
- Modificar un producto: El url para consumir este servicio, a través de una operación Put, es como sigue: http://XXX.XXX.XXX.XXX:5000/api-commands/products/<<id-producto>>, donde <<id-producto>> corresponde al id del producto a modificar, y se debe especificar en el Body del request la información nueva información del producto. El formato para la información del producto es un JSON similar al que sigue:
```json
{
    "name":"Nombre del producto",
    "description":"Descripción del producto",
    "value":0,
    "stock":0
}
```

##### Usuarios

Este servicio expone tres operaciones, las cuales se exponen de la siguiente manera para las ramas sync y sync-sec (reemplazar http por https):

- Listar todos los usuarios: El url para consumir este servicio, a través de una operación Get, es como sigue: http://XXX.XXX.XXX.XXX:5000/users y no requiere de ningún parámetro adicional.
- Crear un nuevo usuario: El url para consumir este servicio, a través de una operación Post, es como sigue: http://XXX.XXX.XXX.XXX:5000/users y se debe especificar en el Body del request la información del nuevo usuario. El formato para la información del nuevo usuario es un JSON similar al que sigue:
```json
{
    "name":"Nombre del usuario"
}
```
- Consultar un usuario específico: El url para consumir este servicio, a través de una operación Get, es como sigue: http://XXX.XXX.XXX.XXX:5000/users/<<id-usuario>>, donde <<id-usuario>> representa el id del usuario a consultar.

Para las ramas async y async-sec (reemplazar http por https), al implemetar el patrón CQRS las operaciones que expone este servicio se exponen en dos partes: comandos y consultas:

- Listar todos los usuarios: El url para consumir este servicio, a través de una operación Get, es como sigue: http://XXX.XXX.XXX.XXX:5000/api-queries/users y no requiere de ningún parámetro adicional.
- Crear un nuevo usuario: El url para consumir este servicio, a través de una operación Post, es como sigue: http://XXX.XXX.XXX.XXX:5000/api-commands/users y se debe especificar en el Body del request la información del nuevo usuario. El formato para la información del nuevo usuario es un JSON similar al que sigue:
```json
{
    "name":"Nombre del usuario"
}
```
- Consultar un usuario específico: El url para consumir este servicio, a través de una operación Get, es como sigue: http://XXX.XXX.XXX.XXX:5000/api-queries/users/<<id-usuario>>, donde <<id-usuario>> representa el id del usuario a consultar.

##### Jwt

Este servicio expone una sola operación, las cual se expone de la siguiente manera para las ramas async y async-sec (reemplazar http por https):

- Consultar token: El url para consumir este servicio, a través de una operación Get, es como sigue: http://XXX.XXX.XXX.XXX:5000/api-queries/jwt y no requiere de ningún parámetro adicional.
