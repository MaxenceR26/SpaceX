import requests


def cores_requests():
    url = "https://api.spacexdata.com/v3/cores"
    request = requests.get(url)
    data = request.json()

    for cores in range(len(data)):
        for mission in range(len(data[cores]['missions'])):
            if not mission:
                print(
                    f"Cores : {data[cores]['core_serial']} -> \n",
                    f"• STATUS : {data[cores]['status']}\n",
                    f"• Original Launch : {data[cores]['original_launch']}\n",
                    f"• Original Launch Unix : {data[cores]['original_launch_unix']}\n",
                    f"• MISSIONS : {data[cores]['missions'][mission]['name']}\n",
                    f"• Details : {data[cores]['details']}\n",
                )
