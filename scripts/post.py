#!/usr/bin/env python
# coding: utf-8

# In[15]:


import tweepy
import datetime
import pandas as pd
import numpy as np
import pickle
import os


# ## Parameters and impo

# In[16]:


user_id_dog = 1483397937787023362
user_id_cat = 1514287408677806082


# In[17]:


with open('../../content/dogs/posts.pickle','rb') as f:
    dogs = pickle.load(f)
with open('../../content/cats/posts.pickle','rb') as f:
    cats = pickle.load(f)    


# In[18]:


dogs['text'] = dogs.apply(lambda row: str(row.text) + ' ' + str(row.hashtags), axis=1)
cats['text'] = cats.apply(lambda row: str(row.text) + ' ' + str(row.hashtags), axis=1)


# In[19]:


dogs['image'] = dogs.apply(lambda row: '../content/dogs/images/'+row.image, axis=1)
cats['image'] = cats.apply(lambda row: '../content/cats/images/'+row.image, axis=1)


# In[20]:


dogs['text'] = dogs.apply(lambda row: row.text.replace('nan ', ''), axis=1)
cats['text'] = cats.apply(lambda row: row.text.replace('nan ', ''), axis=1)


# ## Twitter Authentification

# In[21]:

api_key = os.environ['api_key']
api_key_secret = os.environ['api_key_secret']
bearer_token = os.environ['bearer_token']
client_id = os.environ['client_id']
client_secret = os.environ['client_secret']
access_token_dog = os.environ['access_token_dog']
access_token_cat = os.environ['access_token_cat']
access_token_secret_dog = os.environ['access_token_secret_dog']
access_token_secret_cat = os.environ['access_token_secret_cat']


client_dog = tweepy.Client(bearer_token, api_key, api_key_secret, access_token_dog, access_token_secret_dog)        


# In[22]:


client_cat = tweepy.Client(bearer_token, api_key, api_key_secret, access_token_cat, access_token_secret_cat)


# In[23]:


auth_dog = tweepy.OAuthHandler(api_key, api_key_secret)
auth_dog.set_access_token(access_token_dog, access_token_secret_dog)
api_dog = tweepy.API(auth_dog)


# In[24]:


auth_cat = tweepy.OAuthHandler(api_key, api_key_secret)
auth_cat.set_access_token(access_token_cat, access_token_secret_cat)
api_cat = tweepy.API(auth_cat)


# ## Check if this day has already been posted

# In[25]:


# use twitter api to return the last tweet from dog account
dog_check = api_dog.user_timeline(user_id=user_id_dog, count=1)
cat_check = api_cat.user_timeline(user_id=user_id_cat, count=1)


# In[26]:


# check if dog account has already tweeted today
if dog_check == []:
    dog_post_of_day = 1
elif dog_check[0].created_at.date() != datetime.date.today():
    dog_post_of_day = 1
else:
    dog_post_of_day = 2
    
# check if cat account has already tweeted today
if cat_check == []:
    cat_post_of_day = 1
elif cat_check[0].created_at.date() != datetime.date.today():
    cat_post_of_day = 1
else:
    cat_post_of_day = 2


# ## Post

# In[27]:


# retrieve text and picture of tweet from dataframe
dog_post = dogs.loc[(dogs.date == datetime.date.today()) & (dogs.post_of_day == dog_post_of_day)]
dog_text = dog_post.text.item()
dog_pic = dog_post.image.item
#----------------------------
cat_post = cats.loc[(cats.date == datetime.date.today()) & (cats.post_of_day == cat_post_of_day)]
cat_text = cat_post.text.item()
cat_pic = cat_post.image.item


# In[28]:


if dog_text == None:
    dog_pic = dogs.loc[(dogs.date == datetime.date.today()) & (dogs.post_of_day == dog_post_of_day)]['image'].item()
    media_dog = api_dog.media_upload(dog_pic)
    client_dog.create_tweet(media_ids=[media_dog.media_id])
else:
    dog_pic = dogs.loc[(dogs.date == datetime.date.today()) & (dogs.post_of_day == dog_post_of_day)]['image'].item()
    media_dog = api_dog.media_upload(dog_pic)
    client_dog.create_tweet(text=dog_text, media_ids=[media_dog.media_id])
#----------------------------
if cat_text == None:
    cat_pic = cats.loc[(cats.date == datetime.date.today()) & (cats.post_of_day == cat_post_of_day)]['image'].item()
    media_cat = api_cat.media_upload(cat_pic)
    client_cat.create_tweet(media_ids=[media_cat.media_id])
else:
    cat_pic = cats.loc[(cats.date == datetime.date.today()) & (cats.post_of_day == cat_post_of_day)]['image'].item()
    media_cat = api_cat.media_upload(cat_pic)
    client_cat.create_tweet(text=cat_text, media_ids=[media_cat.media_id])


# In[ ]:





# In[ ]:




