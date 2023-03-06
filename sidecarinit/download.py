import urllib.request
import shutil
import os
from zipfile import ZipFile

def download_archive(url, repository):
    build_id = os.environ.get('build.config.id')
    archive_path = f"/{build_id}.zip"

    with urllib.request.urlopen(url) as response:
        with open(repository + archive_path, 'wb') as out_file:
            out_file.write(response.read())

    with ZipFile(repository + archive_path) as archive_zip:
        archive_zip.extractall(repository)
