# Diseño e implementación de un sistema dispensador de alimentos para mascotas.  🐶🐱
## Introducción

Como lo mencionan los autores del proyecto:
> "La estrecha relación ser humano mascota se hace cada día más notoria, pasando de ser la mascota de la casa, a ser parte fundamental del núcleo familiar, por tal razón, sus dueños buscan la manera de brindar soluciones tecnológicas a sus necesidades."

de lo anterior se considera que tener mascotas en casa es una tarea ardua que requiere de tiempo y mucha atención. Es notable que cuando el amo debe salir de casa y dejar a su pequeño amigo solo, la cuestión de la comida es algo que realmente atormenta, ya que para los animales es mesnester tener sus alimentos en cierto espacio de tiempo y en una cantidad adecuada. De aquí que **Jorge Iván Zapata Valencia y Daniel Alejandro Gil Agudelo** en el año 2017 se pensaron para su proyecto una solución ante esta problemática, implementando la tecnología de bajo costo y la los sistemas de control automatico; además de contar con una aplicación móvil para el respectivo monitoreo.

## Procedimiento

Para el desarrollo del presente proyecto se debe tener en cuenta que el diseño y la implementación del prototipo requiere de un ensamblaje mecanico y un modelado de ingenieria para adaptar la solución en un instrumento físico. De lo anterior, el prototipado se desarrolló en la plataforma [*SolidWorks*][enlace2] en la cual se produjeron 63 piezas en acrílico, teniendo en cuenta las características necesarias para que el dispositivo fuera resistente ante las diversas condiciones climatologicas y del medio externo.

[enlace2]: https://www.solidworks.com/community

|![modeloDispensador](https://user-images.githubusercontent.com/89711101/140620543-8ac33cd6-5d48-4dd0-9535-79492c296f68.JPG)|
|:--:|
|*Modelo SolidWorks: Dispensador alimento para mascotas. Autoria: Jorge Iván Zapata Valencia y Daniel Alejandro Gil Agudelo*|

Asimismo, como es necesario tener en cuenta estas características del modelado, es importante fijar el estudio en la población a la cual se desea beneficiar, en este caso a los animales y sus suministros de comida. Así pues, un parametro fundamental para este proyecto es la cantidad de comidas diarias de un animal en relación con su tiempo de vida (edad):


|Edad (meses) |  No. comidas|
|-------------|-------------|
|    0 - 3    |      4      |
|    3 - 6    |      3      |
|    6 - 17   |      2      |
|     18>=    |      1      |

Ahora bien, dejando de lado el prototipado mecánico, el desarrollo y la programación de este artefacto se da a través de un procesador de bajo costo, pero de gran alcance para proyectos que requieren de una cantidad significativa de entradas y salidas para su funcionamiento. El lenguaje de programación empleado es python con el sistema operativo Linux, además de contar con una conexión a internet mediante red wi-fi. Para la fase visual y la conexión a la base de datos se cuenta con HTML y Apache —como servidor web—
De lo anterior, las fases que componen al sistema se definen de la siguiente manera:
1. El cliente a través de la aplicación realiza una petición al servidor
2. El servidor la recibe, la manda a través de internet y la bifurca para dar una respuesta a dicha solicitud mediante [HTML][enlace]. 

[enlace]: https://www.w3schools.com/html/

4. Mediante la petición de internet se conecta al servidor web, se verifican los datos de la solicitud, se valida en la base de datos y envía una respuesta al procesador.
5. Python recibe la comunicación desded la base de datos y la implementa con los actuadores (electrónica) mediante la [raspberry pi] [enlace3].
6. Se ejecuta la petición del cliente (opera el dispensador de comida para la mascota)

[enlace3]:https://www.solidworks.com/community

|![Estructura etapas](https://user-images.githubusercontent.com/89711101/140651489-ec4cc791-012c-4048-a19b-afe877a17548.JPG)|
|:--:|
|*Modelo estructural del sistema.  Autoria: Jorge Iván Zapata Valencia y Daniel Alejandro Gil Agudelo*|

## Limitaciones del proyecto

* El proyecto está diseñado físicamente para mascotas de razas pequeñas, afectando la implementación en animales grandes debido a las raciones de comida.
  * Replanteamiento de las dimensiones del sismtema mecánico
  * Costos más elevados.

* La aplicación móvil solo está disponible para Android, es necesario para abrir el mercado expandirla a los diferentes sistemas operativo móviles
  ** Adaptación del servidor y la base de Datos a la nueva adquisición y las peticiones del lado del cliente.

* El dispensador funciona con un timer y es reprogramable; sin embargo sería óptimo implementar Inteligencia Artificial que le permita a la red aprender los gestos del perro y sus sonidos para que establezca la dosificación de alimento.


## Referencias

* Tomado de [Diseño e implentación de dispensador de alimento para mascotas](http://repositorio.utp.edu.co/dspace/bitstream/handle/11059/8054/6817664Z35)
* Pimanin Spirada, "Ayude a su perro comer para vivir, no vivir para comer."

