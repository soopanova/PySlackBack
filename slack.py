import requests
def get_key():
    with open('token.txt', 'r') as f:
        line = f.read()
    return line
    
def make_call(key, call):
    payload = {'token':key}
    r = requests.get('http://slack.com/api/'+call, params=payload)
    print r.json()

def main():
    key = get_key()
    #print key
    make_call(key, 'channels.list')
if __name__ == '__main__':
    main()