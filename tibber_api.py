import os
import requests
import json

class Tibber:

    def __init__(self, token):
        self.token = token

    def req_price(self):
        baseURL = 'https://api.tibber.com/v1-beta/gql'
        token = self.token
        query = '{viewer{homes{currentSubscription{priceInfo{current{total,energy,tax,startsAt}today{total,energy,tax,startsAt}tomorrow{total,energy,tax,startsAt}}}}}}'
        requestURL = f"{baseURL}?token={token}&query={query}"
        r = requests.get(requestURL)

        return json.loads(r.content)



    def curr_price(self):

        token = self.token
        query = '{ "query": "{viewer {homes {currentSubscription {priceInfo {current {total energy tax startsAt } today {total energy tax startsAt }}}}}}" }'

        r = f'curl -H "Authorization: Bearer {token}" -H "Content-Type: application/json" -X POST -d  \'{query}\' https://api.tibber.com/v1-beta/gql'
        os.system(r)
