import runpod
import subprocess
import requests
import time
import json

def check_api_availability(host):
    while True:
        try:
            response = requests.get(host)
            return
        except requests.exceptions.RequestException as e:
            print(f"API is not available, retrying in 200ms... ({e})")
        except Exception as e:
            print('something went wrong')
        time.sleep(200/1000)

check_api_availability("http://127.0.0.1:3000/sdapi/v1/txt2img")

print('run handler')

def handler(event):
    '''
    This is the handler function that will be called by the serverless.
    '''
    print('got event')
    print(event)

    apiResponse = ''

    if('params' in event['input']):

        if ('task' in event['input']) and (event['input']['task'] == 'img2img'):
            response = requests.post(
                url=f'http://127.0.0.1:3000/sdapi/v1/img2img', json=event['input']['params'])
        elif ('task' in event['input']) and (event['input']['task'] == 'extra'):
            response = requests.post(
                url=f'http://127.0.0.1:3000/sdapi/v1/extra-single-image', json=event['input']['params'])
        else:
            response = requests.post(
                url=f'http://127.0.0.1:3000/sdapi/v1/txt2img', json=event['input']['params'])

        apiResponse = response.json()
    
    result = {'result': apiResponse, 'request': event}

    # do the things
    print(result)

    # return the output that you want to be returned like pre-signed URLs to output artifacts
    return result


runpod.serverless.start({"handler": handler})