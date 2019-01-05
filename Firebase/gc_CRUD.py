import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Use a service account
cred = credentials.Certificate('credentials.json')
firebase_admin.initialize_app(cred)

db = firestore.client()

def gcWrite(sensor,data,timestamp):
    x = timestamp

    timestamp = {
        str(timestamp) : int(data)
    }
    db.collection(str(sensor)). document(x).set(timestamp)



def gcRead(sensor, timestamp):
    doc_ref = db.collection(sensor).document(timestamp)

    try:
        doc = doc_ref.get()
        print(u'Document data: {}'.format(doc.to_dict()))
    except google.cloud.exceptions.NotFound:
        print(u'No such document!')

gcWrite('temp', '6:00')
