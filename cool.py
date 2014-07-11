import  os, requests
familybotid = "a2dc0da36676eec3febf7df4de"
funguys = "db6fba2dad56160da5223dcdf0"
 
def groupmesend(botid, message2group):
	website = "https://api.groupme.com/v3/bots/post"
	botparams = {
		"bot_id"  : botid,
		"text"    : message2group
	}
	requests.post(website, data = botparams)

def family():
	groupmesend(familybotid, "No one cares")
					
 
if __name__ == "__main__":
	family() 
