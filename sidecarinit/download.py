import urllib.request
import shutil
import hashlib
import os
import zlib
from zipfile import ZipFile, BadZipFile

def download_archive(url, repository):
    build_id = os.environ.get('BUILD_CONFIG_ID')
    archive_path = f"{build_id}.zip"
    zip_path = os.path.join(repository, archive_path)

    try:
      url = f"{url}/{build_id}"
      print(f"Trying to download archive from url {url}\n")
      with urllib.request.urlopen(url) as response:
          with open(zip_path, 'wb') as out_file:
              shutil.copyfileobj(response, out_file)
      downloaded = True
    except urllib.error.HTTPError as e:
      downloaded = False
      if e.code == 404:
        print("Archive is not found.\n")
      else:
        print(f"{e.code}: {e.reason}\n\n{e.headers}")

    if downloaded:
      checksum = get_file_sha256(zip_path)
      if checksum:
          print(f"ZIP file SHA-256: {checksum}")

      print(f"Archive is downloaded successfully, unpacking it in {repository}\n")
      try:
          with ZipFile(zip_path) as archive_zip:
              archive_zip.extractall(repository)
              print("Unpacked successfully.\n")
      except (BadZipFile, zlib.error) as e:
        print(f"Error extracting zip file: {str(e)}\n")

        print("Start cleaning up extracted files from local FS...")
        try:
            shutil.rmtree(repository)
            print(f"Cleanup completed: {repository}\n")
        except Exception as cleanup_e:
            print(f"Error during cleanup: {str(cleanup_e)}\n")

        print("Start cleaning up zip file from Archive FS...")
        clean_archive_url = f"{url}/{checksum}"
        print(f"URL request: {clean_archive_url}")
        req = urllib.request.Request(clean_archive_url, method='DELETE')
        try:
            urllib.request.urlopen(req)
        except Exception as e:
            print(f"DELETE Archive Error: {str(e)}")

def get_file_sha256(file_path):
    sha256_hash = hashlib.sha256()
    try:
        with open(file_path, "rb") as f:
            for byte_block in iter(lambda: f.read(100 * 1024 * 1024), b""):
                sha256_hash.update(byte_block)
        return sha256_hash.hexdigest()
    except Exception as e:
        print(f"Error calculating SHA-256: {str(e)}")
        return None