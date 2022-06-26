import requests


def payloads_requests():
    url = "https://api.spacexdata.com/v3/payloads"
    request = requests.get(url)
    data = request.json()

    for payloads in range(len(data)):
        print(
            f"• ID : {data[payloads]['payload_id']}\n",
            f"• Reused : {data[payloads]['reused']}\n",
            f"• Payload Type : {data[payloads]['payload_type']}\n",
            f"• orbit : {data[payloads]['orbit']}\n"
        )
