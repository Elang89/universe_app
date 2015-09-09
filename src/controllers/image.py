'''
Created on Sep 7, 2015

@author: Cassandra
'''

import uuid
from cassandra.cluster import Cluster

class Image(object):

    def __init__(self, cluster="", session=""):
        self.cluster = Cluster()
        self.session = self.cluster.connect('universe_data')
    #
    def create(self, name, contents):
        file = open(contents,'r')
        file_content = file.read()
        file.close()
        query = self.session.prepare("INSERT INTO image_table(image_id,name,contents,Earth_time)VALUES(now(),?,?,dateof(now()))")
        statement = query.bind([name,file_content])
        self.session.execute(statement)
    #
    def update_image_name(self, image_id, name):
        image_id = uuid.UUID(image_id)
        query = self.session.prepare("UPDATE image_table SET name = ? WHERE image_id = ? ")
        statement = query.bind([name])
        self.session.execute(statement);
    #
    def show(self, image_id):
        if bool or image_id == "":
            query = self.session.prepare("SELECT * FROM image_table ")
            statement = query
        else:
            image_id = uuid.UUID(image_id)
            query = self.session.prepare("SELECT * FROM image_table WHERE (image_id = ?)")
            statement = query.bind([image_id])
        end_result = self.session.execute(statement)
        return end_result
    #
    def delete_event(self, image_id):
        image_id = uuid.UUID(image_id)
        query = self.session.prepare("DELETE FROM image_table WHERE image_id = ?")
        statement = query.bind([image_id]);
        self.session.execute(statement);