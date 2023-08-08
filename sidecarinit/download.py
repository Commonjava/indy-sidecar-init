import urllib.request
import shutil
import os
from zipfile import ZipFile
from zipfile import BadZipFile

def download_archive(url, repository):
    build_id = os.environ.get('BUILD_CONFIG_ID')
    archive_path = f"/{build_id}.zip"

    try:
      print(f"Trying to download archive from url {url}\n")
      with urllib.request.urlopen(url) as response:
          with open(repository + archive_path, 'wb') as out_file:
              shutil.copyfileobj(response, out_file)
      downloaded = True
    except urllib.error.HTTPError as e:
      downloaded = False
      if e.code == 404:
        print("Archive is not found.\n")
      else:
        print(f"{e.code}: {e.reason}\n\n{e.headers}")

    if downloaded:
      print(f"Archive is downloaded successfully, unpacking it in {repository}\n")
      try:
          with ZipFile(repository + archive_path) as archive_zip:
              archive_zip.extractall(repository)
              print("Unpacked successfully.\n")
      except BadZipFile:
        print("Downloaded archive can not be extracted since it's a bad zip file.\n")
