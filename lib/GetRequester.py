import requests
import json

class GetRequester:

    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        response=requests.get(self.url)
        return response.content

    def load_json(self):
        resp=[]
        progs=json.loads(self.get_response_body())
        for prog in progs:
            resp.append(prog)
        return resp

get_requester = GetRequester('https://learn-co-curriculum.github.io/json-site-example/endpoints/people.json')
data=get_requester.load_json()
print(data)