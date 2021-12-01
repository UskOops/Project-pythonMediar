import os
import json

# Imports the Google Cloud client library
from google.cloud import storage

# Instantiates a client
storage_client = storage.Client()

# The name for the new bucket
bucket_name = "mediar-parameters"

bucket = storage.Bucket(storage_client, bucket_name)

blobs = list(storage_client.list_blobs(bucket, prefix="stura")) #list client and search for "stura" in gcp
for blob in blobs:
    if blob.name.endswith(".json"):
        print(blob.name)
        filename = os.path.join("/temp",blob.name.replace("/","%%")) 
        blob.download_to_filename(filename)
        with open(filename) as yuri: #yuri is a exemple name
            json_data = json.load(yuri)
            for roi in json_data['shapes']:
                if roi['attributes'][0]['value'] != 'crop':
                    roi_id = int(roi['attributes'][0]['value']) + 10**9
                    print(f'cam: {roi["frame"]} - roi: {roi_id}')

