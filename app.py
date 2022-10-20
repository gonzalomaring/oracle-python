from flask import Flask, request, session, redirect, url_for, render_template, flash
import re 
import oracledb
import os
 
app = Flask(__name__)

@app.route('/')
def inicio():
    return render_template("index.html") 
@app.route('/login',methods=['POST'])
def login():
    from flask import request
    usuario=request.form.get("usuario")
    contrasena=request.form.get("contraseña")
    with oracledb.connect(user=usuario, password=contrasena, dsn="localhost:1521/ORCLCDB") as connection:
        with connection.cursor() as cursor:
            sql = """select nombre from equipos"""
            lista_equipos=[]
            for r in cursor.execute(sql):
                lista_equipos.append(r[0])
            return render_template("login.html",lista_equipos=lista_equipos)