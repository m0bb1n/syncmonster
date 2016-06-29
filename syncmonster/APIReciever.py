import requests
import json

base_url='http://127.0.0.1:5000'

# MAKE SURE TO PASS ***user_id *** when authentication is setup #
#################################################################

def authenticateUser(email, password):
    url = base_url + '/AuthenticateUser?email=%s&password=%s' % (email, password)
    return (requests.post(url).content)
    
def getFiles(user_id):
    user_id = '1'
    url = base_url + '/GetAllFiles?user_id=%s' % user_id
    return (requests.get(url)).json()

def getAccounts(user_id):
    user_id = '1'
    url = base_url + '/GetAllAccounts?user_id=%s' % user_id
    return (requests.get(url)).json()

def deleteFile(file_id):
    url = base_url + '/DeleteFile?file_id=%s' % file_id
    r = requests.delete(url)
    

def AddAccount(user_id,name,token,type_):
    user_id = '1'
    url = base_url  + '/AddAccount?user_id=%s&type=%s&name=%s&token=%s' % (user_id,type_,name,token)
    r = requests.post(url)
    return r

def UploadFile(user_id, name, size, compression,password):
    user_id = '1'
    url = base_url + '/UploadFile?user_id=%s&name=%s&size=%s&compression=%s&password=%s' % (user_id, name, size, compression, password)
    r = requests.put(url)
    return r
