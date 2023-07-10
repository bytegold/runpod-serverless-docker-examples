#!/usr/bin/env python
''' Contains the handler function that will be called by the serverless. '''

import runpod
import os
import base64

# Load models into VRAM here so they can be warm between requests


def handler(event):
    '''
    This is the handler function that will be called by the serverless.
    '''
    print(event)

    # do the things
    if('image' in event['input']):
        inputData = bytes(event['input']['image'], 'utf-8')

        # first clean up old input png if it exists
        inputFilePath = 'input.png'
        if os.path.exists(inputFilePath):
            os.remove(inputFilePath)

        # write new input png
        with open(inputFilePath, "wb") as fh: 
            fh.write(base64.decodebytes(inputData))

        # generate output png
        outputFilePath = 'output.png'
        cmd = 'rembg i "' + inputFilePath + '" "' + outputFilePath + '"' 
        os.system(cmd);

        # read output svg
        with open(outputFilePath, 'rb') as file:
            base64Data = base64.b64encode(file.read())
            stringData = base64Data.decode('utf-8')
            print(stringData)
            return stringData

    # return the output that you want to be returned like pre-signed URLs to output artifacts
    return ''


runpod.serverless.start({"handler": handler})
