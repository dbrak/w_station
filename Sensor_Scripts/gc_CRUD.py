import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import time
import json

with open('Cred','r') as f:
    config = json.load(f)

# Use a service account
cred = credentials.Certificate(config['Firebase'])
firebase_admin.initialize_app(cred)

db = firestore.client()

def gcWrite(location,temp,humid,timestamp):
    x = str(timestamp)

    try:
        timestamp = {
            str('Temperature') : int(temp),

            str('Humidity') : int(humid),

            str('Time') : int(time.time())
        }
        db.collection(str(location)). document(x).set(timestamp)

    except:
        print("Firebase write failed at: ",timestamp)


def gcRead(location, timestamp):
    doc_ref = db.collection(str(location)).document(str(timestamp))

    try:
        doc = doc_ref.get()
        print(u'Document data: {}'.format(doc.to_dict()))
    except google.cloud.exceptions.NotFound:
        print(u'No such document!')


