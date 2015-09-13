'''
Created on Sep 7, 2015

@author: Cassandra
'''
import uuid
from cassandra.cluster import Cluster

class Star(object):

    def __init__(self, cluster="", session=""):
        self.cluster = Cluster()
        self.session = self.cluster.connect('universe_data')
    #
    def create(self, star_name, planetary_system, event_descrpition):
        query = self.session.prepare("INSERT INTO stellar_event(id_stellar_event,star_name,planetary_system, event_description,Earth_time)VALUES(now(),?,?,?,dateof(now()))")
        statement = query.bind([star_name,planetary_system,event_descrpition])
        self.session.execute(statement)
    #
    def update_event_description(self, id_stellar_event, star_name="", event_description=""):
        id_event = uuid.UUID(id_stellar_event)
        query =""
        statement = ""
        if star_name == "" and event_description != "":
            query = self.session.prepare("UPDATE stellar_event SET event_description = ? WHERE id_stellar_event = ? ")
            statement = query.bind([event_description, id_event])
        if star_name != "" and event_description == "":
            query = self.session.prepare("UPDATE stellar_event SET star_name = ? WHERE id_stellar_event = ? ")
            statement = query.bind([star_name, id_event])
        else:
            query = self.session.prepare("UPDATE stellar_event SET star_name = ?, event_description = ? WHERE id_stellar_event = ? ")
            statement = query.bind([star_name,event_description, id_event])
        self.session.execute(statement);
    #
    def show(self, id_stellar_event):
        if bool or id_stellar_event == "":
            query = self.session.prepare("SELECT * FROM stellar_event")
            statement = query
        else:
            id_event = uuid.UUID(id_stellar_event="")
            query = self.session.prepare("SELECT * FROM stellar_event WHERE (id_planet = ?) AND (shape = ?)")
            statement = query.bind([id_event])
        end_result = self.session.execute(statement)
        return end_result
    #
    def delete_event(self, id_stellar_event):
        id_event = uuid.UUID(id_stellar_event)
        query = self.session.prepare("DELETE FROM stellar_event WHERE id_stellar_event = ?")
        statement = query.bind([id_event]);
        self.session.execute(statement);