# fotoalpes-microservices-examples

## Instalación

El ejemplo del caso Foto Alpes es un proyecto en Flask que implementa microservicios y las tácticas vistas en el curso Aritecturas ágiles de software. El presente repositorio contiene el código del ejemplo en diferentes ramas de acuerdo a los temas vistos. Las ramas del proyecto son:

- main: Rama que implementa CQRS y comunicación asíncrona
- sync: Rama que implementa comunicación síncrona
- security: Rama que implementa el uso de tokens y certificados de seguridad

Para ejecutar el proyecto es necesario instalar [Oracle VirtualBox](https://www.virtualbox.org/wiki/Downloads) en un pc local. Una vez instalado, se debe descargar la imagen de la máquina virtual ([MISW4202-FotoAlpes-Microservicios.zip](https://uniandes-my.sharepoint.com/:u:/g/personal/ci_cortesg_uniandes_edu_co/EQMbaoWx1yZOl5cMyrQ-8rgBqzCjd4HWqfLmfYs1vbWFZQ?e=16NHt7)) e importarla en Virtualbox. Para importar la imagen se deben seguir los siguientes pasos:

1. Descargar el archivo MISW4202-FotoAlpes-Microservicios.zip

2. Descomprimir el archivo descargado en el paso anterior

3. Abrir Oracle Virtualbox e ir al menú Máquina --> Añadir

   ![Agregar_VM](C:\Users\Carlos Cortes\Documents\Uniandes\Asistencia Graduada\MISO\Curso AAS\Ejemplo Foto AlpesV2\img\Agregar_VM.png)

4. Ubicar la carpeta donde se descomprimió el archivo zip y seleccionar el archivo MISW4202-FotoAlpes-Microservicios-New.ovdx

   <img src="C:\Users\Carlos Cortes\Documents\Uniandes\Asistencia Graduada\MISO\Curso AAS\Ejemplo Foto AlpesV2\img\Seleccionar_Archivo_VM.png" alt="Seleccionar_Archivo_VM" style="zoom:75%;" />

5. En el menú izquierdo debe aparecer la máquina con el nombre del archivo seleccionado

6. Dar clic en el botón Iniciar ubicado en la parte superior

   <img src="C:\Users\Carlos Cortes\Documents\Uniandes\Asistencia Graduada\MISO\Curso AAS\Ejemplo Foto AlpesV2\img\Iniciar_VM.png" alt="Iniciar_VM" style="zoom:75%;" />

7. Una vez la máquina termine de cargar, debe visualizar la pantalla de inicio

   <img src="C:\Users\Carlos Cortes\Documents\Uniandes\Asistencia Graduada\MISO\Curso AAS\Ejemplo Foto AlpesV2\img\Pantalla_Inicio_VM.png" alt="Pantalla_Inicio_VM" style="zoom:75%;" />

8. Ingresar con el usuario **estudiante** y la contraseña **Estudiante2021**

9. Ejecutar el siguiente comando:

   ```
   ifconfig
   ```

10. Tomar nota de la dirección ip que se despliega en pantalla, como aparece en la siguiente imagen:

    <img src="C:\Users\Carlos Cortes\Documents\Uniandes\Asistencia Graduada\MISO\Curso AAS\Ejemplo Foto AlpesV2\img\Direccion_IP_VM.png" alt="Direccion_IP_VM" style="zoom:75%;" />

11. La dirección IP obtenida en el paso anterior corresponde a la dirección asociada al adaptador de red de la máquina virtual. Tome nota de esta dirección porque se utilizará para acceder a los servicios desde su pc local

12. Ubíquese en el directorio fotoalpes-microservices-examples ejecutando el siguiente comando:

    ```
    cd fotoalpes-microservices-examples
    ```

13. Para ejecutar los servicios, corra el siguiente comando:

    ```
    sudo docker-compose up
    ```

    

## Pruebas

Una vez los servicios se estén ejecutando podemos hacer pruebas de las funciones expuestas por estos. El ejemplo no implementa una interfaz de usuario por lo que debemos utilizar un programa que permita consumir servicios REST. Se sugiere utilizar [Postman](https://www.postman.com/downloads/) para ejecutar los servicios del ejemplo, por lo que debe descargarlo haciendo clic sobre el enlace anterior.

Una vez haya descargado e instalado Postman, ejecute este programa siga los siguientes pasos:

1. Haga clic en el botón New

2. Seleccione la opción Collection

3. En el campo Name ingrese el nombre para el conjunto de pruebas o servicios, por ejemplo Ejemplo FotoAlpes. Luego haga clic en el botón Create

   <img src="C:\Users\Carlos Cortes\Documents\Uniandes\Asistencia Graduada\MISO\Curso AAS\Ejemplo Foto AlpesV2\img\Crear_Coleccion.png" alt="Crear_Coleccion" style="zoom:75%;" />

4. Nuevamente haga clic en el botón New

5. Seleccione la opción Request

6. En el campo Request name ingrese un nombre para la prueba a ejecutar, por ejemplo listar usuarios

7. En el campo Select a collection or folder to save escriba el nombre de la colección que definió en el paso 3 y seleccione la opción que aparece en el cuadro de abajo

8. Haga clic el el botón Save to ....

   <img src="C:\Users\Carlos Cortes\Documents\Uniandes\Asistencia Graduada\MISO\Curso AAS\Ejemplo Foto AlpesV2\img\Crear_Request.png" alt="Crear_Request" style="zoom:75%;" />

9. Dependiendo del servicio a probar seleccione el método requerido. Para las operaciones de consulta, el método es Get. Para las operaciones de creación el método es Post y para las operaciones de modificación el método es Put. El ejemplo no implementa ningún otro tipo de operaciones.

10. Ingrese el url del servicio y la operación a probar. Por ejemplo, para el caso de listar los usuarios, en la rama main, el url sería el siguiente: http://XXX.XXX.XXX.XXX/api-queries/users. Reemplace XXX.XXX.XXX.XXX por la dirección IP de la máquina virtual obtenida en el paso 9 de la sección **Instalación**

11. Haga clic en el botón Send

12. En la opción Body de la respuesta recibida se puede ver la información que retorna el servicio

    <img src="C:\Users\Carlos Cortes\Documents\Uniandes\Asistencia Graduada\MISO\Curso AAS\Ejemplo Foto AlpesV2\img\Listar_Usuarios.png" alt="Listar_Usuarios" style="zoom:75%;" />



Para el caso de las operaciones que usan los métodos Post y Put se debe especificar la información requerida por el servicio. Esta información se debe definir en formato Json en la opción Body del Request. La siguiente imagen muestra la definición de los datos para crear un nuevo usuario:

<img src="C:\Users\Carlos Cortes\Documents\Uniandes\Asistencia Graduada\MISO\Curso AAS\Ejemplo Foto AlpesV2\img\Crear_Usuario.png" alt="Crear_Usuario" style="zoom:75%;" />
