# twitter_bot

This is a twitter bot to reply to tweets in real time on mentioning the bot ( **@cbzbot** ).
This chatbot have been programmed to provide useful information using metadata tags used with the messages. 
There are several metadata defined to help chatbot find suitable reply in context with the users query like **"#info" "#goodmorning" "#goodnight" "#time" "#date"  "#calendar" "#website" etc.** 

### Following are the files included in the repository and their uses

**Pybot.py**

This Python file runs the main script and support chatbot's functionalities. User authentication, collecting data from Twitters API, replying to each tweet.

Following functions are used


| Function |parameter | return | Use |
| ------ | ------ |  ------ | ------ |
| updated_time() |-| current date and time | returns current IST date and time for log |
| read_last_seen_id() |-| ID of last replied tweet | return the status id of last replied tweet |
| update_last_seen_id(ID) |id of last replied tweet|-| store the tweet ID after each reply to tweet  |
| get_message(mention) |detail of tweet|text containg message| returns the message to be sent in reply |

**logs.py** 

This python module helps in logging and maintaining console.

It stores following functions

|function |parameter | return | Use |
| ------ | ------ |  ------ | ------ |
| log |string of text| | logs activities |
| clear |-|- | clear console content |

**log_seen_id.txt**

txt file to store the ID of tweet last replied.


log.txt

store the logs of activities performed by chatbot.
