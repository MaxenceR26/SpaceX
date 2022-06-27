import requests


def capsules_requests():
    url = "https://api.spacexdata.com/v3/capsules"
    request = requests.get(url)
    data = request.json()

    counter = 0
    for capsule in range(len(data)):
        for mission in range(len(data[capsule]['missions'])):
            if not mission:
                counter += 1
                if counter > 2:
                    input("Continue...")
                    counter = 0
                print(
                    f"Capsule : {data[capsule]['capsule_serial']} -> \n",
                    f"• ID : {data[capsule]['capsule_id']}\n",
                    f"• Status : {data[capsule]['status']}\n",
                    f"• Missions : {data[capsule]['missions'][mission]['name']}\n",
                )
