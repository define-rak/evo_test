# coding=utf-8
from flask import Flask, Response, request
from flask_sqlalchemy import SQLAlchemy

from datetime import *
from db import *
import random

import json

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://evo:evoevo@localhost:3306/evo'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

@app.route('/epithet', methods=['GET']) # /epithet?name=
def get_epithet():
    if request.args.get('name') == None:
        return Response(response=json.dumps('Bad request', indent=3),
                status=400,
                mimetype="application/json")
    else:
        name = request.args.get('name')
        try:
            curr_name = names.query.filter(names.name == name).one()
        except:
            curr_name = names(name=name, epithet_id=random.randint(1, epithets.query.count())) 
            db.session.add(curr_name)
            db.session.commit()
        else:
            pass

        curr_name = names.query.join(epithets, names.epithet_id == epithets.id).add_columns(names.name, epithets.epithet).filter(names.name == name).one()

        return Response(response=json.dumps({'name': curr_name.name, 'epithet': curr_name.epithet}, indent=3),
                status=200,
                mimetype="application/json")



@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
    return response

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5200, debug=True, threaded=True)