## Callbacks en Python
En la primera parte del laboratorio se utilizaron los callbacks para simular un sistema de notificación de eventos. La clase EventManager en el módulo de eventos.py tiene como atributo un diccionario de eventos al que se le pueden agregar o eliminar valores usando los métodos subscribe y unsubscribe. Por otro lado, como se denota a continuación, el método notify recibe la llave del diccionario correspondiente al evento y los datos que la función o funciones de este necesiten. Luego, procede a ejecutar la función.
```python 
def notify(self, event, data=None):

        if event in self.subscribers:

            for callback in self.subscribers[event]:

                callback(data)
```
La clase mencionada anteriormente se utiliza como una instancia de la clase RealTimeDataManager en el módulo datamanager.py. Esta clase cuenta con un diccionario que almacena los datos de temperatura y humedad, y un método para actualizar dichos datos. Además, posee un método de bucle infinito que invoca la actualización de datos y utiliza el método notify del atributo de EventManager. Por otro lado, se creó una función externa para imprimir los datos actuales del diccionario. Se instanció una clase RealTimeDataManager y se registró el evento. 
```python
def get_data(dict_data):

        #Funcion que se encarga de buscar los datos actualizados

        print(f' Datos en tiempo real actualizados: Temperatura actual:{dict_data["temperatura"]} , Humedad actual:{dict_data["humedad"]}')

  

real_time_data_manager =RealTimeDataManager()

#Suscribir antravez del atributo que es una instancia de la clase EventManager el evento

real_time_data_manager.event_manager.subscribe("evento1",get_data)
```
En el método start_real_time_updates se busca en notify el evento y se le pasan los datos actualizados del diccionario. 
```python
 def start_real_time_updates(self):

        while True:

            time.sleep(3)

            self.generate_real_time_data()

            #Notificar el evento

            self.event_manager.notify("evento1",self.data)
```

### Resultados
Al ejecutar el programa se obtiene la siguiente salida: 

![Resultadoparte1](https://github.com/Msolis314/Clases/blob/main/lab6ejercicio1.png)
Cumpliendo el objetivo de imprimir las actualizaciones en tiempo real de los datos. 

## Funciones Lambda en Python
En la siguiente parte del laboratorio se utilizaron funciones lambda para crear un sistema de cálculos sencillos. Se reciben dos números por parte del usuario y una operación. Se verifica que ambos inputs sean adecuados. Además, se define un diccionario con las operaciones como llave y sus respectivas funciones lambda.
```python
operations = {"+" : lambda a,b: a+b , "-": lambda a , b : a-b,"/":lambda a , b : a/b,"*":lambda a , b : a*b}
```
Luego, se emplea una declaración condicional para verificar que la operación introducida por el usuario esté contenida en el diccionario. En caso afirmativo, se le pasa dicha operación y su clave con la función lambda como parámetros a otra función encargada de verificar nuevamente la operación e imprimir su resultado.
```python
if user_input[2] in operations:

            #Busca la llave de la operacion respectiva y le pasa como callback a la funcion ejecutar operaciones la operacion

            ejecutar_operacion(user_input, operations[user_input[2]])

        else:

            print("Operacion invalida. Seleccione (+, -, *, /) o  escriba 'exit' para salir.")
```
### Resultados
En la siguiente imagen se muestra como se ejecutan los cálculos con la operaciones respectivas:

![Parte 2](https://github.com/Msolis314/Clases/blob/main/reportelab6eje2.png)

Lo cual demuestra que la calculadora funciona adecuadamente. Además, cuando se le digita una entrada incorrecta se muestra lo siguiente: 

![Parte Exceptions](https://github.com/Msolis314/Clases/blob/main/Reporte6ej2false.png)

Por tanto, hay un adecuado manejo de excepciones. 
