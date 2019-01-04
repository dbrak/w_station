import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore


# Use a service account
cred = credentials.Certificate('ri-python-test-276d722bbbd2.json')
firebase_admin.initialize_app(cred)

db = firestore.client()

def gcRead(name):
    doc_ref = db.collection(u'family').document(name)

    try:
        doc = doc_ref.get()
        print(u'Document data: {}'.format(doc.to_dict()))
    except google.cloud.exceptions.NotFound:
        print(u'No such document!')

gcRead(u'jake')
