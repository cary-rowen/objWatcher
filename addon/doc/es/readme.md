# obj Watcher #

**Este complemento para NVDA observa cambios en los atributos de los objetos.**

* Autor: Cary-rowen <manchen_0528@outlook.com>, hwf1324 <1398969445@qq.com>
* Compatibilidad: NVDA 2023.1 o posterior

## Casos de uso posibles

1. Ver subtítulos o letras de canciones en ciertos reproductores y habilitar
   el anuncio automático cuando se actualicen.
2. Mirar elementos de interés en la lista de un chat grupal de Unigram o la
   lista de conversaciones en WeChat. Los nuevos mensajes se anunciarán
   automáticamente, y se soporta el anuncio en segundo plano.
3. Sólo con propósitos de prueba, mirar también la barra de estado del bloc
   de notas para anunciar las filas y columnas durante la inserción y
   eliminación del contenido.

## Gestos

``Control+NVDA+w``: pulsa una vez para vigilar el objeto bajo el navegador
de objetos. Si el objeto actual del navegador de objetos ya está bajo
vigilancia, se anunciará el atributo observado. Pulsa dos veces para dejar
de observar.

**Este gesto se puede cambiar desde el diálogo Gestos de entrada.**

## Colaboradores

* Cary-rowen
* ibrahim hamadeh
* hwf1324

## Colaboración

1. El complemento acepta solicitudes de cambio (pull requests) con nuevas
   características y traducciones actualizadas en [GitHub][GitHub].
2. Si tienes comentarios, envíalos mediante una [incidencia de
   GitHub][GitHubIssue].

## Registro de cambios
### Versión 0.4.4
* Se soporta el modo de voz a petición de NVDA 2024.1.

### Versión 0.4.3
* Compatible con NVDA 2024.1

### Versión 0.4.2
* Se añade traducción al ucraniano por VovaMobile.

### Versión 0.4.1
* Se añade traducción al árabe, por ibrahim hamadeh.

### Versión 0.4.0
* Se puede configurar el intervalo de vigilancia en el panel de opciones. El
  valor por defecto es 100.

### Versión 0.3.4
* Documentación mejorada.
* La pulsación del gesto dos veces rápidamente ya no prioriza
  consistentemente la ejecución de la primera función de pulsación.

[[!tag dev stable]]

[GitHub]: https://github.com/cary-rowen/objWatcher [GitHubIssue]:
https://github.com/cary-rowen/objWatcher/issues

