#Flask es un sistema para hacer un servicio web.
#Get() sirve para obtener una respuesta (Datos, informacion, etc).
#Metodos http --- Post[]-- Publica y envía información  a un medio ejem: Pulicar un usuario en una BD.
#PUT[]- Actualiza información registrada previamente, esté necesita un identificador de registro para encontrarlo y realizar las modificaciones.

from flask import Flask, request, render_template,  url_for, redirect
from numpy import block 
from database import task


app=Flask(__name__)

#Si tu no le dices a route que tipo de http va a usar por default va ausar un get

#Ponerlo como Titulo
 #return "<h1>Hello Wolrd Flask</h1>" 

@app.route ("/")
def index():
    return render_template('index.html',todoList = task)

#Hacer que el texto introducido aparezca como liga
    #return "<a href='#'>Hola EBC</a>"

@app.route ("/ebc")
def HolaEBC():
    return "Hola EBC"

@app.route("/ebc/random")
def ungetrandom():
    return"Hola Random"

@app.route("/newtask", methods=['POST'])
def AddNewTask():
  if request.method == 'POST':
    newTask = {"id": len(task)+1, "name": request.form['task_name']}
    task.append(newTask)
    return redirect(url_for('index'))


if __name__ == '__main__': 
    app.run(port=5000,debug=True)

