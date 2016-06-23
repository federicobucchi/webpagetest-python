# import required modules
import requests
import threading

# import project modules
import config

# vars
assets = {}

# Call runtest url in webpagetest
response_runtest = requests.get(config.service_url + '/' + config.runtest_file + '?url=' + config.test_url + '&k=' + config.webtest_api_key + '&f=json&location=' + config.location)
json_url = response_runtest.json()['data']['jsonUrl']

def check_test_complete():
    response_test_complete = requests.get(json_url)
    if (response_test_complete.json()['statusCode'] == 101) or (response_test_complete.json()['statusCode'] == 100):
        threading.Timer(2, check_test_complete).start()
    else:
        assets_breakdown = response_test_complete.json()['data']['median']['firstView']['breakdown']
        assets['js'] = assets_breakdown['js']['requests']
        assets['css'] = assets_breakdown['css']['requests']
        assets['images'] = assets_breakdown['image']['requests']
        assets['fonts'] = assets_breakdown['font']['requests']
        print assets

check_test_complete()
