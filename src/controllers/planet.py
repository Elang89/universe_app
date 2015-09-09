'''
Created on Sep 7, 2015

@author: Cassandra
'''
import uuid
from cassandra.cluster import Cluster

class Planet(object):

    def __init__(self, cluster="", session=""):
        self.cluster = Cluster()
        self.session = self.cluster.connect('universe_data')
    #
    def create(self, planet_name, event_name, event_descrpition):
        query = self.session.prepare("INSERT INTO planetary_event(id_planetary_event,planet_name,event_name, event_description,Earth_time)VALUES(now(),?,?,?,dateof(now()))")
        statement = query.bind([planet_name,event_name,event_descrpition])
        self.session.execute(statement)
    #
    def update_event_description(self, id_planetary_event, event_description):
        id_event = uuid.UUID(id_planetary_event)
        query = self.session.prepare("UPDATE planetary_event SET event_description = ? WHERE id_planetary_event = ? ")
        statement = query.bind([event_description, id_event])
        self.session.execute(statement);
    #
    def show(self, id_planetary_event):
        if bool or id_planetary_event == "":
            query = self.session.prepare("SELECT * FROM planetary_event")
            statement = query
        else:
            id_event = uuid.UUID(id_planetary_event="")
            query = self.session.prepare("SELECT * FROM planetary_event WHERE (id_planet = ?) AND (shape = ?)")
            statement = query.bind([id_event])
        end_result = self.session.execute(statement)
        return end_result
    #
    def delete_event(self, id_planetary_event):
        id_event = uuid.UUID(id_planetary_event)
        query = self.session.prepare("DELETE FROM planetary_event WHERE id_planetary_event = ?")
        statement = query.bind([id_event]);
        self.session.execute(statement);
       
        