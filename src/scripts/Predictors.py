# -*- coding: utf-8 -*-
"""
@author: DiegoÁlvarez
"""

from conect_to_ibm import conect_to_ibm
import pickle
import pandas as pd

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
        
        #obtenemos las etiquetas empleadas en la clasificación
        connect = conect.get_item('cluster_labels.csv')
        if not hasattr(connect, "__iter__"): connect.__iter__ = types.MethodType( __iter__, connect )
        self.cluster_labels = pd.read_csv(connect)
        
        connect = conect.get_item('home_hospital_labels.csv')
        if not hasattr(connect, "__iter__"): connect.__iter__ = types.MethodType( __iter__, connect )
        self.home_hospital_labels = pd.read_csv(connect)
        
        connect = conect.get_item('again_hospital_labels.csv')
        if not hasattr(connect, "__iter__"): connect.__iter__ = types.MethodType( __iter__, connect )
        self.again_hospital_labels = pd.read_csv(connect)
        
        connect = conect.get_item('death_labels.csv')
        if not hasattr(connect, "__iter__"): connect.__iter__ = types.MethodType( __iter__, connect )
        self.death_labels = pd.read_csv(connect)
        
        
    def predict_cluster (self, data):
        return self.cluster_predictor.predict(data)
        
    def predict_proba_cluster (self, data):

        df = pd.DataFrame(data = self.cluster_predictor.predict_proba(data), columns = self.cluster_labels.to_numpy())
        return_df = df.stack().reset_index().rename(columns = {'level_1': 'Label', 0: 'Value'}).drop(['level_0'], axis = 1)
        return_df['Label'] = return_df['Label'].apply(lambda x: x[0])
        return return_df
    
    def predict_home_hospital (self, data):
        return self.home_hospital_predictor.predict(data)
        
    def predict_proba_home_hospital (self, data):
        
        df = pd.DataFrame(data = self.home_hospital_predictor.predict_proba(data), columns = self.home_hospital_labels.to_numpy())
        return_df = df.stack().reset_index().rename(columns = {'level_1': 'Label', 0: 'Value'}).drop(['level_0'], axis = 1)
        return_df['Label'] = return_df['Label'].apply(lambda x: x[0])
        return return_df

    
    def predict_again_hospital_predictor (self, data):
        return self.again_hospital_predictor.predict(data)
        
    def predict_proba_again_hospital_predictor (self, data):
        
        df = pd.DataFrame(data = self.again_hospital_predictor.predict_proba(data), columns = self.again_hospital_labels.to_numpy())
        return_df = df.stack().reset_index().rename(columns = {'level_1': 'Label', 0: 'Value'}).drop(['level_0'], axis = 1)
        return_df['Label'] = return_df['Label'].apply(lambda x: x[0])
        return return_df

    def predict_death_predictor (self, data):
        return self.death_predictor.predict(data)
        
    def predict_proba_death_predictor (self, data):
        
        df = pd.DataFrame(data = self.death_predictor.predict_proba(data), columns = self.death_labels.to_numpy())
        return_df = df.stack().reset_index().rename(columns = {'level_1': 'Label', 0: 'Value'}).drop(['level_0'], axis = 1)
        return_df['Label'] = return_df['Label'].apply(lambda x: x[0])
        return return_df
