import sys
import requests
from tqdm import tqdm
url=sys.argv[1]
type=sys.argv[2]
name=sys.argv[3]

def img_download(link):
    try:
        response=requests.get(url=link)
        with open(name,'wb') as file:
            file.write(response.content)
        return "ma bro your pic is pulled"
    except Exception as ex:
        raise Exception("ma bro shit hit the fan")
def download_video(link):
    try:
        print("wait")
        response=requests.get(url=link,stream=True)
        print(response.status_code)
        total_size_in_bytes= int(response.headers.get('content-length', 0))
        print("total size {}".format(total_size_in_bytes))
        progress_bar = tqdm(total=total_size_in_bytes, unit='iB', unit_scale=True)
        with open(name, 'wb') as file:
            for chunk in response.iter_content(chunk_size=1024 * 1024):
                if chunk:
                    progress_bar.update(len(data))
                    file.write(chunk)
        pogress_bar.close()
        return 'hommie your task is done'
    
    except Exception as _ex:
        return 'ooo hell noo!!! Check the URL please!, '
def main():
    if type=="mp4":
        print("ok lets begin")
        download_video(url)
    else:
        img_download(url)
    
    
if __name__ == '__main__':
    main()
    
