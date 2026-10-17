# Bitácora · Día 2 · Herramientas de desarrollo

- **Coder:*Andrés Felipe Gómez Jiménez*
- **Fecha:*15/oct/2026*
- **TL:*Johan*

---

## 1. Mi entorno de desarrollo (Etapa 1)

- Versión de Ubuntu: Ubuntu 26.04.1 LTS
- Versión de Python: Python 3.14.4
- ¿Dónde está instalado Python? (resultado de which python3): /usr/bin/python3
- Con mis palabras, la diferencia entre un compilador y un intérprete es: la diferencia entre estos dos es que el intérprete traduce el código para que el sistema lo pueda ejecutar y el compilador lo que hace es ejecutar ese archivo linea por linea
- ¿Qué pasó con la línea 4 de hola.py y por qué?: Lo que paso con la linea 4 de hola.py es que como no detecta la variable mensaje_secreto, lanza error, pues sine sta no hay un que ejecutar

| Herramienta | ¿Qué es? (sistema operativo, editor, intérprete, compilador o navegador) |
|---|---|
| Ubuntu | | Sistema operativo
| VS Code | | editor
| Python | | intérprete
| Chrome | | navegador
| gcc | | compilador

## 2. Reinstalación de VS Code (Etapa 2)

- ¿Cómo estaba instalado VS Code? (snap, .deb o no estaba): code estaba instalado como snap
- Comando que usé para desinstalarlo: sudo snap remove code
- Comando que usé para instalarlo: sudo apt install ./code_*.deb
- ¿Por qué es importante instalar desde la fuente oficial?: porque así nos prevenimos en la medida de lo posible de no descargar malware
- ¿Qué pasó con mi configuración al desinstalar? ¿Dónde vive?: Las configuraciones que ya existian viven en las carpetas correspondientes que ya se habían creado, porque lo que hice fue eliminar code no las carpetas con las configs 

## 3. Perfiles y extensiones (Etapa 3)

- Con mis palabras, un perfil de VS Code es: Una carpeta con tu propia configuración visual y de atajos
- ¿Qué cambia en el Explorador entre un perfil y otro?: Los iconos con base en la extensión que se tenga instalada en el perfil
- ¿Por qué VS Code pregunta si confío en el publicador de una extensión?: Para que se nos asigne a nosotros la responsabilidad si instalamos una extensión de un autor que no conocemos y esta extensión tiene malware

## 4. Duelo de perfiles (Etapa 4)

| Prueba | Perfil2-Basico | Perfil1-Pro |
|---|---|---|
| 1. Auto guardado | Cuando no se le da ctrl + s no se guardan los cambios | Sin necesidad de presionar ctrl + s se guarda todo después de escribir algo nuevo |
| 2. Auto Rename Tag | Cuando cambio una etiqueta no se cambian la de cierre | Cuando se cambia una etiqueta de apertura o se elimina, se cambia o se elimina en la de cierre |
| 3. Error Lens | Cuando tenemos un error como por ejemplo el del parentesis, solo nos muestra una linea ondeadita | cuando tenemos un error, nos dice una pequeña descripción del error que tenemos |
| 4. Íconos | Sin la ext de los iconos, solo nos deja los predeterminados de vsc | Con esta extensión ya cambia todos, agregandoles iconos con diferentes colores |
| 5. Guías de indentación | Sin esta ext solo nos aparecen las tabulaciones limpias | Con la ext lo que hace es que cada tabulación la marca con una linea |
| 6. Extensiones corriendo | Sin esto solo aparecen las báscias las que vienen por defecto y tienen tiempos cortos de ejecución | Aquí ya aparecen las nuevas y los tiempos de ejecución cambian |

**Reflexión**

1. ¿Noté diferencias en la experiencia de trabajo entre los dos perfiles? ¿Cuáles?
   - La comodidad   
   - Las personalización entre cada perfil
2. ¿Qué ventajas tiene usar múltiples perfiles en VS Code?
   - Que varias personas pueden trabajas en el mismo pc, pero con diferentes perfiles y cada perfil personalizado a su gusto
3. ¿Cómo influyen las extensiones en la productividad y en el rendimiento del editor?
   - Que cada una de ellas te ayuda en algo diferente, por ejemplo con la extensión de rename tag haces lo mismo como si lo estuvieras haciendo a mano, pero en menos tiempo
4. ¿Cuándo sería útil usar perfiles distintos en un entorno profesional? (dos ejemplos)
   - Cuando hay un solo computador para varios empleados
   - Cuando vas a trabajar con una cosa u otra

## 5. Inspección y modificación (Etapa 5)

- Página que usé: https://es.wikipedia.org/wiki/Medell%C3%ADn
- Cinco etiquetas que encontré y para qué sirven:
  1. h1: titulo principal de la página
  2. p: texto
  3. img: para imprimir imagenes
  4. a: para links
  5. div: contenedores
- ¿Qué pasó con mis cambios al recargar y por qué?: Se desaparecieron, porque los cambios solo se guardan en nuestro navegador, los archivos principales, solo los pueden cambiar los devs
- Con mis palabras, el DOM es: El dom es  lo que nos permite modificar los que se ve en las páginas

## 6. La consola (Etapa 6)

| Operación | Mi predicción | Resultado real |
|---|---|---|
| 2 + 3 | 5 | 5 |
| 10 - 4 * 2 | 2 | 2 |
| (10 - 4) * 2 | 12 | 12 |
| 10 / 4 | 2.5 | 2.5 |
| 10 % 3 | 1 | 1 |
| 2 ** 8 | 256 | 256 |
| 120000 * 0.19 | 22800| 22800 |
| 365 * 24 | 8760 | 8760 |

- ¿Por qué 0.1 + 0.2 no da exactamente 0.3?:
- Errores o advertencias que encontré en la página (o "ninguno"):
- Diferencia entre un error y una advertencia:

## 7. La red / Network (Etapa 7)

| Imagen | Formato | Tamaño | Tiempo | Código de estado |
|---|---|---|---|---|
| icono corazon | svg+xml | 1.2KB | 143ms | 200 |
| Logo Wikipedia | png | 14.2KB | 108ms | 200 |
| Icono menú | svg+xml | 1.1KB | 218 | 200 |

| Experimento | Solicitudes | Transferido | Load |
|---|---|---|---|
| A. Sin caché | 49 / 63 | 0.0KB/88.9KB | 260 |
| B. Con caché | 63 | 1.2MB | 1 |
| C. Red lenta | | | |

- Archivo más pesado de la página y su tipo: El archivo más pesado es un documento y pesa 220KB
- ¿Por qué la página cargó más rápido con caché?: Porque se guardan algunos archivos en la caché del servidor, sin caché se tienen q traer todos los archivos del servidor
- ¿Por qué un desarrollador querría probar con una red lenta?: Para saber como se comportaria su página y los tiempos que demoraria un usuario en acceder a ella si tiene una red lenta
- ¿Qué haría para que una imagen pesada cargue más rápido?: reducirle el peso

## 8. Dispositivos móviles (Etapa 8)

| Ancho (px) | Dispositivo | ¿Cambia el menú? | ¿Imágenes bien? | ¿Scroll horizontal? | Observación |
|---|---|---|---|---|---|
| 320 | Responsive (No hay uno para ese ancho) | Sí, se ponen las 3 rayitas del menú | Si, en lugar de aparecer en el lado derecho aparecen abajo con un buen tamaño | No | No hay un dispositivo específicamente con este ancho |
| 375 | Iphone SE | Sigue con el menú hamburguesa | Sí | No | La información ahora no se va hacia tan abajo porque se expande más hacia los lados |
| 768 | iPad Mini | Sigue con el menú hamburguesa | Sí | No | Ahora las imagenes ya aparecen a la derecha |
| 1024 | Laptop | Sigue con menú hamburguesa y aún no aparecen los links que aparecen en pc normal | Si, ahora más grandes al lado derecho | No | Aún no aparecen las mismas cosas que normalmente aparecerian |
| 1440 | Laptop L| Sigue el menú hamburguesa, pero aún no aparece lo que aparece normalmente | Sí, mucho más grandes | No | Ahora hay más espacio y la información a pesar de que no se divide, tiene un marga x más grande |

- ¿Por qué es importante probar varias resoluciones antes de entregar un proyecto?: Para saber si nuestro proyecto es responsive y saber en que dispositivos se puede o no usar

## 9. Laboratorio de errores (Etapa 9)


| # | Tipo | ¿Dónde lo detecté? | Mensaje o síntoma | Causa | Solución aplicada |
|---|---|---|---|---|---|
| 1 | JavaScript (TypeError) | En la consola, en la línea del addEventListener de app.js. | Apareció un error porque no encontraba el botón y el código dejaba de ejecutarse. | El botón tenía el id boton-saludar, pero en JavaScript estaba buscando btn-saludar. | Cambié el selector para que buscara el id correcto: document.querySelector("#boton-saludar"). |
| 2 | JavaScript (ReferenceError) | En la consola, al hacer clic en el botón de saludar. | El saludo no cambiaba porque había un error con el nombre de una variable. | La variable se había declarado como nombreCoder, pero se estaba usando como nombreCodr. | Corregí el nombre de la variable para que fuera igual en las dos partes del código. |
| 3 | Ruta incorrecta (404) | En la pestaña Network, donde aparecía app.js en rojo, y también en la consola. | El archivo JavaScript no se encontraba, por lo que el contador y el saludo no funcionaban. | La ruta tenía las letras mayúsculas y minúsculas diferentes a las de la carpeta real. | Corregí la ruta para que coincidiera con el nombre de la carpeta: ../js/app.js. |
| 4 | Recurso no encontrado (404) | En la pestaña Network, en el filtro Img, al revisar logo.png o favicon.ico. | La imagen del logo no aparecía correctamente o el ícono de la pestaña no se mostraba. | La ruta del archivo no coincidía con la ubicación real de la imagen o del ícono. | Corregí la ruta del archivo o lo moví a la carpeta correspondiente para que la página pudiera encontrarlo. |


- Uno de los errores, descrito con detalle, y cómo lo resolví: El error #1 fue el que más me confundió, porque el contador de visitas funcionaba, pero el botón de saludar no hacía nada. Al revisar la consola, me apareció un TypeError en la línea del addEventListener, Revisando el HTML vi que el id era diferente al que estaba buscando en JavaScript. Lo corregí y al recargar la página, apareció otro error con el nombre de una variable que estaba mal escrito, ese segundo error no se mostraba antes porque el primero hacía que el script se detuviera
- ¿Qué vi al pausar con el breakpoint?: Al pausar el código, vi que la variable visitas todavía tenía el valor de la visita anterior, porque aún no se había ejecutado la línea que le suma uno. Cuando avancé, el valor aumentó y se guardó en el localStorage. Las variables boton y nombreCoder todavía no tenían un valor porque esas líneas no se habían ejecutado
- ¿Qué pasó al cambiar visitas por 99 y al borrarlo?: Cuando cambié el valor de visitas a 99 y recargué la página, el contador mostró 100 porque el código le suma uno al valor que encuentra guardado. Después, al borrar ese dato del localStorage, el contador volvió a empezar desde 1
- ¿Para qué usan el localStorage las páginas reales? ¿Qué NO debería guardar ahí?: El localStorage se usa para guardar cosas que una página necesita recordar, como el tema oscuro, el idioma o los datos de un formulario. Pero no se debe de guardar información importante como contraseñas, datos de tarjetas o información personal, porque los scripts de la página pueden acceder a esos datos y no están cifrados
- Ancho exacto en el que se apilan las tarjetas y regla de CSS responsable: Las tarjetas se empiezan a apilar cuando la pantalla tiene 600px o menos de ancho, porque esa es la condición que tiene el media query. Cuando el ancho es de 601px o más, las tarjetas siguen apareciendo una al lado de la otra
- ¿Por qué no basta con mirar solo la consola para encontrar errores?: Porque no todos los errores aparecen en la consola. También pueden haber problemas con los estilos, las rutas de los archivos o elementos del HTML que no están funcionando como deberían. Además, cuando aparece un error que detiene el script, puede que los demás errores no se muestren hasta que se corrija el primero


## 10. Comparación con Firefox (Etapa 10)

| Herramienta | Chrome: nombre y atajo | Firefox: nombre y atajo | Diferencia que noté |
|---|---|---|---|
| Inspeccionar HTML y CSS | Elements — Ctrl + Shift + I | Inspector — Ctrl + Shift + I | Los dos permiten revisar y modificar el HTML y CSS, pero cambia la forma en que organizan algunas opciones. |
| Consola | Console — Ctrl + Shift + J | Consola — Ctrl + Shift + K | En los dos puedo ejecutar código y revisar errores, pero el atajo para abrirla es diferente. |
| Red | Network — Ctrl + Shift + I y seleccionar Network | Red — Ctrl + Shift + E | Los dos muestran las solicitudes y los archivos que carga la página, aunque la forma de acceder es diferente. |
| Simulación de dispositivos | Device Toolbar — Ctrl + Shift + M | Modo de diseño adaptable — Ctrl + Shift + M | Ambos permiten probar cómo se ve una página en diferentes tamaños de pantalla. |
| Almacenamiento local | Application — Ctrl + Shift + I y seleccionar Application | Almacenamiento — Ctrl + Shift + I y seleccionar Almacenamiento | En ambos se puede revisar el localStorage, pero se encuentra en una sección diferente. |
| Mensaje del error que reintroduje | Console — muestra el error de JavaScript | Consola — muestra el error de JavaScript | Los dos muestran información sobre el error y ayudan a encontrar la línea donde ocurre. |

- Una característica de Firefox interesante o diferente a Chrome (qué es, para qué sirve y cómo la probé): Una característica interesante es el modo de diseño adaptable, porque permite probar una página con diferentes tamaños de pantalla. Lo utilicé para revisar cómo cambiaba la página al modificar el ancho y comprobar si los elementos se acomodaban correctamente.


## 11. Reflexión final (Etapa 11)

- La herramienta que más voy a usar y por qué: La consola, porque me permite encontrar errores en el código y entender por qué algunas cosas no funcionan como deberían. También me parece útil Network para revisar si los archivos están cargando correctamente

- Lo más difícil del día y cómo lo resolví: Lo más difícil fue encontrar los errores que hacían que algunas funciones no trabajaran. Lo resolví revisando la consola, comparando el código con el HTML y corrigiendo los nombres y las rutas que estaban mal

- Las DevTools explicadas para alguien que no programa (3 líneas):
Las DevTools son herramientas que permiten revisar cómo funciona una página web por dentro
Con ellas se pueden encontrar errores, revisar los archivos y comprobar cómo se ve la página en diferentes dispositivos
También ayudan a los desarrolladores a solucionar problemas y mejorar el funcionamiento de sus proyectos
