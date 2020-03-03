import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore



import inspect,json,os

path = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))


cred = credentials.Certificate(path+ "/eight-days-9e75a-firebase-adminsdk-47po1-8cd5d44953.json")
firebase_admin.initialize_app(cred, {
  'projectId' : 'eight-days-9e75a',
})
db = firestore.client()
from DatabaseQuery import *
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from datetime import datetime

with open(path + '/config.json', 'r') as f:
    config = json.load(f)
import logging

sqlHost = config["host"]
sqlUser = config["user"]
sqlPasswd = config["passwd"]
sqlDb = config["db"]

mainLogger = logging.getLogger("serviceFeeder")
mainLogger.setLevel(logging.INFO)
streamHandler = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
streamHandler.setFormatter(formatter)
mainLogger.addHandler(streamHandler)
fileHandler = logging.FileHandler(path + "/main.log")
fileHandler.setFormatter(formatter)
mainLogger.addHandler(fileHandler)

engine = create_engine("mysql+pymysql://" +sqlUser +":"+sqlPasswd+"@"+sqlHost + "/" + sqlDb +"?charset=utf8mb4",encoding='utf-8', echo=False)

Session = sessionmaker(bind=engine)
session = Session()
query = session.query(PlaceStatic)
placeList = query.all()

# 이미 있는 문서인지 체크하기 위한 Id List

docs = db.collection(u'curation').stream()
for doc in docs:
    newListOfPlaces = [];
    print(doc.to_dict())
    for item in doc.to_dict()["list_of_places"]:
        print(item["place_id"])
        place = db.collection(u'place').document(item["place_id"]).get().to_dict()
        if place is None:
            # 없으면 Curation에서 삭제함.
            pass
        else:
            print(place)
            item["score"] = place["score"]
            newListOfPlaces.append(item)

    newDoc = doc.to_dict()
    newDoc["list_of_places"] = newListOfPlaces
    doc_ref = db.collection(u'curation').document(doc.id)
    doc_ref.update(newDoc)

# docs는 generator라서 len()을 쓸 수 없음
mainLogger.info("Commit Curation Data To FireStore" + str(1 + sum(1 for x in docs)))
