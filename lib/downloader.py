import requests
import tarfile
import os

class Downloader(object):

    def __init__(self, url, filename=None):
        self.url = url
        self.filename = filename if filename else os.path.basename(url)

    def download(self):
        r = requests.get(self.url, stream=True)
        f = open(self.filename, 'wb')
        for chunk in r.iter_content(chunk_size=1024):
            f.write(chunk)
            f.flush() 
        f.close()

    def extract(self):
        tar = tarfile.open(self.filename, "r:*")
        tar.extractall()
        tar.close()
