import requests
r1 = requests.get('https://gsom.spbu.ru/en/')
if 'text/html' in r1.headers.get('Content-Type', ''):
    string = r1.text
    png_index = string.find('.png')

    if png_index != -1:
        start_quote = string.rfind('"', 0, png_index)
        end_quote = string.find('"', png_index)
        relative_url = string[start_quote + 1:end_quote]
        full_url = 'https://gsom.spbu.ru' + relative_url
        print(f"First .png image URL: {full_url}")

        image_response = requests.get(full_url)

        image_filename = full_url.split('/')[-1]

with open('file.png', 'wb') as f:
    f.write(r1.content)
print(r1.content)
