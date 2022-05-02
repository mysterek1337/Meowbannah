import requests
from requests.sessions import session
import json
import time

print("Meowbannah")
print("Simple tool for reporting Meowbahh!")
print("Made by Mysterek!")

session = requests.session()

x = "https://www.tiktok.com/aweme/v1/aweme/feedback/?aid=1988&app_language=en-US&app_name=tiktok_web&browser_language=en-US&browser_name=Mozilla&browser_online=true&browser_platform=Win32&browser_version=5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F100.0.4896.127%20Safari%2F537.36&channel=tiktok_web&cookie_enabled=true&current_region=US&device_platform=web_pc&focus_state=true&from_page=user&history_len=7&is_fullscreen=false&is_page_visible=true&lang=en-EN&nickname=Meowbah%21&object_id=7071600069443109889&os=windows&owner_id=7071600069443109889&priority_region=&reason=306&referer=https%3A%2F%2Fwww.tiktok.com%2F404%3FfromUrl%3D%2Fmeowbah_&region=US&report_type=user&root_referer=https%3A%2F%2Fwww.tiktok.com%2F404%3FfromUrl%3D%2Fmeowbah_&secUid=MS4wLjABAAAAcJKM8e6yLnNpKOQSG1FGlMqDRqrgVwqttfoIjYTeP1tVyZlJsr5CY8VbSyDcZqMU&target=7071600069443109889"
print("")

print('Reporting...')
print('')

while True:
    req = session.post(x)
    
    print(req.text)
    print('reported + L Ratio + EZ WIN + GG')

    time.sleep(5)


input()



