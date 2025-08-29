import requests
import random
from pathlib import Path

BASE_URL = "https://xkcd.com"
SUFFIX = "info.0.json"


def get_rand_comic_num():
    response = requests.get(f"{BASE_URL}/{SUFFIX}")
    response.raise_for_status()
    return random.randint(1, response.json()['num'])


def fetch_comic(num):
    response = requests.get(f"{BASE_URL}/{num}/{SUFFIX}")
    response.raise_for_status()
    return response.json()


def download_image(url, filename):
    response = requests.get(url)
    response.raise_for_status()
    filename.write_bytes(response.content)


def save_rand_comic():
    num = get_rand_comic_num()
    info = fetch_comic(num)
    path = Path(f"{info['title']}.png")
    download_image(info['img'], path)
    return info['alt'], path


def main():
    caption, path = save_rand_comic()
    print(f'Скачан {path.name}. Комментарий: {caption}')


if __name__ == '__main__':
    main()
