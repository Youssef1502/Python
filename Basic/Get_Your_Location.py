#!/usr/bin/python3
'''================================================================================
--    Author    :   			YOUSSEF ADEL YOUSSEF

-- Description  :   Write application to get information about you location.
================================================================================'''

import requests

def get_public_ip():
    response = requests.get("https://api.ipify.org?format=json")
    if response.status_code == 200:
        return response.json()["ip"]
    else:
        return None

def get_location(ip, token):
    url = f"https://ipinfo.io/{ip}?token={token}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

if __name__ == "__main__":
    token = "21d40bf8637f86"
    public_ip = get_public_ip()

    if public_ip:
        print(f"Public IP: {public_ip}")
        location_info = get_location(public_ip, token)

        if location_info:
            print("Location Information:")
            print(f"IP: {location_info.get('ip')}")
            print(f"Hostname: {location_info.get('hostname')}")
            print(f"City: {location_info.get('city')}")
            print(f"Region: {location_info.get('region')}")
            print(f"Country: {location_info.get('country')}")
            print(f"Location: {location_info.get('loc')}")
            print(f"Organization: {location_info.get('org')}")
            print(f"Postal: {location_info.get('postal')}")
            print(f"Timezone: {location_info.get('timezone')}")
        else:
            print("Failed to retrieve location information.")
    else:
        print("Failed to retrieve public IP address.")
