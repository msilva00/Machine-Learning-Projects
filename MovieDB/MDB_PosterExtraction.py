#!/usr/bin/env python
# coding: utf-8

# In[1]:


import time


# In[2]:


import requests
import urllib.request as req
from PIL import Image
from IPython.display import clear_output
# from tqdm import tqdm


# In[3]:


CONFIG_PATTERN = 'http://api.themoviedb.org/3/discover/movie?api_key={key}&sort_by=popularity.desc&page={page}'


# In[4]:


KEY = '58f46cd179e3ec287410d723fafd6d76'
config = []


# In[ ]:





# In[ ]:





# In[5]:


base_url = 'http://image.tmdb.org/t/p/original'


# In[6]:


lst = range(1,501)
str_pages = ["{:1d}".format(x) for x in lst]


# In[7]:


for i in range(len(str_pages)):
    CONFIG_PATTERN = 'http://api.themoviedb.org/3/discover/movie?api_key={key}&sort_by=popularity.desc&page={page}'
    KEY = '58f46cd179e3ec287410d723fafd6d76'
    url = CONFIG_PATTERN.format(key=KEY, page = str_pages[i])
    r = requests.get(url)
    config.append(r.json())


# In[8]:


test = []
for page in range(500):
    testtt = []
    testtt = [config[page]['results'][i]['poster_path'] for i in range(len(config[page]['results']))]
# config[0]['results'][print(i) for i in testtt]['poster_path']
    test.append(testtt)
flattened_list = [y for x in test for y in x]


# In[ ]:


base_url + flattened_list[0]


# In[13]:


for i in range(len(flattened_list)):
#     if (i % 10) == 0:
#         print(i)
#     if (i % 100) == 0:
#         clear_output()
#         print(i/len(flattened_list)*100, "% COMPLETE")
    if flattened_list[i] is not None: 
        filename = 'poster_{}.jpg'.format(i)
        req.urlretrieve(base_url + flattened_list[i], filename)
#         basewidth = 75
        img = Image.open(filename)
#         wpercent = (basewidth/float(img.size[0]))
#         hsize = int((float(img.size[1])*float(wpercent)))
        img = img.resize((224,224), Image.ANTIALIAS)
        img.save(filename) 


# In[ ]:


# for page in (range(500)):
#     clear_output()
#     print("outer iter: ", page)
#     test = []
#     for i in range(len(config[page]['results'])):
#         test.append(config[page]['results'][i])
#     url2 = []
#     for i in range(len(config[page]['results'])):
#         # some movie titles have no poster path
#         if(test[i]['poster_path'] is not None):
#             url2.append(test[i]['poster_path'])
#     full_url = []
#     for i in range(len(url2)):
#         full_url.append(base_url + url2[i])
#
#
#     for i in range(len(full_url)):
#
#         print(i)
#         filename = 'poster_{0}_{1}.jpg'.format(page, i)
#         req.urlretrieve(full_url[i], filename)
#         basewidth = 75
#         img = Image.open(filename)
#         wpercent = (basewidth/float(img.size[0]))
#         hsize = int((float(img.size[1])*float(wpercent)))
#         img = img.resize((basewidth,hsize), Image.ANTIALIAS)
#         img.save(filename)
#
#
#
#
# # In[ ]:
#
#
# testtt = []
# for page in range(182,500):
#     clear_output()
#     print("outer iter: ", page)
#
#
# # In[ ]:
#
#
# page*len(url2)
#
#
# # In[ ]:
#
#
# test = []
# url2 = []
# full_url = []
# filename = []
# page = -1
# while page < 499:
#     page += 1
#     for i in range(len(config[page]['results'])):
#         test.append(config[page]['results'][i])
#
#     for i in range(len(config[page]['results'])):
#         url2.append(test[i]['poster_path'])
#
#     for i in range(len(config[page]['results'])):
#         full_url.append(base_url + url2[i])
#
#
#
#     for i in range(len(config[page]['results'])):
#         filename.append('poster_{0}_{1}.jpg'.format(page, i))
#
#
# #     for i in range(len(config[page]['results'])):
# #         print(page, i)
# #         filename.append('poster{0}_{1}.jpg'.format(page, i))
# #         print(filename[i])
#
# #     for i in range(len(config[page]['results'])):
# #         req.urlretrieve(full_url[i], filename[i])
#
#
# # In[ ]:
#
#
# config[1]['results'][0]['title']
#
#
# # In[ ]:
#
#
# full_url[0]
#
#
# # In[ ]:
#
#
# full_url[20]
#
#
# # In[ ]:
#
#
# # for i in range(len(full_url)):
#
# req.urlretrieve(full_url[0], filename[0])
#
#
# # In[ ]:
#
#
# full_url[0]
#
#
# # In[ ]:
#
#
#
#
#
# # In[ ]:
#
#
# f = urlopen(full_url[0])
#
#
# # In[ ]:
#
#
# filename = []
# for i in range(len(full_url)):
#     filename.append('poster_{0}.jpg'.format(i))
#
#
# # In[ ]:
#
#
# full_url
#
#
# # In[ ]:
#
#
#
#
#
# # In[ ]:
#
#
# for i in range(len(full_url)):
#     req.urlretrieve(full_url[i], filename[i])
#
#
# # In[ ]:
#
#
# filename = []
# filename.append('poster{0}_{1}.jpg'.format(2, 2))
# print(filename)
#
#
# # In[ ]:
#
#
#
#
#
# # In[ ]:
#
#
#
#
#
# # In[ ]:
#
#
#
#
#
# # In[ ]:
#
#
#
#
#
# # In[ ]:
#
#
# for i in range(len(config[pg1]['results'])):
#     test.append(config[pg1]['results'][i])
#
# for i in range(len(config[pg1]['results'])):
#     url2.append(test[i]['poster_path'])
#
# for i in range(len(config[pg1]['results'])):
#     full_url.append(base_url + url2[i])
#
#
# # In[ ]:
#
#
#
# for i in range(len(config[pg1]['results'])):
#     filename.append('poster{0}_{1}.jpg'.format(pg1, i))
#
# filename
#
#
# # In[ ]:
#
#
# full_url
#
#
# # In[ ]:
#
#
# import urllib.request as req
# for i in range(len(config[pg1]['results'])):
#     req.urlretrieve(full_url[i], filename[i])
#
#
# # imgurl ="https://i.ytimg.com/vi/Ks-_Mh1QhMc/hqdefault.jpg"
#
# # req.urlretrieve(imgurl, "image_name.jpg")
#
