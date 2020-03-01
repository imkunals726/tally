import boto3
import botocore
from boto3.s3.transfer import S3Transfer
import uuid
from datetime import datetime, timedelta
import requests, json, ast, sys, os
from django.core import serializers


import re



AWS_ACCESS_KEY_ID       = "AKIAIT7XRXKXPTGHUPWA"
AWS_SECRET_ACCESS_KEY   = "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"
BUCKET_NAME             = "ritesh"
AWS_HOST                = "ritesh.s3.ap-south-1.amazonaws.com"#http://ritesh.s3-website.ap-south-1.amazonaws.com


def uploadFileToS3( fileName, brand = 'ALL' , report = 'cost' , LANG = 'en-US', objectACL='public-read'):
    '''
    Takes in arguments like brand and report to create the folders `brand/reportYYYY-MM-DDTHH:MM`
    Takes in the local path of the filename and splits it into filename and extension
    S3 Location : `brand/reportYYYY-MM-DDTHH:MM/fileName`
    Response will have FileURL and other necessary details.
    '''
    # lang_message_json = languages.MESSAGE[LANG]
    print( fileName , 'atfirst')
    try:
        datetime_now = datetime.now().strftime('%d-%b-%Y')
        file = fileName.split("/")[-1:]
        extension = str(str(file).strip('[\']').split(".")[-1:]).strip('[\']')
        if extension == 'zip':
            fileNameExt = (str(file[0][:-4]) + "-" + str(uuid.uuid4()) + '.zip').replace(' ', '')
        else:
            fileNameExt = (str(file[0][:-(len(extension)+1)]) + "-" + datetime_now + "-" + str(uuid.uuid4())[-8:] + '.' + str(extension)).replace(' ', '')
        path = (str(brand) + "/" + str(report) + datetime_now).replace(' ', '')
        location = (path + "/" + fileNameExt).replace(' ', '')

        s3 = boto3.resource('s3', aws_access_key_id=AWS_ACCESS_KEY_ID, aws_secret_access_key=AWS_SECRET_ACCESS_KEY)
        print( 'fff' , fileName )
        response = s3.Object(BUCKET_NAME, location).upload_file(fileName)
        print( 'done' )
        object_acl = s3.ObjectAcl(BUCKET_NAME,location)
        if objectACL=='public-read':
            responseACL = object_acl.put(ACL=objectACL) 
 

        file_url = "http://%s/%s" % (AWS_HOST, location) # Generate URL for download
        return ({
                    "success": True,
                    "msg": "S3 URL for " + report,
                    "message": "S3 URL for " + report,
                    "data":{
                            "Report" : report,
                            "fileURL" : file_url,
                    }
            })
    except Exception as e:
        print(e)
        return({
                "success" : False,
                "data":[],
                "message": "Something went wrong while creating URL in 'uploadFileToS3()': " + str(e)
                })
