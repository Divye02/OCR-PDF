import httplib, urllib, base64
import json
import time

length = 291 + 1;

headers = {
    # Request headers
    'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Key': 'eb1d0ddbe2e04a9e931222d193af240b',
}

params = urllib.urlencode({
    # Request parameters
    'language': 'unk',
    'detectOrientation ': 'true',
})
data = [];
conn = httplib.HTTPSConnection('api.projectoxford.ai')
for i in range(0, length):
    try:
        if (i+1) % 20 == 0:
            time.sleep(46)
        conn.request("POST", "/vision/v1/ocr?%s" % params, "{'Url': 'http://divye02.github.io/OCR-PDF/test/page-" + str(i) + ".jpg'}", headers)
        response = conn.getresponse()
        data.append({'page' : i, 
                    'content' : json.loads(response.read())
                    })
        #print(data)
    except Exception as e:
        print("[Errno {0}] {1}".format(e.errno, e.strerror))

conn.close()

with open('data.json', 'w') as outfile:
    json.dump(data, outfile)