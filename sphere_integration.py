##
# This class is responsible for instantiating the sphere engine python client
#
# Using this class eliminates the need to deal with sphere engine calls and logic
# and makes easier to focus on the functional requirements
#
# Usage: see bottom of file
# 
##
import os

import requests
from flask_restful import abort

AUTH_TOKEN = os.getenv('SPHERE_AUTH')
ENDPOINT = os.getenv('SPHERE_ENDPOINT')
SPHERE_STATUS_MAPPING = ["finished", "compilation", "running"]
SPHERE_ERR_MAPPING = {
    11: "compilation error",
    12: "runtime error",
    13: "time limit exceeded",
    17: "memory limit exceeded",
    19: "forbidden system call",
    20: "not your fault error",
}


def submit(source, input="", lang=4):
    url = ENDPOINT + '/api/v3/submissions/?access_token=' + AUTH_TOKEN
    headers = {
        "Content-Type": 'application/json'
    }
    content = {
        "compilerId": lang,
        "sourceCode": source,
        "input": input
    }
    print(content)
    response = requests.post(url, headers=headers, json=content)

    if response.status_code != 201:
        print(response.content)
        print(response.status_code)
        abort(502)
    return response.json()["id"]


def poll(id):
    url = ENDPOINT + '/api/v3/submissions/' + id
    params = {
        "access_token": AUTH_TOKEN,
        "withOutput": True,
        "withStderr": True
    }
    response = requests.get(url, params=params)
    if response.status_code != 200:
        abort(502)
    data = response.json()
    if data["status"] < 0:
        return {
                   "id": id,
                   "status": "in queue",
               }, False
    elif data["status"] != 0:
        return {
                   "id": id,
                   "status": SPHERE_STATUS_MAPPING[data["status"]],
               }, False
    if data["result"] == 15:
        output = {
            "type": data["output_type"],
            "value": data["output"],
        }
    else:
        type = "generic error"
        if data["result"] in SPHERE_ERR_MAPPING:
            type = SPHERE_ERR_MAPPING[data["result"]]
        output = {
            "type": type,
            "value": data["stderr"]
        }
    result = {
        "id": id,
        "status": "finished",
        "time": data["time"],
        "success": data["result"] == 15,
        "memory": data["memory"],
        "output": output
    }
    return result, data["result"] == 15
