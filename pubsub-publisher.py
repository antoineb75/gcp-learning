import os
from google.cloud import pubsub_v1

credentials_path = 'tunes-admin.privateKey.json'
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credentials_path

publisher = pubsub_v1.PublisherClient()
topic_path = 'projects/prepa-certif-pca/topics/music-tunes'

data = 'A new tune is ready'
data = data.encode('utf-8')
attributes = {
    'artist': 'beatles',
    'album': 'white album',
    'title': 'blackbird6'
}

future = publisher.publish(topic_path, data, **attributes)

print(f'published message id {future.result()}')
