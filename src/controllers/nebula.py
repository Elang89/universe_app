'''
Created on Sep 7, 2015

@author: Cassandra
'''

import uuid
from cassandra.cluster import Cluster

class Nebula(object):

    def __init__(self, cluster="", session=""):
        self.cluster = Cluster()
        self.session = self.cluster.connect('universe_data')
    #
    def create(self, nebula_name, nebula_type, event_descrpition):
        query = self.session.prepare("INSERT INTO nebula_event(id_nebula_event,nebula_name,nebula_type, event_description,Earth_time)VALUES(now(),?,?,?,dateof(now()))")
        statement = query.bind([nebula_name,nebula_type,event_descrpition])
        self.session.execute(statement)
    #
    def update_event_description(self, id_nebula_event, nebula_name="", nebula_type="", event_description=""):
        id_event = uuid.UUID(id_nebula_event)
        query =""
        statement = ""
        if nebula_name == "" and nebula_type == "" and event_description != "":
            query = self.session.prepare("UPDATE nebula_event SET event_description = ? WHERE id_nebula_event = ? ")
            statement = query.bind([event_description, id_event])
        elif nebula_name != "" and nebula_type == "" and event_description == "":
            query = self.session.prepare("UPDATE nebula_event SET nebula_name = ? WHERE id_nebula_event = ? ")
            statement = query.bind([nebula_name, id_event])
        elif nebula_name == "" and nebula_type != "" and event_description =="":
            query = self.session.prepare("UPDATE nebula_event SET nebula_type = ? WHERE id_nebula_event = ? ")
            statement = query.bind([nebula_type, id_event])
        elif nebula_name != "" and nebula_type != "" and event_description == "":
            query = self.session.prepare("UPDATE nebula_event SET nebula_name = ?, nebula_type = ? WHERE id_nebula_event = ? ")
            statement = query.bind([nebula_name, nebula_type, id_event])
        elif nebula_name == "" and nebula_type != "" and event_description !="":
            query = self.session.prepare("UPDATE nebula_event SET nebula_type = ?, event_description = ? WHERE id_nebula_event = ? ")
            statement = query.bind([nebula_name, event_description, id_event])
        elif nebula_name != "" and nebula_type=="" and event_description != "":
            query = self.session.prepare("UPDATE nebula_event SET nebula_name = ?, event_description = ? WHERE id_nebula_event = ? ")
            statement = query.bind([nebula_type, event_description, id_event])
        else:
            query = self.session.prepare("UPDATE nebula_event SET nebula_name = ?, nebula_type = ?, event_description = ? WHERE id_nebula_event = ? ")
            statement = query.bind([nebula_name, nebula_type, event_description, id_event])
        self.session.execute(statement);
    #
    def show(self, id_nebula_event):
        if bool or id_nebula_event == "":
            query = self.session.prepare("SELECT * FROM nebula_event")
            statement = query
        else:
            id_event = uuid.UUID(id_nebula_event="")
            query = self.session.prepare("SELECT * FROM nebula_event WHERE (id_planet = ?) AND (shape = ?)")
            statement = query.bind([id_event])
        end_result = self.session.execute(statement)
        return end_result
    #
    def delete_event(self, id_nebula_event):
        id_event = uuid.UUID(id_nebula_event)
        query = self.session.prepare("DELETE FROM nebula_event WHERE id_nebula_event = ?")
        statement = query.bind([id_event]);
        self.session.execute(statement);