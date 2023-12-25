import yaml
import mysql.connector as mysql;
import streamlit as stl ;

with open('config.yaml', 'r') as f:
    configs = yaml.load(f, Loader=yaml.FullLoader)
    db_Credintials = configs['db']



def get_database_connection():
    db = mysql.connect( host = db_Credintials['host'],
        user = db_Credintials['user'],
        passwd = db_Credintials['passwd'],
        database = db_Credintials['database'],
        auth_plugin = db_Credintials['auth_plugin'])
        
    cursor = db.cursor()
    return cursor, db
                
def get_all_members(db, cursor):
	pass

def get_single_member(db, cursor):
	pass