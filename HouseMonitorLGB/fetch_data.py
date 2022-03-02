"""
    Called at regularly scheduled intervals to fetch environmental data by:
        1.  Gathering list of devices in-use (as defined in the database)
        2.  For each device, attempt to scrape data from each page of the
            device's web pages (as defined in the database)
        3.  Write the collected data to the central database        
"""

import requests
from bs4 import BeautifulSoup


class device:
    def __init__(self, hostname, room, room_id, pages):
        self.hostname = hostname
        self.room = room
        self.room_id = room_id
        self.pages = pages
    
    def getpagecontents_HTML(self, addr):
        #attempt to gather contents from a specified address
        try:
            print("Attempting to gather contents from page %s", addr)
            page = requests.get(addr)
            if page.status_code == 200:
                print("successfully retrieved page contents")
            else:
                print("unable to retrieve page contents")
            
            return page.content
        except:
            print("unable to retrieve page contents")
    
    def getpagecontents_text(self, addr):
        #take webpage raw contents and attempt to strip any HTML, leaving only page text
        contents_raw = self.getpagecontents_HTML(addr)
        soup = BeautifulSoup(contents_raw, 'html.parser')
        return(soup.prettify())
        
    def getpagecontents_midstring (self, addr, start_pos=0, length=-1):
        #from the webpage text returned, return contents using start/end characters
        contents = self.getpagecontents_text(addr)
        
        if length == -1:
            target_contents = contents[start_pos:]
        else:
            target_contents = contents[start_pos:start_pos+length]
            
        return target_contents

if __name__ == "__main__":
    dev = device(hostname = "ESP-2FC394", room = 'Living Room', room_id = '2', pages = ['/temp'])
    addr = "http://" + dev.hostname + "/lighting"
    contents = dev.getpagecontents_midstring(addr, start_pos = 21, length = 5)
    print(contents)
    
    
