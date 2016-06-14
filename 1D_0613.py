# -*- coding: utf-8 -*-
"""
Created on Mon Jun 13 10:51:16 2016

@author: xinruyue
"""
from pymongo import MongoClient
import datetime

event = MongoClient("10.8.8.111:27017")['eventsV35']['eventV35']

endTime = datetime.date.today()-datetime.timedelta(hours = 8)
timeDelta = datetime.timedelta(weeks = 1)
startTime = endTime - timeDelta

#prologue and epilogue pv
def get_pv(eventKey,videoId):
    if type(videoId) == list:
        pv = event.find({"eventKey":eventKey,"eventValue.videoId":{"$in":videoId},
        "serverTime":{"$gte":startTime,"$lte":endTime}}).count()
    else:
        pv = event.find({"eventKey":eventKey,"eventValue.videoId":videoId,
        "serverTime":{"$gte":startTime,"$lte":endTime}}).count()
    print eventKey + '-' + videoId + ':' + str(pv)
    return pv

pro_skip = get_pv("clickPVSkip",["prologueA","prologueP"])

epi_skip = get_pv("clickEVSkip",["epilogueA","epilogueP"])

prologue_pv = get_pv("enterVideo",["prologueA","prologueP"])

epilogue_pv = get_pv("enterVideo","epilogueA")

pro_ratio = float(pro_skip)/prologue_pv
print pro_ratio
epi_ratio = float(epi_skip)/epilogue_pv
print epi_ratio
