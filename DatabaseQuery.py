# coding: utf-8
from sqlalchemy import Column, DateTime, Float, String, Table, Text
from sqlalchemy.dialects.mysql import BIGINT, INTEGER, LONGTEXT, TINYINT
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class RawFlightAgent(Base):
    __tablename__ = 'RawFlightAgents'

    rawFlightAgentsId = Column(String(100), primary_key=True)
    agentsId = Column(INTEGER(11))
    carrierImageUrl = Column(String(100))
    writeDate = Column(DateTime)
    apiCallId = Column(String(100))


class RawFlightCarrier(Base):
    __tablename__ = 'RawFlightCarriers'

    rawFlightCarriersId = Column(String(100), primary_key=True)
    carrierId = Column(INTEGER(11))
    carrierCode = Column(String(100))
    carrierName = Column(String(100))
    carrierImageUrl = Column(String(100))
    writeDate = Column(DateTime)
    apiCallId = Column(String(100))


class RawFlightItinerary(Base):
    __tablename__ = 'RawFlightItineraries'

    rawFlightItinerariesId = Column(String(100), primary_key=True)
    outboundLegId = Column(String(100))
    inboundLegId = Column(String(100))
    pricingOptions = Column(Text)
    bookingDetailsLink = Column(Text)
    apiCallId = Column(String(100))
    queryAdults = Column(INTEGER(11))
    queryChildren = Column(INTEGER(11))
    queryOriginPlace = Column(String(100))
    queryDestinationPlace = Column(String(100))
    queryOutboundDate = Column(DateTime)
    queryInboundDate = Column(DateTime)
    queryCabinClass = Column(String(100))
    queryGroupingPricing = Column(TINYINT(1))
    writeDate = Column(DateTime)


class RawFlightLeg(Base):
    __tablename__ = 'RawFlightLegs'

    rawFlightLegsId = Column(String(100), primary_key=True)
    legId = Column(String(100))
    segmentsIds = Column(Text)
    originStation = Column(String(100))
    destinationStation = Column(String(100))
    departureDatetime = Column(DateTime)
    arrivalDatetime = Column(DateTime)
    duration = Column(INTEGER(11))
    journeyMode = Column(String(100))
    stops = Column(Text)
    carriers = Column(Text)
    operatingCarriers = Column(Text)
    directionality = Column(String(100))
    flightNumbers = Column(Text)
    writeDate = Column(DateTime)
    apiCallId = Column(String(100))


class RawFlightPlace(Base):
    __tablename__ = 'RawFlightPlaces'

    rawFlightPlacesId = Column(String(100), primary_key=True)
    skyscannerPlaceId = Column(INTEGER(11))
    skyscannerPlaceParentId = Column(INTEGER(11))
    skyscannerPlaceCode = Column(String(100))
    skyscannerPlaceType = Column(String(100))
    skyscannerPlaceName = Column(String(100))
    apiCallId = Column(String(100))
    writeDate = Column(DateTime)


class RawFlightPricingOption(Base):
    __tablename__ = 'RawFlightPricingOptions'

    rawFlightPricingOptionsId = Column(String(100), primary_key=True)
    rawFlightItinerariesId = Column(String(100))
    agents = Column(Text)
    price = Column(Float)
    deepLinkUrl = Column(Text)
    writeDate = Column(DateTime)


class RawFlightQuote(Base):
    __tablename__ = 'RawFlightQuotes'

    rawFlightQuotesId = Column(String(100), primary_key=True)
    skyscannerQuoteId = Column(String(100))
    minPrice = Column(Float)
    direct = Column(TINYINT(1))
    quoteFirstLegCarrierId = Column(String(100))
    quoteFirstLegDestinationId = Column(String(100))
    quoteFirstLegOriginId = Column(String(100))
    quoteFirstDepartureDate = Column(DateTime)
    quoteDateTime = Column(DateTime)
    queryOutboundDate = Column(DateTime)
    queryInboundDate = Column(DateTime)
    queryDestinationPlace = Column(Text)
    queryOriginPlace = Column(Text)
    writeDate = Column(DateTime)
    apiCallId = Column(String(100))


class RawFlightSegment(Base):
    __tablename__ = 'RawFlightSegments'

    rawFlightSegmentsId = Column(String(100), primary_key=True)
    segId = Column(String(100))
    originStation = Column(String(100))
    destinationStation = Column(String(100))
    departureDatetime = Column(DateTime)
    arrivalDatetime = Column(DateTime)
    carrier = Column(String(100))
    operatingCarrier = Column(String(100))
    duration = Column(INTEGER(11))
    flightNumber = Column(String(100))
    journeyMode = Column(String(100))
    directionality = Column(String(100))
    writeDate = Column(DateTime)
    apiCallId = Column(String(100))


class Exchange(Base):
    __tablename__ = 'exchange'

    exchangeId = Column(String(100), primary_key=True)
    currencyUnit = Column(String(100))
    currencyName = Column(String(100))
    todayRate = Column(INTEGER(11))
    weekAgoRate = Column(INTEGER(11))
    monthAgoRate = Column(INTEGER(11))
    rateList = Column(Text)
    rateTitle = Column(LONGTEXT)
    rateDescription = Column(LONGTEXT)
    created = Column(DateTime, nullable=False)
    dateToShow = Column(DateTime, nullable=False)
    score = Column(Float)


class FlightPrice(Base):
    __tablename__ = 'flightPrice'

    flightPriceId = Column(String(100), primary_key=True)
    airportId = Column(String(100))
    flightPriceTitle = Column(Text)
    flightPriceDescription = Column(LONGTEXT)
    flightMonthAgoAverage = Column(INTEGER(11))
    flightMonthAgoMinumum = Column(INTEGER(11))
    flightTodayAverage = Column(INTEGER(11))
    flightTodayMinimum = Column(INTEGER(11))
    created = Column(DateTime, nullable=False)
    dateToShow = Column(DateTime, nullable=False)
    score = Column(INTEGER(11))


class HotelPrice(Base):
    __tablename__ = 'hotelPrice'

    hotelPriceId = Column(String(100), primary_key=True)
    placeId = Column(String(100))
    hotelPriceTitle = Column(Text)
    hotelPriceDescription = Column(LONGTEXT)
    generalAverage = Column(INTEGER(11))
    luxuryAverage = Column(INTEGER(11))
    hostelAverage = Column(INTEGER(11))
    created = Column(DateTime, nullable=False)
    dateToShow = Column(DateTime, nullable=False)


class PlaceMainDesc(Base):
    __tablename__ = 'placeMainDesc'

    placeMainDescId = Column(String(100), primary_key=True)
    score = Column(INTEGER(11))
    placeId = Column(String(100))
    placeMainDescription = Column(LONGTEXT)
    created = Column(DateTime, nullable=False)
    dateToShow = Column(DateTime, nullable=False)


class PlaceOp(Base):
    __tablename__ = 'placeOp'

    placeOpId = Column(String(100), primary_key=True)
    placeId = Column(String(100))
    opMsgTitle = Column(Text)
    opMsgDesc = Column(LONGTEXT)
    created = Column(DateTime, nullable=False)
    dateToShow = Column(DateTime, nullable=False)


class PlaceStatic(Base):
    __tablename__ = 'placeStatic'
    placeId =  Column(String(100), primary_key=True)
    titleKor = Column(String(100))
    titleEng = Column(String(100))
    countryName = Column(String(100))
    countryCode = Column(String(100))
    stateName = Column(String(100))
    stateCode = Column(String(100))
    currencyUnit = Column(String(100))
    subtitle = Column(String(100))
    airport1 = Column(String(100))
    airport2 = Column(String(100))
    airport3 = Column(String(100))
    imgUrl = Column(String(300))
    created = Column(DateTime)


class RawExchange(Base):
    __tablename__ = 'rawExchange'

    rawExchangeId = Column(String(100), primary_key=True)
    result = Column(INTEGER(11))
    currencyUnit = Column(String(100))
    currencyName = Column(String(100))
    transferBuying = Column(String(100))
    transferSelling = Column(String(100))
    basicRate = Column(String(100))
    bookRate = Column(String(100))
    yearRate = Column(String(100))
    tenDaysRate = Column(String(100))
    korBasicRate = Column(String(100))
    korBookRate = Column(String(100))
    writeDate = Column(DateTime)
    rateDate = Column(DateTime)

class RawWeatherSeoulOnly(Base):
    __tablename__ = 'rawWeatherSeoulOnly'

    rawWeatherSeoulId = Column(String(100), primary_key=True)
    temperature = Column(Float)
    temperatureMax = Column(Float)
    skyCode = Column(INTEGER(11))
    waterfallCode = Column(INTEGER(11))
    waterfallKor = Column(String(100))
    waterfallEng = Column(String(100))
    waterfallProb = Column(Float)
    windSpeed = Column(INTEGER(11))
    windDirection = Column(INTEGER(11))
    windDirectionKor = Column(String(100))
    windDirectionEng = Column(String(100))
    humidity = Column(Float)
    writeDate = Column(DateTime)
    forcastDate = Column(DateTime)

class Weather(Base):
    __tablename__ = "weather"
    weatherId = Column(String(100), primary_key =True)
    country = Column(String(100))
    state = Column(String(100))
    score = Column(BIGINT(20))
    reasonBad = Column(String(100))
    compareTempSeoul = Column(String(100))
    rainDays = Column(BIGINT(20))
    placeAverage = Column(Float)
    seoulToday = Column(Float)
    description = Column(Text)
    title = Column(Text)
    lowTempPenalty = Column(Float)
    highTempPenalty = Column(Float)
    snowPenalty = Column(Float)
    rainPenalty = Column(Float)
    created = Column(DateTime)
    dateToShow = Column(DateTime)
    month = Column(BIGINT(20))