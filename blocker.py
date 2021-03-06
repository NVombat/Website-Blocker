from datetime import datetime as dt
import time


#TEMP HOST FILE COPIED INTO FOLDER
temp_hosts_path = "/home/nvombat/Desktop/Website-Blocker/hosts"
#ORIGINAL HOST FILE -> /etc/hosts
original_hosts_path = "/etc/hosts"
#When visiting the webistes that have been blocked redirect to localhost
redirect_ip = "127.0.0.1"
#Lists of domain names of websites to block 
website_block_list = ["www.facebook.com", "facebook.com", "www.hotstar.com", "hotstar.com", "www.instagram.com", 
"instagram.com", "www.youtube.com", "youtube.com", "www.web.whatsapp.com", "web.whatsapp.com"]


while True:
    #Set a time period to block the websites -> Current set to block from 8:00 am to 4:00 pm
    if dt(dt.now().year, dt.now().month, dt.now().day,15) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day,16):
        print("Working Hours")
        with open(original_hosts_path, "r+") as f:
            cont = f.read()
            #print(cont)
            #Check if each website is in the hosts file
            for ws in website_block_list:
                #If website is in file during block time
                if ws in cont:
                    pass
                #If website is not in file during block time
                else:
                    #Write to file in a formatted manner the redirect ip and name of the website to be blocked
                    f.write(redirect_ip+" "+ws+"\n")
    #If the time is outside that of the websites being blocked
    else:
        print("Free Hours")
        with open(original_hosts_path, "r+") as f:
            cont = f.readlines()
            #Place the file pointer at the start of the file
            f.seek(0)
            for line in cont:
                #If the website to be blocked is not in the current line
                if not any(ws in line for ws in website_block_list):
                    #Write line to file from the start
                    f.write(line)
            #Remove all lines below it thus resulting in the original hosts file with no websites to be blocked
            f.truncate()
    #Keep checking conditions every n seconds
    time.sleep(10)