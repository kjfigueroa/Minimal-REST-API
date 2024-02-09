# minimal-rest-api.py

# Minmal Restful API, a Pet care center.
# Show pets (dogs and cats) by 'name', and then the 'age', and 'gender'

# ------------------------ 0. Inizialiting

from flask import Flask, jsonify, request
petlist = Flask(__name__)
from petsfile import dogs,cats

# ------------------------ 1. ROUTE [GET]

@petlist.route('/', methods=['GET'])
def regards():
    return jsonify({'response': 'Welcome!\n you can ask by dogs and cats'})

# ------------------------ 2. GET

    #---------->>>>>Dogs

@petlist.route('/dogs', methods=['GET'])
def getDogs():
    return jsonify({"dog's list": dogs})

@petlist.route('/dogs/<string:dog_name>')
def getDogName(dog_name):
    dogsFound = [dogname for dogname in dogs if dogname['name'] == dog_name]
    if (len(dogsFound) > 0):
        return jsonify({"I found this dog on my list": dogsFound[0]})
    return jsonify({'message': "Wow! this dog isn't in my list!"})

    #---------->>>>>Cats
@petlist.route('/cats', methods=['GET'])
def getCats():
    return jsonify({"cat's list": cats})

@petlist.route('/cats/<string:cat_name>')
def getCat(cat_name):
    catsFound = [catname for catname in cats if catname['name'] == cat_name]
    if (len(catsFound) > 0):
        return jsonify({"I found this cat on my list": catsFound[0]})
    return jsonify({'message': "Wow! this cat isn't in my list!"})

# ------------------------ 3. CREATE

    #---------->>>>>Dogs

@petlist.route('/dogs', methods=['POST'])
def addDog():
    new_dog = {
        'name': request.json['name'],
        'age': request.json['age'],
        'gender': request.json['gender']
    }
    dogs.append(new_dog)
    return jsonify({"Our new pet was successfully added": dogs})

    #---------->>>>>Cats

@petlist.route('/cats', methods=['POST'])
def addCat():
    new_cat = {
        'name': request.json['name'],
        'age': request.json['age'],
        'gender': request.json['gender']
    }
    cats.append(new_cat)
    return jsonify({"Our new pet was successfully added": cats})


# ------------------------ 4. UPDATE

    #---------->>>>>Dogs
@petlist.route('/dogs/<string:dog_name>', methods=['PUT'])
def editDog(dog_name):
    dogsFound = [dogname for dogname in dogs if dogname['name'] == dog_name]
    if (len(dogsFound) > 0):
        dogsFound[0]['name'] = request.json['name']
        dogsFound[0]['age'] = request.json['age']
        dogsFound[0]['gender'] = request.json['gender']
        return jsonify({
            'message': 'We have a new pet now!',
            'dogs list': dogsFound[0]
        })
    return jsonify({'message': "Wow! this cat isn't in my list!"})

    #---------->>>>>Cats

@petlist.route('/cats/<string:cat_name>', methods=['PUT'])
def editCat(cat_name):
    catsFound = [catname for catname in cats if catname['name'] == cat_name]
    if (len(catsFound) > 0):
        catsFound[0]['name'] = request.json['name']
        catsFound[0]['age'] = request.json['age']
        catsFound[0]['gender'] = request.json['gender']
        return jsonify({
            'message': 'We have a new pet now!',
            'cats list': catsFound[0]
        })
    return jsonify({'message': "Wow! this cat isn't in my list!"})

# ------------------------ 5. DELETE

    #---------->>>>>Dogs

@petlist.route('/dogs/<string:dog_name>', methods=['DELETE'])
def adoptDog(dog_name):
    dogsFound = [dogname for dogname in dogs if dogname['name'] == dog_name]
    if len(dogsFound) > 0:
        dogs.remove(dogsFound[0])
        return jsonify({
            'message': 'We have given a puppy up for adoption',
            'Our dogs': dogs
        })

    #---------->>>>>Cats

@petlist.route('/cats/<string:cat_name>', methods=['DELETE'])
def adoptCat(cat_name):
    catsFound = [catname for catname in cats if catname['name'] == cat_name]
    if len(catsFound) > 0:
        cats.remove(catsFound[0])
        return jsonify({
            'message': 'We have given a kitten up for adoption',
            'Our cats': cats
        })

# ------------------------ 6. RUN

if __name__ == '__main__':
    petlist.run(debug=True,host='0.0.0.0',port=4000)