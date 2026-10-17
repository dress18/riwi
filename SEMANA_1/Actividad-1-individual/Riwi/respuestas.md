# Puntos de control

1. Ruta absoluta vs relativa: la absoluta parte de la raíz (ej. /home/usuario/Documents/Riwi/clientes/activos); la relativa parte de donde estoy (ej. desde Riwi, clientes/activos).
2. `.control_interno` no sale en `ls` porque los nombres que empiezan por punto son ocultos; se ven con `ls -a`. Los nombres con espacios se manejan con comillas ("lista de pendientes.txt") o con barra invertida.
3. `>` reemplaza el contenido del archivo; `>>` agrega al final. Uso `>` para crear o sobrescribir y `>>` para conservar el historial. En el experimento, la tercera línea con `>` borró las dos anteriores.
4. Mover cambia la ubicación pero el contenido sigue igual (se comprueba con `cat` antes y después).
5. `mv` mueve o renombra según el destino: otra carpeta = mover; otro nombre en la misma carpeta = renombrar.
6. Copiar un archivo usa `cp`; copiar una carpeta con subcarpetas exige `cp -r` (recursivo).
7. El respaldo no recibió la nueva línea porque una copia es un archivo independiente del original.
8. Buscar por nombre (`find`) localiza archivos por su nombre; buscar por contenido (`grep`) localiza texto dentro de los archivos.
9. `rmdir` solo elimina carpetas vacías; con archivos dentro falla para evitar borrar datos por accidente.
