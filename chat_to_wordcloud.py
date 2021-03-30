# -*- coding: utf-8 -*-
"""
Created on Thu Feb 18 10:16:04 2021

Given a path to a .json exported whattsapp chat,
it reads all message words,creates a wordcloud with the most common ones
and saves it to a png file.

@author: Pablo R. Alves
"""

import json
from re import sub
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS


path = input('Whattsapp chat json file path:')
data = json.load(open(path, 'r',encoding = 'utf-8')) 

text = ''

for msg in data['messages']:
    if str(msg).__contains__("from") == False:
        pass
    elif str(msg).__contains__('[{') == True:
        pass
    else:
        text += str(msg['text'])+" "
    
file_content = text.split()



file_content = sub(r'\b\w{1,2}\b', '', str(file_content))

def random_color_func(word=None, font_size=None, position=None, orientation=None, font_path=None, random_state=None):
    h = int(360.0 * 230.0 / 255.0)
    s = int(100.0 * 255.0 / 255.0)
    l = int(100.0 * float(random_state.randint(60, 120)) / 255.0)
    return "hsl({}, {}%, {}%)".format(h, s, l)


wordcloud = WordCloud(font_path = r'C:\Windows\Fonts\Verdana.ttf',
                            stopwords = STOPWORDS,
                            background_color = 'orange',
                            width = 1920,
                            height = 1080,
                            color_func = random_color_func
                            ).generate(file_content)

plt.imshow(wordcloud)
plt.axis('off')
plt.show()

wordcloud.to_file(path+' (wordcloud).png') 