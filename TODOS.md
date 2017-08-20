##Modelo:
  ###Datos:
  - Hacer Clase DeviceState y TaskState
  - Hacer Clase AlertOptions y poner sus posibilidades
  - Obtener datos a partir de datetime inicio y un datetime fin (recibidos por POST).
  - Hacer que Mqtt cree Data por POST (según Device anteriormente consultado por GET)
  - Hacer que cuando se crea un dato se consulta por la IP o ID del Device que le pertenece para
    vincularlo en la bd (es lo anterior, supuestamente)
 
  ###Estadísticas:
  - Ver cómo hacer las estadísticas, si otra app o consultar directamente a la BD.
  - Vincularla con los datos.
  - Ver cómo cruzar todo para tener estadísticas por Device, consumo y Datetime.

##BD:
 - Hacer un script para entrar a phppgmyadmin de una
 - Hacer un script para buscar devices y data en postgre 
 - Ver si hacer sqlite, sql, postgre o mongodb.
 

##MQTT:
  - Hacer que sea ordenado el envío y recepción de los datos por POST O POR RABBITMQ.

##WEBSOCKET:
  - Tener solucionadas las urls (permisos) de respuesta para websocket desde angular.

##LOGIN y AUTENTICACIÓN:
  - Una autenticación por ruta en Ionic
  - Un token de sesión validado desde el server
  - Qué onda desde websocket o ajax con angular, el token va a ser validado siempre que se haga algo (url POST/GET)
  - Encriptación?
  - Cookies? En principio no se puede
  - Cómo crear cosas pero que pida permisos?


##INTERFAZ:
  - Sección de Estadísticas
  - Sección de Programación (Tareas / Tasks)
  - Login / Autenticación - Ver como resolver lo del Token