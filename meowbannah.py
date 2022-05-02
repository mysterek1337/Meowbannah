import requests
from requests.sessions import session
import json
import time

print("Meowbannah")
print("Simple tool for reporting Meowbahh!")
print("Made by Mysterek!")

session = requests.session()

x = "https://www.tiktok.com/aweme/v1/aweme/feedback/?aid=1988&app_language=pl-PL&app_name=tiktok_web&battery_info=1&browser_language=pl-PL&browser_name=Mozilla&browser_online=true&browser_platform=Win32&browser_version=5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F100.0.4896.127%20Safari%2F537.36&channel=tiktok_web&cookie_enabled=true&current_region=PL&device_id=7046068764631631365&device_platform=web_pc&focus_state=true&from_page=user&history_len=2&is_fullscreen=false&is_page_visible=true&lang=pl-PL&nickname=Meowbah%21&object_id=7071600069443109889&os=windows&owner_id=7071600069443109889&priority_region=&reason=3012&referer=&region=PL&report_type=user&screen_height=768&screen_width=1366&secUid=MS4wLjABAAAAcJKM8e6yLnNpKOQSG1FGlMqDRqrgVwqttfoIjYTeP1tVyZlJsr5CY8VbSyDcZqMU&target=7071600069443109889&tz_name=Europe%2FWarsaw&webcast_language=pl-PL&msToken=i6BcyDXw7poqM-cvgNQCsYvaZLnNQu8XgNSCgdk6whL4DW6Tq3FKrSf8FkCr60F6tUkfSlGXabR1KKHMTF9lf0js8mdXI7SyfynmQwm5yK84wlEv7mvYCz0P8s3fWTpP42ww&X-Bogus=DFSzswV7102ANykcSUzmHOYklTXF&_signature=_02B4Z6wo0000134R0NgAAIDCoGeIfU5UEXN-EdRAAL335c"
print("")

print('Reporting...')
print('')

while True:
    req = session.post(x)
    
    print(req.text)
    print('reported + L Ratio + EZ WIN + GG')

    time.sleep(5)


input()



