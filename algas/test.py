import requests

counter = 0
target ="moodle.sptech.school "

while True:
    try:
        r = requests.get(target)
        print(f"request {counter}")
    except e as Exception:
        print(e)
    counter += 1
        
