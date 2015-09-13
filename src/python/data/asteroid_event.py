'''
Created on Sep 7, 2015

@author: Cassandra
'''
import uuid
from cassandra.cluster import Cluster

class Asteroid(object):

    def __init__(self, cluster="", session=""):
        self.cluster = Cluster()
        self.session = self.cluster.connect('universe_data')
    #
    def create(self, asteroid_size, planet, planetary_system, event_descrpition):
        query = self.session.prepare("""INSERT INTO asteroid_impact(id_asteroid_event,asteroid_size, planet, planetary_system, 
        event_description,Earth_time)VALUES(now(),?,?,?,?,dateof(now()))""")
        statement = query.bind([asteroid_size,planet,planetary_system,event_descrpition])
        self.session.execute(statement)
    #
    def update_event_description(self, id_asteroid_event, planet="", planetary_system="", event_description=""):
        query = ""
        statement = ""
        id_event = uuid.UUID(id_asteroid_event)
        if planet == "" and planetary_system == "" and event_description != "":
            query = self.session.prepare("UPDATE asteroid_impact SET event_description = ? WHERE id_asteroid_event = ? ")
            statement = query.bind([event_description, id_event])
        elif planet != "" and planetary_system == "" and event_description =="":
            query = self.session.prepare("UPDATE asteroid_impact SET planet = ? WHERE id_asteroid_event = ? ")
            statement = query.bind([planet, id_event])
        elif planet == "" and planetary_system != "" and event_description == "":
            query = self.session.prepare("UPDATE asteroid_impact SET planetary_system = ? WHERE id_asteroid_event = ? ")
            statement = query.bind([planetary_system, id_event])
        elif planet != "" and planetary_system != "" and event_description == "":
            query = self.session.prepare("UPDATE asteroid_impact SET planet = ?, planetary_system = ? WHERE id_asteroid_event = ? ")
            statement = query.bind([planet, planetary_system,id_event])
        elif planet == "" and planetary_system != "" and event_description != "":
            query = self.session.prepare("UPDATE asteroid_impact SET planet = ?, event_description = ? WHERE id_asteroid_event = ? ")
            statement = query.bind([planet,event_description,id_event])
        else:
            query = self.session.prepare("UPDATE asteroid_impact SET planet = ?, planetary_system = ?, event_description = ? WHERE id_asteroid_event = ? ")
            statement = query.bind([planet,planetary_system,event_description,id_event])
        self.session.execute(statement);
    #
    def show(self, id_asteroid_event):
        if bool or id_asteroid_event == "":
            query = self.session.prepare("SELECT * FROM asteroid_impact")
            statement = query
        else:
            id_event = uuid.UUID(id_asteroid_event="")
            query = self.session.prepare("SELECT * FROM asteroid_impact WHERE (id_planet = ?) AND (shape = ?)")
            statement = query.bind([id_event])
        end_result = self.session.execute(statement)
        return end_result
    #
    def delete_event(self, id_asteroid_event):
        id_event = uuid.UUID(id_asteroid_event)
        query = self.session.prepare("DELETE FROM asteroid_impact WHERE id_asteroid_event = ?")
        statement = query.bind([id_event]);
        self.session.execute(statement);