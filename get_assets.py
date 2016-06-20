# import required modules
import requests
import threading
import ast

# import project modules
import config

# vars
assets = {
    'total': 0
}

# Call runtest url in webpagetest
response_runtest = requests.get(config.service_url + '/' + config.runtest_file + '?url=' + config.test_url + '&k=' + config.webtest_api_key + '&f=json')
json_url = response_runtest.json()['data']['jsonUrl']

def f():
    print 'start'
    response_again = requests.get(json_url)
    if (response_again.json()['statusCode'] == 101) or (response_again.json()['statusCode'] == 100):
        threading.Timer(2, f).start()
    else:
        print 'done'
        for record in response_again.json():
            print record.data
            #for attr, value in ast.literal_eval(record).iteritems():
                #if (attr == 'host') and (value == 'gopro.com'):
                    #print 'found'
                    #assets['total'] += 1

        #print assets['total']

f()

# LOOP ALL RESULT ADDING to RESULT
# Num. of JS files
# Num. of CSS files
# Num. of Images files
# Num. of fonts files