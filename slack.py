import requests
def get_key():
	fo = open('token.txt', 'r')
	line = fo.read()
	return line
	
def make_call(key, call):
	payload = {'token':key}
	r = requests.get('http://slack.com/api/'+call, params=payload)
	print r.json()

def main():
	key = get_key()
	make_call(key, 'channels.list')
if __name__ == '__main__':
	main()