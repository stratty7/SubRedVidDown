import praw
import subprocess
import os
import time

from datetime import datetime

reddit = praw.Reddit(client_id="",
                     client_secret="",
                     user_agent="RedditDATA")


videolist = []
titlelist = []
count = 0
sub = "nba"
today = datetime.now()
date_time = today.strftime("%d")
path = "C:/reddit/" + sub + date_time
count2 = 0

for filename in os.listdir(path):
    print(filename)

try:
    os.mkdir(path)
except OSError:
    print ("Creation of the directory %s failed" % path)
else:
    print ("Successfully created the directory %s " % path)


for submission in reddit.subreddit(sub).hot(limit=100):
    if ('gfycat' in submission.url):
        titlelist.append(submission.title)
        videolist.append(submission.url)
    elif('streamable' in submission.url):
        titlelist.append(submission.title)
        videolist.append(submission.url)
    elif ('youtube' in submission.url):
        titlelist.append(submission.title)
        videolist.append(submission.url)
for x in videolist:
  count += 1
  os.system('cd ' + path + ' & ' + 'youtube-dl ' + x)


for filename in os.listdir(path):
    name = filename.replace(".mp4", "")
    name1 = filename.replace(" ", "")
    name2 = name1.replace("_", "")
    name3 = name2.replace("-", "")
    name4 = name3.replace("'","")
    name5 = name4.replace(r'\.(?=.*?\.)', '')
    name6 = name5.replace("'","")
    
    print(name1)
    os.system('cd ' + path + ' & ' + 'ffmpeg -i ' + '"' + filename + '"' +'  -vf drawtext="fontfile=/path/to/font.ttf: text='+ name +': fontcolor=white: fontsize=24: box=1: boxcolor=black@0.5: boxborderw=5: x=10:y=10" -codec:a copy "'+ name6+'"')
    os.remove(path + '/' + filename)
    


print(videolist)
print(titlelist)
print(count)
        
