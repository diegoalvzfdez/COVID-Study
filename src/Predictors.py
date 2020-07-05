# -*- coding: utf-8 -*-
"""
@author: DiegoÁlvarez
"""

from conect_to_ibm import conect_to_ibm
import pickle

class Predictors():
    
    def __init__(self):
        
        conect = conect_to_ibm()
        
        #descargamos el predictor que nos determina los Clusters
        connect = conect.get_item('scores_cluster.pkl')
        self.cluster_predictor = pickle.loads(connect.read())
        
        #descargamos el predictor que nos determina si se debe de dar de alta un paciente
        connect = conect.get_item('scores_home_hospital.pkl')
        self.home_hospital_predictor = pickle.loads(connect.read())
        
        #descargamos el predictor que nos determina si un paciente va a recaer
        connect = conect.get_item('scores_again_hospital.pkl')
        self.again_hospital_predictor = pickle.loads(connect.read())
        
        #descargamos el predictor que nos determina si un paciente muere en planta
        connect = conect.get_item('scores_death.pkl')
        self.death_predictor = pickle.loads(connect.read())
        
        
    def predict_cluster (self, data):
        return self.cluster_predictor.predict(data)
        
    def predict_proba_cluster (self, data):
        return self.cluster_predictor.predict_proba(data)
    
    def predict_home_hospital (self, data):
        return self.home_hospital_predictor.predict(data)
        
    def predict_proba_home_hospital (self, data):
        return self.home_hospital_predictor.predict_proba(data)
    
    def predict_again_hospital_predictor (self, data):
        return self.again_hospital_predictor.predict(data)
        
    def predict_proba_again_hospital_predictor (self, data):
        return self.again_hospital_predictor.predict_proba(data)

    def predict_death_predictor (self, data):
        return self.death_predictor.predict(data)
        
    def predict_proba_death_predictor (self, data):
        return self.death_predictor.predict_proba(data)