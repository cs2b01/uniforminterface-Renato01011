from flask import Flask,render_template, request, session, Response, redirect
from database import connector
from model import entities
import json

db = connector.Manager()
engine = db.createEngine()
app = Flask(__name__)

@app.route('/')
def index():
    db_session = db.getSession(engine)
    alumno = entities.Alumno(apellido="Bacigalupo", nombre="Renato", codigo="201810112", password="Ut3c1234")
    alumno1 = entities.Alumno(codigo="20181158", nombre="Matias", apellido="Bernardo", password="Ut3c4321")
    alumno2 = entities.Alumno(codigo="20181098", nombre="Fernando", apellido="Medina", password="Ut3c1243")
    db_session.add(alumno)
    db_session.add(alumno1)
    db_session.add(alumno2)
    db_session.commit()
    db_session = db.getSession(engine)
    users = db_session.query(entities.Alumno)
    data = users[:]
    return Response(json.dumps(data, cls=connector.AlchemyEncoder), mimetype='application/json')

if __name__ == '__main__':
    app.run(port=8080)
