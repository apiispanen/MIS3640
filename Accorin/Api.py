import requests
import json
import urllib
#url = 'https://api.harvestapp.com/api/v2/users/me.json'
#headers = {'Harvest-Account-ID': '564947', 'Authorization':'Bearer 1394475.pt.LGPWqst-aA_J3P1Wz4_q-qHEcHRcVKRQ8zZhidxjjSRh83dPz1AxgQYrVZss1-ibpXE2rBph6N1G8WbD2TdqAA','User-Agent':'Harvest API Example'}
#r=requests.get(url,headers=headers)
#print (r.status_code)
#print (r.headers['content-type'])
#print(r.text)

url = 'https://api.harvestapp.com/api/v2/projects'
headers={'Authorization':'Bearer 1394475.pt.LGPWqst-aA_J3P1Wz4_q-qHEcHRcVKRQ8zZhidxjjSRh83dPz1AxgQYrVZss1-ibpXE2rBph6N1G8WbD2TdqAA','Harvest-Account-Id': '564947','User-Agent':'MyApp (andrewp@accorin.com'}
t=requests.get(url, headers=headers)
#print (t.status_code)
#print (t.headers['content-type'])
#print(t.text)

proj_json = t.json()['projects']

print('ID                Project Name ')
for project in proj_json:
   print('{}           {} '.format(project['id'],project['name']))

for project in proj_json:
    if project['name'][0]=='A':
        print (project['name'])

# import pdb; pdb.set_trace()
print(t.json()['projects'][0]['id'])

#Function finds the projects THAT BEGIN WITH NAME INPUT

def search(name):
    for element in t.json()['projects']:
        if element['name'][0:(len(name))] == name:
            print(element)
search('AmorePacific Retainer')

#print(t.json()['projects'][0]['name'])

#print('')
#print(t.json()['projects'][1])
#def Lookup(PM_Name):
#    for users in user_json:
 #       if users['name']==PM_Name:
  #          print (users['name'])

#Lookup('Sunil Patel')



#Loop through users to find each project 