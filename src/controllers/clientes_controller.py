from flask import request, jsonify
from flask_controller import FlaskController
from src.models.clientes import Clientes
from src.app import app
from src.schemas.clientes_schema import clientes_schema, cliente_schema
import re

class ClientesController(FlaskController):
    @app.route('/api/v1/clientes', methods=['GET'])
    def lista_clientes():
        try:
            clientes = Clientes.traer_clientes()
            return clientes_schema.dump(clientes)
        except:
            return jsonify({ 'error': 'Error de conexión a la base de datos.' }), 400

    @app.route('/api/v1/clientes/<id>', methods=['GET'])
    def cliente_por_id(id):
        try:
            cliente = Clientes.traer_cliente_por_id(id)
            return cliente_schema.dump(cliente)
        except:
            return jsonify({ 'error': 'Error de conexión a la base de datos.' }), 400
        
    @app.route('/api/v1/clientes', methods=['POST'])
    def crear_cleinte():
        cliente = Clientes(documento_identidad=request.json["documento_identidad"], 
                           nombre_completo=request.json["nombre_completo"], 
                           direccion=request.json["direccion"], 
                           telefono=request.json["telefono"], 
                           email=request.json["email"])
        try:
            Clientes.crear_cliente(cliente)
            return jsonify({ 'success': 'Cliente creado correctamente.' }), 201
        except:
            return jsonify({ 'error': 'Error al almacenar el cliente.' }), 400
