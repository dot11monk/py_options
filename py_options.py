import requests

#r = requests.options('URL')
#print (r.text)
with open('path_to_dictionary','r') as f:
    for line in f:
        for word in line.split():
           r = requests.head('URL'+word)
           if r.status_code !=404:
            print r.status_code
           else
               print r.raw

               response = urllib.request.urlopen(newurl)
    with open("Page/" + x, "a") as p:
        p.writelines(reponse.read())
