from flask import Flask, jsonify, request
from flask_pymongo import PyMongo



app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'dan'
app.config['MONGO_URI'] = 'mongodb://username:password@ds221339.mlab.com:21339/dan'

mongo = PyMongo(app)

@app.route('/', methods=['GET'])
def test():
    return jsonify({'message':'Welcome to the API'})

@app.route('/individuals', methods=['GET'])
def get_all():
    users = mongo.db.individuals

    output = []

    for q in users.find():
        output.append({
            "forenames": q["forenames"],
            "surname": q["surname"],
            "age": q["age"],
            "age_unit": q["age_unit"],
            "birth_county": q["birth_county"],
            "birth_place": q["birth_place"],
            "birth_place_flag": q["birth_place_flag"],
            "detail_flag": q["detail_flag"],
            "disability": q["disability"],
            "individual_flag": q["individual_flag"],
            "language": q["language"],
            "marital_status": q["marital_status"],
            "name_flag": q["name_flag"],
            "notes": q["notes"],
            "occupation": q["occupation"],
            "occupation_flag": q["occupation_flag"],
            "relationship": q["relationship"],
            "sequence_in_household": q["sequence_in_household"],
            "sex": q["sex"],
            "verbatim_birth_county": q["verbatim_birth_county"],
            "verbatim_birth_place": q["verbatim_birth_place"]
        })

    return jsonify({'result' : output})

@app.route('/individuals/<forenames>', methods=['GET'])
def get_one(forenames):
    users = mongo.db.individuals

    q = users.find_one({'forenames' : forenames})

    if q:
        output = {
            "forenames": q["forenames"],
            "surname": q["surname"],
            "age": q["age"],
            "age_unit": q["age_unit"],
            "birth_county": q["birth_county"],
            "birth_place": q["birth_place"],
            "birth_place_flag": q["birth_place_flag"],
            "detail_flag": q["detail_flag"],
            "disability": q["disability"],
            "individual_flag": q["individual_flag"],
            "language": q["language"],
            "marital_status": q["marital_status"],
            "name_flag": q["name_flag"],
            "notes": q["notes"],
            "occupation": q["occupation"],
            "occupation_flag": q["occupation_flag"],
            "relationship": q["relationship"],
            "sequence_in_household": q["sequence_in_household"],
            "sex": q["sex"],
            "verbatim_birth_county": q["verbatim_birth_county"],
            "verbatim_birth_place": q["verbatim_birth_place"]
        }
    else:
        output = 'No results found'

    return jsonify({'result' : output})


if __name__ == '__main__':
    app.run(debug=True)

# find a way to connect dwelling id in dwelling collection
