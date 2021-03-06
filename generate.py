# The goal is to make an inbetween for telegram-history-dump and word_cloud

import json
import re # regex
import numpy as np # for fast math
from PIL import Image
from os import path
import sys # for argv

import matplotlib.pyplot as plt
import random
from wordcloud import WordCloud
# regex to remove non alphanumeric values
def main():
    if len (sys.argv) == 2:
        gen_wordcloud_from_jsonl_file(sys.argv[1])


def gen_wordcloud_from_jsonl_file(filename):
    """Open system program to view a wordcloud for all the text from jsonl file generated by telegram-history-backup  """        
    regex = re.compile('[^a-zA-Z]')
    count = 0
    word_cloud_list = []
    with open(filename) as jsonl_lines:
        for line in jsonl_lines:
            json_line_obj = json.loads(line)
            text = json_line_obj.get('text')
            if(text != None):#this was a message
                count = count + 1
                words = text.split()
                for word in words:
                    filtered_word = regex.sub('',word)
                    word_cloud_list.append(filtered_word)

    combined_text = ' '.join(word_cloud_list)



    wordcloud = WordCloud().generate(combined_text)
    #Display the generated image:
    #the matplotlib way:
    import matplotlib.pyplot as plt
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    plt.show()

main()
