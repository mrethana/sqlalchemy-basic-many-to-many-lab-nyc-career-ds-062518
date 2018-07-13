from models import *

def return_christian_bales_roles(session):
    return session.query(Actor).filter_by(name = 'Christian Bale')[0].roles
    # Return a list of Christian Bale role instances

def return_catwoman_actors(session):
    return session.query(Role).filter_by(character = "Catwoman")[0].actors
    #  Return a list of actor instances that have played Catwoman

def return_number_of_batman_actors(session):
    batman = session.query(Role).filter_by(character = "Batman")[0].actors
    return len(batman)
    # Return the number of actors that have played Batman
