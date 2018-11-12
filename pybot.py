# pybot.py
# Ayush Kumar 11/11/2018
# chatbot to reply with coustomized text whem mentioned (@cbzbot)

# start->authenticate-> recieve mentions-> iterate through each mention -> get_message -> send message -> sleep-> recieve mentions

# importing modules
import tweepy
from datetime import datetime
from pytz import timezone
from tzlocal import get_localzone
from logs import log, clear
import calendar, time


print("This is chatbot")
log("pybot restarted !")

# initializing credentials
CONSUMER_KEY = 's9Oickg7v50mBGePI6FFd07es'
CONSUMER_SECRET = 'ad6ijS9p0MgcPUGncbVmJyeirW5A9g5sIplBcmC1mfg6ce3a29'
ACCESS_KEY = '1061286379458621441-0pk8k0iuSlY6SKdjS2YSfsE4T1I34I'
ACCESS_SECRET = 'QclCsy5RtGxtuqo108DbBkUoJ5HpEdLh3EGgdZcOO8lYV'

# authenticating user
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)

api = tweepy.API(auth)

# some variables
DATETIME_FORMAT = "%Y-%m-%d %H:%M:%S %Z"


# update time
def updated_time():
    UTC = datetime.now(timezone('UTC'))
    IST = UTC.astimezone(get_localzone())
    DATETIME_IST = IST.strftime(DATETIME_FORMAT)
    return DATETIME_IST

# To get data of last replied mention from file "last_seen_id.txt"
def read_last_seen_id():
    file = open('last_seen_id.txt','r')
    text = int(file.readline())
    file.close()
    return text

# To store data of last replied mention in file "last_seen_id.txt" after every reply
def update_last_seen_id(ID):
    file = open('last_seen_id.txt','w')
    file.write(str(ID))
    file.close()

# to get coustomized reply for every mentions according to content of tweet
def get_message(mention):
    sender_user_name = mention.user.screen_name
    hashtags = mention.entities['hashtags']

    str_tags = ''
    list_tags = []
    for tags in hashtags:
        str_tags += ' #'
        list_tags.append(tags['text'].lower())
        str_tags += tags['text']

    message = "@" + sender_user_name + " "

    # selecting which message to send

    if "info" in list_tags:
        text = "type website, support, date, time, calendar to use :)"
    # GOOD MORNING
    elif "goodmorning" in list_tags:
        text = "good morning"
    # GOOD NIGHT
    elif "goodnight" in list_tags:
        text = "good night"

    #WEBSITE
    elif "website" in list_tags:
        text = "https://www.github.com/gr8ayu"

    #SUPPORT
    elif "support" in list_tags:
        text = "We will soon be in contact with you, Sorry for any inconvenience "

    #DATE
    elif "date" in list_tags:
        now_utc = datetime.now(timezone('UTC'))
        now_local = now_utc.astimezone(get_localzone())
        date = now_local.strftime(DATETIME_FORMAT)
        text = "DATE :" + str(date)

    #TIME
    elif "time" in list_tags:
        now_utc = datetime.now(timezone('UTC'))
        now_local = now_utc.astimezone(get_localzone())
        date = now_local.strftime(DATETIME_FORMAT)
        text =  "Time :" + str(date)

    #CALENDER
    elif "calendar" in list_tags or "cal" in list_tags:
        now_utc = datetime.now(timezone('UTC'))
        now_local = now_utc.astimezone(get_localzone())
        cal = calendar.month(now_local.year,now_local.month)
        text = 'CALENDAR :\n' + str(cal)

    else:
        text = "Thanks for mentioning me :) "


    message += text
    message += str_tags
    return message

since_id = '1061381025165533184'
since_id = read_last_seen_id()



# infinite loop to keep looking for new mentions every 30 seconds
while(True):
    since_id = read_last_seen_id()
    mentions = api.mentions_timeline(since_id)
    print(str(updated_time()) + ' retrieved' ,len(mentions), 'new mentions')
    log(str(updated_time()) + ' retrieved ' +str(len(mentions))+ ' new mentions')

    # iterating through every unread mentions and replying to them
    for mention in reversed(mentions):
        sender_user_name = mention.user.screen_name
        hashtags = mention.entities['hashtags']

        str_tags = ''
        list_tags = []
        for tags in hashtags:
            str_tags += ' #'
            list_tags.append(tags['text'].lower())
            str_tags += tags['text']

        # getting appropriate messages for mentions using function get_message()
        message =  get_message(mention)

        try :
            api.update_status(message,mention.id)
        except tweepy.TweepError as e:
            print('============================')
            print("handled TweepError, " + e.reason + " for " + str(mention.id))
            print("============================")

            log("handled TweepError, " + e.reason + " for " + str(mention.id))

        else:
            print("message sent for ", mention.id)
            log("message sent for "+ str(mention.id))


        # storing new last seen user in file
        update_last_seen_id(mention.id)

    time.sleep(30) #sleep for 30 seconds after retrieving data
