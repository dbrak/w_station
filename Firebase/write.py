import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Use a service account
cred = credentials.Certificate('ri-python-test-276d722bbbd2.json')
firebase_admin.initialize_app(cred)

db = firestore.client()

def gcWrite(name,dob,country):
    x = name

    name = {
        u'name' : str(name),
        u'dob' : str(dob),
        u'country': str(country)
    }
    db.collection(u'family'). document(x).set(name)


gcWrite('james', '19/04/09', 'UK')
