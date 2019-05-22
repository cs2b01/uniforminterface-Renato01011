from sqlalchemy import Column, Integer, String, Sequence, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from database import connector

class Alumno(connector.Manager.Base):
    __tablename__ = 'alummnos'
    id = Column(Integer, Sequence('alumno_id'), primary_key=True)
    codigo = Column(String(9))
    nombre = Column(String(30))
    apellido = Column(String(30))
    password = Column(String(10))
