import requests
r1 = requests.get('https://gsom.spbu.ru/en/')
if 'text/html' in r1.headers.get('Content-Type', ''):
    string = r1.text
    png_counter = string.count('.png')
    print("Number of .png images is", png_counter)
