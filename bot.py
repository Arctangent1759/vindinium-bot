import urllib
import urllib2
import json

kKey = 'j0tzveqn'
kVindiniumURL = 'http://vindinium.org/api/training'
#kVindiniumURL = 'http://vindinium.org/api/arena'

class Vindinium:
    def __init__(self):
        pass
    def HTTPPost(self, url, key_val_dict):
        data = urllib.urlencode(key_val_dict)
        req = urllib2.Request(url, data)
        res = urllib2.urlopen(req)
        return res.read()
    def CartCoordsToMove(self, x, y):
        if x == 0 and y == 0:
            return 'Stay'
        elif x == 1 and y == 0:
            return 'East'
        elif x == -1 and y == 0:
            return 'West'
        elif x == 0 and y == 1:
            return 'North'
        elif x == 0 and y == -1:
            return 'South'
        else:
            assert False, 'Invalid move command.'
    def Start(self):
        res = self.HTTPPost(kVindiniumURL, {'key':kKey})
        json_res = json.loads(res)
        self.play_url = json_res["playUrl"]
        self.view_url = json_res["viewUrl"]
        return json_res
    def Move(self, x, y):
        print self.CartCoordsToMove(x,y)
        return json.loads(self.HTTPPost(self.play_url, {'key':kKey, 'dir':self.CartCoordsToMove(x,y)}))

v = Vindinium()
v.Start()
print v.view_url
while True:
    print v.Move(1,0)["game"]["board"]["tiles"]
    print v.Move(-1,0)["game"]["board"]["tiles"]
    print v.Move(0,1)["game"]["board"]["tiles"]
    print v.Move(0,-1)["game"]["board"]["tiles"]

