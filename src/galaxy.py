'''
Created on Sep 4, 2015

@author: Cassandra
'''
import uuid
from cassandra.cluster import Cluster

class Galaxy(object):
    
    def __init__(self, cluster="", session=""):
        self.cluster = Cluster()
        self.session = self.cluster.connect('universe_data')
        self.id_galaxy = ""
        self.shape = ""
        self.galaxy_name = ""
        self.star = ""
        self.planet = ""
        self.nebula = ""
    #
    def create(self, shape, name):
        query = self.session.prepare("INSERT INTO galaxy(id_galaxy, shape, galaxy_name)VALUES(now(),?,?)")
        statement = query.bind([shape,name])
        self.session.execute(statement)
        self.clear(shape, name)
    #
    def clear(self,*args):
        for i in args: 
            self.i = ""
    #
    def add_planet_nebula_star(self, id_galaxy, shape, planet="", nebula="", star=""):
        self.id_galaxy = uuid.UUID(id_galaxy)
        self.shape = shape 
        if planet != "" and nebula == "" and star == "":
            query = self.session.prepare("UPDATE galaxy SET planet = ? WHERE (id_galaxy = ?) AND (shape = ?)")
            statement = query.bind([planet,self.id_galaxy,self.shape])
        elif nebula != "" and planet == "" and star == "":
            query = self.session.prepare("UPDATE galaxy SET nebula = ? WHERE (id_galaxy = ?) AND (shape = ?)")
            statement = query.bind([nebula,self.id_galaxy,self.shape])
        elif star != "" and planet == "" and nebula == "":
            query = self.session.prepare("UPDATE galaxy SET nebula = ? WHERE (id_galaxy = ?) AND (shape = ?)")
            statement = query.bind([star,self.id_galaxy,self.shape])
        elif planet != "" and nebula != "" and star == "":
            query = self.session.prepare("UPDATE galaxy SET planet = ?, nebula = ? WHERE (id_galaxy = ?) AND (shape = ?)")
            statement = query.bind([planet,nebula,self.id_galaxy,self.shape])
        elif planet != "" and star != "" and nebula == "":
            query = self.session.prepare("UPDATE galaxy SET planet = ?, star = ? WHERE (id_galaxy = ?) AND (shape = ?)")
            statement = query.bind([planet,star,self.id_galaxy,self.shape])
        elif nebula != "" and star != "" and planet == "":
            query = self.session.prepare("UPDATE galaxy SET nebula = ?, star = ? WHERE (id_galaxy = ?) AND (shape = ?)")
            statement = query.bind([nebula,star,self.id_galaxy,self.shape])
        else: 
            query = self.session.prepare("UPDATE galaxy SET planet = ?, nebula = ?, star = ?  WHERE (id_galaxy = ?) AND (shape = ?)")
            statement = query.bind([planet,nebula,star,self.id_galaxy,self.shape])
        self.session.execute(statement)
    #
    def show(self,bool, id_galaxy="", shape=""):
        if bool or id_galaxy == "" or shape =="":
            query = self.session.prepare("SELECT * FROM galaxy")
            statement = query
        else:
            self.id_galaxy = uuid.UUID(id_galaxy)
            self.shape = shape
            query = self.session.prepare("SELECT * FROM galaxy WHERE (id_galaxy = ?) AND (shape = ?)")
            statement = query.bind([self.id_galaxy,self.shape])
        end_result = self.session.execute(statement)
        return end_result