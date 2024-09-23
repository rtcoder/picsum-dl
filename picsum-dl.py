import os
import requests
import argparse


def download_images(count, width, height=None):
    folder_name = 'picsum-dl'
    os.makedirs(folder_name, exist_ok=True)

    for i in range(1, count + 1):
        # Budowanie URL do pobierania obrazu
        if height:
            url = f"https://picsum.photos/{width}/{height}"
        else:
            url = f"https://picsum.photos/{width}"

        print(f"Downloading image {i} from {url}...")
        response = requests.get(url)

        if response.status_code == 200:
            # Zapisujemy obraz do pliku
            with open(os.path.join(folder_name, f'image_{i}.jpg'), 'wb') as f:
                f.write(response.content)
            print(f"Image {i} has been saved.")
        else:
            print(f"Cannot download image {i}. Status code: {response.status_code}")


if __name__ == "__main__":
    # Argumenty dla skryptu
    parser = argparse.ArgumentParser(description="Download images from Picsum.photos")
    parser.add_argument('-c', '--count', type=int, required=True, help='Images count to download')
    parser.add_argument('-w', '--width', type=int, required=True, help='Images width')
    parser.add_argument('-ht', '--height', type=int, help='Images height (optional)')

    args = parser.parse_args()

    download_images(args.count, args.width, args.height)
