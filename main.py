import requests
import random

def get_rand_comic():
    url_for_rand = "https://xkcd.com/info.0.json"

    response = requests.get(url_for_rand)
    response.raise_for_status()

    num = response.json()['num']
    fin_num = random.randint(1, num)

    return fin_num

def save_comics(filename, image_url):
    image_response = requests.get(image_url)
    image_response.raise_for_status()

    with open (filename, 'wb') as f:
        f.write(image_response.content)

def get_urls(data):
    image_url = data['img']
    comm = data['alt']
    title = data['title']
    return image_url, comm, title

def main():
    url = f"https://xkcd.com/{get_rand_comic()}/info.0.json"
    
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()

    image_url, comm, title = get_urls(data)
    filename = f"{title}.png"
    save_comics(filename, image_url)

    return comm, filename

if __name__ == '__main__':
    main()