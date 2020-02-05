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

for place in placeList:
    query = session.query(PlaceMainDesc).filter(PlaceMainDesc.placeId == place.placeId)
    placeMain = query.first()
    if place.countryCode == "US":
        query = session.query(Weather).filter(Weather.state == place.stateCode)
        weather = query.first()
    else:
        query = session.query(Weather).filter(Weather.country == place.countryCode)
        weather = query.first()
    query = session.query(FlightPrice).filter(FlightPrice.airportId == place.airport1)
    flight = query.first()
    print(flight)
    query = session.query(Exchange).filter(Exchange.currencyUnit == place.currencyUnit)
    exchange = query.first()
    result  = {
        u'score': placeMain.score,
        u'subtitle': place.subtitle,
        u'titleEng': place.titleEng,
        u'titleKor': place.titleKor,
        u'updateDate' : datetime.now(),
    }
    if exchange is not None:
        exchangeResult = {
            u'exchange': {
                u"rateTitle": place.titleKor + u"의 환율",
                u"rateDescription": exchange.rateDescription,
                u"todayRate": exchange.todayRate,
                u"weekAgoRate": exchange.weekAgoRate,
                u"monthAgoRate": exchange.monthAgoRate,
            },
        }
        result.update(exchangeResult)
    if flight is not None :
        flightResult = {
            u'flight': {
                u"flightTitle": place.titleKor + u"의 비행기 표 값",
                u"flightDescription": flight.flightPriceDescription,
                u"todayAverage": flight.flightTodayAverage,
                u"todayMinimum": flight.flightTodayMinimum,
            },
        }
        result.update(flightResult)
    if weather is not None:
        weatherResult = {
            u'weather': {
                u'weatherTitle': place.titleKor + u"의 날씨",
                u'weatherDescription': weather.description,
                u"seoulToday": weather.seoulToday,
                u"placeAverage": weather.placeAverage,
                u"rainDays": weather.rainDays
            },
        }
        result.update(weatherResult)
    doc_ref = db.collection(u'place').document(place.placeId)

    doc_ref.update(result)
mainLogger.info("Commit Data To FireStore" + str(len(placeList)))



