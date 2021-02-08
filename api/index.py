# -*- codeing = utf-8 -*-
# @Time : 2021/02/08 9:05 上午
# @Author : Zfour
# @File : spyder1.py
# @Software : PyCharm

import leancloud
from http.server import BaseHTTPRequestHandler
import json
import datetime

def getdata():
    list = ['title','time','link','author','headimg']
    # Verify key
    leancloud.init("VXE6IygSoL7c2wUNmSRpOtcz-MdYXbMMI", "8nLVKfvoCtAEIKK8mD2J2ki7")

    # Declare class
    Friendspoor = leancloud.Object.extend('friend_poor')

    # Create an alias for the query
    query = Friendspoor.query

    # Select the sort methods
    query.descending('time')

    # Limit the number of queries
    query.limit(1000)

    # Choose class
    query.select('title','time','link','author','headimg','createdAt')

    # Execute the query, returning result
    query_list = query.find()

    # Result to arr
    datalist=[]
    for i in query_list:
        itemlist=[]
        for item in list:
            itemlist.append(i.get(item))
        datalist.append(itemlist)
        update_time = i.get('createdAt')
        datalist.append(update_time.strftime('%Y-%m-%d %H:%M:%S'))
    return datalist

    # Api handler
class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        data = getdata()
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(data).encode('utf-8'))
        return
