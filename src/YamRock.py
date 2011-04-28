import sys, httplib, simplejson

yamconn = httplib.HTTPSConnection("www.yammer.com")
yamconn.request("GET", "/api/v1/users.json?access_token=NeEc1ud9UnnWpDeegzs2g")
userlist = yamconn.getresponse()

userdata=userlist.read()
users = simplejson.loads(userdata)

print "\r"

for user in users:
	if user['verified_admin'] == 'true':
		user_status = 'Verified Admin'
	elif user['admin'] == 'true':
		user_status = 'Admin'
	else:
		user_status = 'Standard User'

	print "\r"
	print user['full_name'] + ", " + str(user['id'])
	print "\r"

	print "Username: \t \t" + str(user['name'])
	print "Email address: \t \t" + str(user['contact']['email_addresses'][0]['address'])
	print "Job Title: \t \t" + str(user['job_title']) 
	print "State: \t \t \t" + str(user['state'])
	print "Status: \t \t" + user_status
	print "Profile URL: \t \t" + str(user['web_url'])
	print "Photo URL: \t \t" + str(user['mugshot_url'])
	print "Following: \t \t" + str(user['stats']['following'])
	print "Followers: \t \t" + str(user['stats']['followers'])

	print "\r"

yamconn.close()