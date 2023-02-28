import urllib.request
import shutil
import os
from zipfile import ZipFile

def download_archive(url, repository):
    archive_name = os.environ.get('build.config.id')
    archive_path = "/" + archive_name + '.zip'

    with urllib.request.urlopen(url) as response, open(repository + archive_path, 'wb') as out_file:
        shutil.copyfileobj(response, out_file)

    archive_zip = ZipFile(repository + archive_path)
    archive_zip.extractall(repository)
    archive_zip.close()
