import requests


def capsules_requests():
    url = "https://api.spacexdata.com/v3/capsules"
    request = requests.get(url)
    data = request.json()

    for capsule in range(len(data)):
        for mission in range(len(data[capsule]['missions'])):
            if not mission:
                print(
                    f"Capsule : {data[capsule]['capsule_serial']} -> \n",
                    f"• ID : {data[capsule]['capsule_id']}\n",
                    f"• STATUS : {data[capsule]['status']}\n",
                    f"• MISSIONS : {data[capsule]['missions'][mission]['name']}\n",
                )
