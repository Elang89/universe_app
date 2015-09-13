'''
Created on Sep 7, 2015

@author: Cassandra
'''

import uuid
from cassandra.cluster import Cluster

class Galaxy(object):
    
    def __init__(self, cluster="", session=""):
        self.cluster = Cluster()
        self.session = self.cluster.connect('universe_data')
    #
    def create(self, galaxy_name, event_descrpition):
        query = self.session.prepare("INSERT INTO galactic_event(id_galactic_event,galaxy_name,event_description,Earth_time)VALUES(now(),?,?,dateof(now()))")
        statement = query.bind([galaxy_name,event_descrpition])
        self.session.execute(statement)
    #
    def update_event_description(self, id_galactic_event, event_description):
        id_event = uuid.UUID(id_galactic_event)
        query = self.session.prepare("UPDATE galactic_event SET event_description = ? WHERE id_galactic_event = ? ")
        statement = query.bind([event_description, id_event])
        self.session.execute(statement);
    #
    def show(self, id_galactic_event):
        if bool or id_galactic_event == "":
            query = self.session.prepare("SELECT * FROM galactic_event")
            statement = query
        else:
            id_event = uuid.UUID(id_galactic_event="")
            query = self.session.prepare("SELECT * FROM galactic_event WHERE (id_galaxy = ?) AND (shape = ?)")
            statement = query.bind([id_event])
        end_result = self.session.execute(statement)
        return end_result;
    #
    def delete_event(self, id_galactic_event):
        id_event = uuid.UUID(id_galactic_event)
        query = self.session.prepare("DELETE FROM galactic_event WHERE id_galactic_event = ?")
        statement = query.bind([id_event]);
        self.session.execute(statement);