import json
from flask import Response

def FailInsertResponse():
    dict = {
        "Status" : 400,
        "Massage" : "Failed insert data"
    }
    temp = json.dumps(dict)
    return Response(temp, status=400, content_type="application/json")

def SuccessInsertResponse():
    dict = {
        "Status" : 200,
        "Massage" : "Success insert data"
    }
    temp = json.dumps(dict)
    return Response(temp, status=200, content_type="application/json")