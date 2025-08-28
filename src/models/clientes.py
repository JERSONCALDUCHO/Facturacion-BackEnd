from sqlalchemy import Column, Integer, String, Float, ForeignKey
from src.models import session, Base


class Clientes(Base):
    __tablename__ = "clientes"
    id = Column(Integer, primary_key=True)
    documento_identidad = Column(String(20), unique=True, nullable=False)
    nombre_completo = Column(String(100), nullable=False)
    direccion = Column(String(300), nullable=False)
    telefono = Column(String(20), nullable=False)
    email = Column(String(200))

    def __init__(self,
                 documento_identidad,
                 nombre_completo,
                 direccion,
                 telefono,
                 email):
        self.documento_identidad = documento_identidad
        self.nombre_completo = nombre_completo
        self.direccion = direccion
        self.telefono = telefono
        self.email = email

    def crear_cliente(cliente):
        cliente = session.add(cliente)
        session.commit()
        return cliente
    
    def traer_cliente_por_id(id):
        cliente = session.query(Clientes).filter(Clientes.id == id).first()
        return cliente

    def traer_clientes():
        clientes =  session.query(Clientes).all()
        return clientes
    