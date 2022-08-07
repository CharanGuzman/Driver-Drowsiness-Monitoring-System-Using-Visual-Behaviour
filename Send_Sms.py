import requests
def sendSms():
    url = "https://www.fast2sms.com/dev/bulkV2"
    payload = "sender_id=FSTSMS&message=Driver is drowsy please alert!!!&language=english&route=p&numbers=6303493629"
    headers = {
    'authorization': "L3V98nqRvjweK74TbWdNotkc2uhCDHzSYFrXUlZM5iamAIyP0fV12z4MaHOAouDpg8xSLkPKBqcvZhiR",
    'Content-Type': "application/x-www-form-urlencoded",
    'Cache-Control': "no-cache",
    }
    response = requests.request("POST", url, data=payload, headers=headers)
    print(response.text)