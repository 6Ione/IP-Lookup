import requests

def main():
    print("#" * 20)
    print("#   IP Lookup")
    print("#" * 20)

    ip = input("# IP: ")
    print("#" * 20)
    response = requests.get(f'https://api.techniknews.net/ipgeo/{ip}')

    if response.status_code == 200:
        data = response.json()

        if data.get('status') == 'success':
            print(f"\n'{ip}' returned {data.get('status')}")
            print(f"Proxy: {data.get('proxy')}")
            print("-" * 20)

            print(f"IP: {data.get('ip')}")
            print(f"Country: {data.get('country')}")
            print(f"State: {data.get('regionName')}")
            print(f"City: {data.get('city')}")
            print(f"Zip: {data.get('zip')}")
            print(f"ISP: {data.get('isp')}")
            print(f"Lat: {data.get('lat')}")
            print(f"Lon: {data.get('lon')}\n")
        else:
            print(f"Request failes with status code: {response.status_code}")
    else:
        print(f"Request failes with status code: {response.status_code}")


if __name__ == "__main__":
    main()