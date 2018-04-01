import requests
import argparse
import json
from requests.auth import HTTPBasicAuth
import logging
from httplib import HTTPConnection


if __name__ == "__main__":

	parser = argparse.ArgumentParser()
	parser.add_argument("username")
	parser.add_argument("password")
	parser.add_argument("httpHostColonPort")
	parser.add_argument("calling")
	parser.add_argument("called")
	parser.add_argument("--http",action="store_true")
	parser.add_argument("--json",action="store_true")

	args = parser.parse_args()

	if args.http:
		HTTPConnection.debuglevel = 1
		logging.basicConfig() 
		logging.getLogger().setLevel(logging.DEBUG)
		requests_log = logging.getLogger("requests.packages.urllib3")
		requests_log.setLevel(logging.DEBUG)
		requests_log.propagate = True

	klRootUrlHttp="https://"+args.httpHostColonPort
	klRestUserRootUrl=klRootUrlHttp+"/rest/version/1/user/"+args.username+"/"

	c2cRequest={}
	c2cRequest["callingParty"]=args.calling
	c2cRequest["calledParty"]=args.called
	c2cRequest={"clickToCallRequest":c2cRequest}
	if args.json:
		print c2cRequest

	response=requests.post(klRestUserRootUrl+"clicktocall",json=c2cRequest,auth=HTTPBasicAuth(args.username,args.password))

	if not response.status_code==200:
		print response
	else:
		if args.json:
			print response.json()
		print response.json()["ctcResponse"]["statusCode"]
