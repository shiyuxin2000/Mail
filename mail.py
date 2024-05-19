from github import Github
import os
import codecs
def create(newfile):
    if not os.path.exists(newfile):
         f = open(newfile,'w')
       #  print newfile
         f.close()
    return

fileName='demo.txt'
respository='salesforce/Merlion'
mytoken = "mytoken"
g=Github(mytoken)

repo=g.get_repo(respository)
stargazers=repo.get_stargazers_with_dates()
create(fileName)
with codecs.open(fileName,'a', 'utf-8') as f:
    for people in stargazers:
        print (people.user.email)
        if people.user.email is not None:
            if people.user.name is None:
                name = people.user.email
            else:
                name = people.user.name
            data=(name)+":"+(people.user.email)+"\r\n"
            f.write(data)
