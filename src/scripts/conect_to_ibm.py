# -*- coding: utf-8 -*-
"""
@author: DiegoÁlvarez
"""

import boto3
import pandas as pd

import ibm_boto3
from ibm_botocore.client import Config, ClientError

#si se necesitan librerias, correr este comando

#pip install ibm-cos-sdk

    
class conect_to_ibm ():
    
    bucket_name = 'covidstudypublic-donotdelete-pr-vpm7tz8euu9ufn'
    
    def __init__(self):
        self.cos= ibm_boto3.resource("s3",
            ibm_api_key_id='Ykpx0He0ReyY8Gi4lTlIDA0Sl67PL067mJkFIZ6EFwNo',
            ibm_service_instance_id='crn:v1:bluemix:public:cloud-object-storage:global:a/ab3491678a354cef8c67c5ce7734eaeb:3c76ff27-8531-4e1b-9585-4adad2442443:bucket:covidstudypublic-donotdelete-pr-vpm7tz8euu9ufn',
            ibm_auth_endpoint="https://iam.cloud.ibm.com/oidc/token",
            config=Config(signature_version="oauth"),
            endpoint_url='https://s3.eu.cloud-object-storage.appdomain.cloud'
        )
        
    def get_bucket_contents(self):
        print("Retrieving bucket contents from: {0}".format(self.bucket_name))
        try:
            files = self.cos.Bucket(self.bucket_name).objects.all()
            for file in files:
                print("Item: {0} ({1} bytes).".format(file.key, file.size))
        except ClientError as be:
            print("CLIENT ERROR: {0}\n".format(be))
        except Exception as e:
            print("Unable to retrieve bucket contents: {0}".format(e))
            
    def get_item(self, item_name):
        print("Retrieving item from bucket: {0}, key: {1}".format(self.bucket_name, item_name))
        try:
            file = self.cos.Object(self.bucket_name, item_name).get()
            return file["Body"]
        except ClientError as be:
            print("CLIENT ERROR: {0}\n".format(be))
        except Exception as e:
            print("Unable to retrieve file contents: {0}".format(e))
        

            
    def put_item(self, item, nombre_fichero, is_csv):
        object = self.cos.Object('covidstudypublic-donotdelete-pr-vpm7tz8euu9ufn', nombre_fichero)
        if is_csv == 1:
            item_import = item.to_csv()
            object.put(Body=item_import.encode())
        else:
            object.put(Body=item_import.encode())