import os

def clear():
    os.system('clear')
    os.system('CLS')

def log(text):
    text = str(text)
    log_file = open("log.txt","a")
    log_file.write(text)
    log_file.write("\n")
    log_file.close()
