# -*- coding: utf-8 -*-
"""unittest solution.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1bJ2c-ZZtjey2KAHX_8Jdui1R8WkGkmic

# Cómo desarrollar pruebas unitarias en Python 

La librería  **unittest**  (o PyUnit) permite desarrollar pruebas unitarias. Una prueba unitaria es una forma de comprobar el correcto funcionamiento de una unidad de código (función o método).

Para ello debemos desarrollar una subclase de la clase **TestCase** que incluirá una batería de pruebas de las funciones que queremos testear (comprobar si están bien implementadas o no). Cada prueba puede devolver tres respuestas:

- OK: indica que la prueba ha sido correcta.
- FAIL: indica que la prueba no ha sido incorrecta. Es decir, que la función no tiene el funcionamiento que se esperaba. En este caso, se lanza una excepción del tipo **AssertionError**.
- ERROR: indica que la prueba no ha sido correcta, pero en este caso, se ha producido un error en la función que se está probando. 

Veamos un ejemplo. La siguiente celda contiene una función que simula la división enterá de dos números y una clase que testea esta función. La función no es correcta (porque no utiliza el operador // sino el operador /). Sin embargo, la salida de la siguiente prueba es OK, porque la división entera de 4 entre 2, es 2.
"""

import unittest

def division_entera(a,b):
  return a/b

class Test(unittest.TestCase):
    def test_dividir(self):
        self.assertEqual(division_entera(4,2), 2)

#Comentar para usarlo en spyder
unittest.main(argv=['first-arg-is-ignored'], exit=False)

#Descomenar para usarlo en Spyder
#if __name__ == '__main__':
#    unittest.main()

"""Sin embargo, en la siguiente prueba la salida es un FAIL, porque el método devuelve 2.5, cuando debería devolver 2. Se lanza una excepción del tipo AssertionError."""

class Test(unittest.TestCase):
    def test_division_entera(self):
        self.assertEqual(division_entera(5,2), 2)

#Comentar para usarlo en spyder
unittest.main(argv=['first-arg-is-ignored'], exit=False)

#Descomenar para usarlo en Spyder
#if __name__ == '__main__':
#    unittest.main()

"""Por último, si tratamos de dividir 4 entre 0, esta prueba devolvera ERROR, no porque la función no devuelva la salida esperada, sino porque dentro de la misma función se produce un error (no es posible dividir entre 0, esto generá una excepción **ZeroDivisionError**).

"""

class Test(unittest.TestCase):
    def test_division_entera(self):
        self.assertEqual(division_entera(5,0), 0)

#Comentar para usarlo en spyder
unittest.main(argv=['first-arg-is-ignored'], exit=False)

#Descomenar para usarlo en Spyder
#if __name__ == '__main__':
#    unittest.main()

"""## Ejercicio
Implementa una función, **isOdd**, que reciba un número y devuelva True si el número es par y False en otro caso. 
"""

def isOdd(a): 
  if a%2==0:
    return True
  else:
    return False

"""Ahora debes implementar un test donde compruebes para varias entradas (un número par y un número impar) si las salidas de la función son correctas.  Así por ejemplo, la salida de **isOdd(3)** debe ser **False**, mientras que la salida de **isOdd(4)** debería ser **True*"""

import unittest
class Test(unittest.TestCase):
    def test_isOdd(self):
        self.assertEqual(isOdd(3), False)
        self.assertEqual(isOdd(10), True)

#Comentar para usarlo en spyder
unittest.main(argv=['first-arg-is-ignored'], exit=False)

#Descomenar para usarlo en Spyder
#if __name__ == '__main__':
#    unittest.main()

"""## Los métodos assert

La clase TestCase proporciona varios métodos que nos van a ayudar a comprobar si nuestras funciones han sido correctamente implementadas. Estos métodos están recogidos en la siguiente tabla:

| Método | Qué comprueba   |
|------|------|
|   assertEqual(a, b)  | a==b|
|   assertNotEqual(a, b)  | a!=b|
|   assertTrue(x)  | bool(x) is True|
|   assertFalse(x)  | bool(x) is False|
|   assertIs(a, b)  | a is b|
|   assertIsNot(a, b)  | a is not b|
|   assertIsNone(x)  | x is None|
|   assertIsNotNone(x)  | x is not None|
|   assertIn(a, b)  | a in b|
|   assertNotIn(a, b)  | a not in b|
|   assertIsInstance(a, b)  | isinstance(a, b)|
|   assertNotIsInstance(a, b)  | not isinstance(a, b)|

Puedes encontrar más información en: 

https://docs.python.org/3/library/unittest.html

## Los métodos setUp y  tearDown

La clase TestCase incluye un método **setUp()** que nos ayudará a preparar el contexto de las pruebas, por ejemplo, conectándose a una base de datos, cargando un fichero que contenga valores de prueba o almacenando los valores de prueba en las variables. 

También incluye el método **tearDown()**, que puede ser utilizado para deshacer los posibles cambios realizados durante las pruebas (por ejemplo, borrar un fichero, desconectarse de un servidor o borrar las entradas de prueba en un base de datos).

Por ejemplo, la función **tokenization** recibe un texto (oración) y devuelve su lista de palabras. También la función **removeShort** recibe una lista de palabras y elimina aquellas que tengan una longitud menor de 3.
"""

def tokenization(text):
  return text.split()

tokens=tokenization('Esto es una prueba de cómo dividir un texto en palabras')
print(tokens)

def removeShort(words):
  return [w for w in words if len(w)>3]

print(removeShort(tokens))

"""Ahora vamos a crear la clase Test para realizar pruebas unitarias para esas funciones. 

El método **setUp** nos va a permitir inicializar los parámetros de las funciones con las que vamos a probar y variables para almacenar las salidas que se espera
 
"""

class Test(unittest.TestCase):

  def setUp(self):
    self.text='Esta es una oración que vamos a dividir en tokens'
    self.words1=['Esta','es','una','oración','que','vamos','a','dividir','en','tokens']
    self.words2=['Esta','oración','vamos','dividir','tokens']

  def test_tokenization(self):
    self.assertEqual(tokenization(self.text), self.words1)

  def test_removeShort(self):
    self.assertEqual(removeShort(self.words1), self.words2)


unittest.main(argv=['first-arg-is-ignored'], exit=False)

"""## Ejercicio:

Implementa una función, **cifrar**, que reciba un texto y devuelva un nuevo texto cifrado. El cifrado consistirá en reemplazar las vocales del texto original por números, de la siguiente manera:

| Entrada | Cifrado|
|------|------|
|   a,A  | 1|
|   e,E  | 2|
|   i,I  | 3|
|   o,O  | 4|
|   u,U  | 5|




Ejemplo: 
*cifrar(‘Cesar’)=C2s1r*

Implementa la función y las pruebas necesarias para validar la función. 

"""

def cifrar(text):
  vowels={'a':1,'e':2,'i':3,'o':4,'u':5}
  result=''
  for c in text:
    if c.lower() in vowels.keys():
      result+=str(vowels[c.lower()])
    else:
      result+=c  
  return result

print(cifrar('Juan e Isabel'))
print(cifrar('Este es un algoritmo para cifrar'))
print(cifrar('Patata'))

class Test(unittest.TestCase):

  def setUp(self):
    self.input=['Esta','es','una','oración','que','vamos','a','dividir','en','tokens']
    self.output=['2st1', '2s', '5n1', '4r1c3ón', 'q52', 'v1m4s', '1', 'd3v3d3r', '2n', 't4k2ns']

  def test_cifrar(self):
    for i in range(len(self.input)):
      self.assertEqual(cifrar(self.input[i]),self.output[i])

unittest.main(argv=['first-arg-is-ignored'], exit=False)