import os
import time
from google.cloud import pubsub_v1

credentials_path = 'tunes-admin.privateKey.json'
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credentials_path

publisher = pubsub_v1.PublisherClient()
topic_path = 'projects/prepa-certif-pca/topics/beatles'

timestamp = str(time.time())
data = 'A new tune is ready'
data = data.encode('utf-8')
print(data)
attributes = {
    'artist': 'beatles',
    'album': 'white album',
    'title': 'song '+timestamp
}

future = publisher.publish(topic_path, data, **attributes)

print(f'for timestamp {timestamp} published message id {future.result()}')
