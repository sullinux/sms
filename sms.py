import requests as r
import json

service_plan_id = " "
access_token = " "
from_ = "447520651996"
to_ = "+ phone numer"

headers = {
    "Authorization":f"Bearer {access_token}",
    "Content-Type":"application/json"
}

payload = {
    "from":from_,
    "to":[to_],
    "body":"Hello sweetie sasa , when we married"
}

response = r.post(
    f'https://sms.api.sinch.com/xms/v1/{service_plan_id}/batches',


    headers=headers,
    data=json.dumps(payload)
).json()

print(response)
