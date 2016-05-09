import requests
from pprint import pprint
def get_key():
    with open('token.txt', 'r') as f:
        line = f.read()
    return line
    
def make_call(key, call):
    payload = {'token':key}
    r = requests.get('http://slack.com/api/'+call, params=payload)
    print r.json()

def test_token(token):
    payload = {'token':token}
    r = requests.get('https://slack.com/api/auth.test', params=payload)
    results = r.json()
    #print results['ok']
    
    if results['ok'] == True:
        print 'Token is valid'
    else:
        print 'Token is invalid'

def main():
    key = get_key()
    #print key
    #make_call(key, 'channels.list')
    test_token(key)
if __name__ == '__main__':
    main()