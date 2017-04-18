## Gather posts/comments from unnofficial Facebook pages of specified colleges

from facepy import GraphAPI
import requests

key = 'EAAEJsGZCZBLOABAJMekrvWXXzjbZAEAZCyEWsZAlrIiKNLXnqM3mTYYn6yEOZCsuEcqW0qJOKbkUmLzzGEgOwVw5VeN7s9yuxSZAAt9chyu2GZCI7ZATfiDtZB36BQYjWqualEHAFwyJ2HzRq0xBk1FknpUTDd2bi2nI5ZA0StZCRHvW88cjqz3ocjZCe'
graph = GraphAPI(key)

# Get my latest posts
posts = graph.get('1486880288288910/posts')
print posts
