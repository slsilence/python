import os
import requests as rq
from splinter import Browser
BASE_URL = 'https://mp.weixin.qq.com/s/eg5kO7Ee3AG6VgsMzKS4ow'
bro = Browser('chrome')
bro.visit(BASE_URL)
links = bro.find_by_css('a[data-linktype="2"]')
print(links)


