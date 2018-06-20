from flask import Flask, render_template
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base();
class Stats(Base):
	__tablename__ = "stats"
	id = Column(Integer, primary_key=True, auto_increment=True)
	name = Column(String)
	played = Column(Integer)
	rated = Column(Integer)
	
	def __init__(self, name, played=0, rated=0):
		self.name = name
		self.played = played
		self.rated = rated
	

