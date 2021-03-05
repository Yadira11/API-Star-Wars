"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, User,Personaje,Planetas,Favoritos
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DB_CONNECTION_STRING')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

@app.route('/user', methods=['GET'])
def handle_hello():

    query = User.query.all()
    results = list(map(lambda x: x.serialize(), query))

    return jsonify(results), 200
@app.route('/user/<int:id>', methods=['GET'])
def getUser():

    user = User.query.get(id)
    if usuario is None:
        raise APIException('Usuario not found', status_code=404)
    results = user.serialize()

    return jsonify(results), 200

@app.route('/Personaje', methods=['GET'])
def personaje_todos():
    query = Personaje.query.all()
    results = list(map(lambda x: x.serialize(), query))
    return jsonify(results),200
@app.route ("/personajes/<int:personaje_id>" , methods=["GET"])
def personaje_unico(id):
    personajes = character.query.get(planeta_id)
    if personajes is None:
        raise APIException("Personaje is not found", status_code=404)
    results = personajes.serialize()
    return jsonify(result), 200
@app.route("/Personas", methods=["POST"])
def add_personas():
    request_body = request.get_json()
    print(request_body)
    add_personas= personas(name=request_body["name"], height=request_body["height"], gender=request_body["gender"], hair_color=request_body["hair_color"], eye_color=request_body["eye_color"] )
    db.session.add(add_personas)
    db.session.commit()


@app.route('/planetas', methods=['GET'])
def planetas_todos():
    query = Planetas.query.all()
    results = list(map(lambda x: x.serialize(),query))
    return jsonify(results),200
@app.route ("/planetas/<int:planeta_id>" , methods=["GET"])
def planeta_unico(planeta_id):
    planetas = character.query.get(planeta_id)
    if planetas is None:
        raise APIException("Planeta is not found", status_code=404)
    results = planetas.serialize()
    return jsonify(result), 200

@app.route("/add_planetas", methods=["POST"])
def add_planeta():
    request_body = request.get_json()
    print(request_body)
    add_planetas= planetas(name=request_body["name"], diameter=request_body["diameter"] , rotation_period= request_body["rotation_period"] , gravity=request_body["gravity"], population=request_body["population"], climate=request_body["climate"] )
    db.session.add(add_planetas)
    db.session.commit()

@app.route('/favoritos', methods=['GET'])
def favoritos_todos():
    query = Favoritos.query.all()
    results = list(map(lambda x: x.serialize(),query))
    return jsonify(results),200

@app.route ("/favoritos/<int:favorito_id>" , methods=["GET"])
def favorito_unico(favorito_id):
    favoritos = favoritos.query.get(favorito_id)
    if favoritos is None:
        raise APIException("Favoritos is not found", status_code=404)
    results = favoritos.serialize()
    return jsonify(result), 200

"""
COMO MANDAR UN ADD FAVORITO
{
    "personajes_name" :"Luke Skywalker",
    "planetas_name" :null,
    "user_name": "Yadira Chavarria"

}
O
{
    "personajes_name" :null,
    "planetas_name" :"Tatooine",
    "user_name": "Yadira Chavarria"

}
"""
@app.route("/add_Favoritos" , methods=["POST"])
def add_favorito():
    request_body = request.get_json()
    print(request_body)
    favorito= Favoritos(user_name=request_body["user_name"], planetas_name=request_body["planetas_name"], personajes_name=request_body["personajes_name"])
    db.session.add(favorito)
    db.session.commit()
    return jsonify("Good Job",200)


@app.route("/del_Favoritos/<int:fid>", methods=["DELETE"])
def del_Favoritos():
    favorito = Favoritos.query.get()
    if favorito is None:
        raise APIException('Favorito no encontrado', status_code=404)
        db.session.delete(favoritos)
        db.session.commit()

        return jsonify("Good,Good"),200
    response_body = {
        "msg": "Hello, this is your GET /user response "
    }

    return jsonify(response_body), 200

# this only runs if `$ python src/main.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
