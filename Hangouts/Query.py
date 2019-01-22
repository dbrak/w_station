import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import json

with open('Cred','r') as f:
    config = json.load(f)

# Use a service account
cred = credentials.Certificate(config['Firebase'])
firebase_admin.initialize_app(cred)

db = firestore.client()

def query(location, type, operation, value, field):

    collection = db.collection(str(location))
    q = collection.where(str(type), str(operation), value).get()

    dictionary = {el.id: el.to_dict() for el in q}

    data = {}

    for i in dictionary.keys():

        k = dictionary[i]
        t = k[str(field)]
        data.update({i : t})
    return data

temp = query('Joe\'s Study', 'Temperature', '>', 20, 'Temperature')

print (temp)
