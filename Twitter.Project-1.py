
# coding: utf-8

# In[85]:

import pickle
import os
import pandas as pd 
import matplotlib.pyplot as plt



# In[74]:

if not os.path.exists('secret_twitter_credentials.pkl'):
    Twitter={}
    Twitter['Consumer Key'] = ''
    Twitter['Consumer Secret'] = ''
    Twitter['Access Token'] = ''
    Twitter['Access Token Secret'] = ''
    with open('secret_twitter_credentials.pkl','wb') as f:
        pickle.dump(Twitter, f)
else:
    Twitter=pickle.load(open('secret_twitter_credentials.pkl','rb'))


# In[75]:

get_ipython().system('pip install twitter')


# In[76]:

import twitter

auth = twitter.oauth.OAuth(Twitter['Access Token'],
                           Twitter['Access Token Secret'],
                           Twitter['Consumer Key'],
                           Twitter['Consumer Secret'])

twitter_api = twitter.Twitter(auth=auth)

print(twitter_api)


# In[77]:

WORLD_WOE_ID = 1
US_WOE_ID = 23424977


# In[78]:

LOCAL_WOE_ID = 	2514815

world_trends = twitter_api.trends.place(_id=WORLD_WOE_ID)
us_trends = twitter_api.trends.place(_id=US_WOE_ID)
local_trends = twitter_api.trends.place(_id=LOCAL_WOE_ID)


# In[79]:

world_trends[:2]


# In[80]:

trends = local_trends
print(type(trends))
print(list(trends[0].keys()))
print(trends[0]['trends'])


# In[81]:

import json

print((json.dumps(us_trends[:2], indent=1)))


# In[82]:

trends_set = {}
trends_set['world'] = set([trend['name']
                          for trend in world_trends[0]['trends']])

trends_set['us'] = set([trend['name']
                       for trend in us_trends[0]['trends']])

trends_set['DC'] = set([trend['name']
                             for trend in local_trends[0]['trends']])


# In[83]:

for loc in ['world','us', 'DC']:
    print(('-'*10, loc))
    print(('-'.join(trends_set[loc])))


# In[86]:

print(( '='*10, 'intersection of the world and the US'))
print((trends_set['world'].intersection(trends_set['us'])))

print(('='*10,'intersection of us and DC'))
print((trends_set['DC'].intersection(trends_set['us'])))


# In[99]:

print(('='*10,'intersection of us and DC'))
print((trends_set['DC'].intersection(trends_set['us'])))


# In[102]:

topic = '#trump'

number = 50

search_results = twitter_api.search.tweets(q=topic, count=number)

statuses = search_results['statuses']


# In[103]:

len(statuses)
print(statuses)


# In[105]:

all_text = []
filtered_statuses = []
for s in statuses:
    if not s["text"] in all_text:
        filtered_statuses.append(s)
        all_text.append(s["text"])
statuses = filtered_statuses


# In[106]:

len(statuses)


# In[107]:

[s['text'] for s in search_results['statuses']]


# In[110]:

status_texts = [ status['text'] 
                 for status in statuses ]

screen_names = [ user_mention['screen_name'] 
                 for status in statuses
                     for user_mention in status['entities']['user_mentions'] ]

hashtags = [ hashtag['text'] 
             for status in statuses
                 for hashtag in status['entities']['hashtags'] ]

# Compute a collection of all words from all tweets
words = [ w 
          for t in status_texts 
              for w in t.split() ]


# In[112]:

from collections import Counter

for item in [words, hashtags]:
    c = Counter(item)
    print(c.most_common()[:10]) # top 10
    print()


# In[ ]:



