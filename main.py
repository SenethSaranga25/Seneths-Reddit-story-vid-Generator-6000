import Ai
import reddit_card
import edit
import time

d = {}
d['topic'] = input("[Topic for the video >>]\n")
d['profile'] = input("[Name of the Profile >>]")
while True:
    d['upvotes'] = input("[Number of upvotes] > ")
    d['comment'] = input("[Number of Comments] > ")
    if d["upvotes"].isnumeric() and d["comment"].isnumeric():
        break

for i in range(100):
    try:
        title = Ai.create_story(topic=str(d["topic"]))
        if title == 1:
            print("Api fault")
        else:
            reddit_card.create_card(title=title,profile="stuf\prof_pic\prof.png",upvotes=int(d["upvotes"]),Profile_name=str(d["profile"]),comments=int(d["comment"]))
            edit.edit()
            print("[Video Done!!!!]")
        print(f"\n[Video{i} Done!!!]\n")
    except:
        time.sleep(30*60)

