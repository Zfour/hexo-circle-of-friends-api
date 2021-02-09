# -*- codeing = utf-8 -*-
# @Time : 2021/02/08 9:05 上午
# @Author : Zfour
# @File : spyder1.py
# @Software : PyCharm

import leancloud
from http.server import BaseHTTPRequestHandler
import json
import datetime
import os

def getdata():
    list = ['title','time','link','author','headimg']
    list_user = ['frindname','friendlink','firendimg','error']
    # Verify key
    leancloud.init(os.environ["LEANCLOUD_ID"], os.environ["LEANCLOUD_KEY"])

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

    Friendlist = leancloud.Object.extend('friend_list')
    query_userinfo = Friendlist.query
    query_userinfo.limit(1000)
    query_userinfo.select('frindname','friendlink','firendimg','error')
    query_list_user = query_userinfo.find()


    # Result to arr
    datalist=[]
    for i in query_list:
        itemlist=[]
        for item in list:
            itemlist.append(i.get(item))
        update_time = i.get('createdAt')
        itemlist.append(update_time.strftime('%Y-%m-%d %H:%M:%S'))
        datalist.append(itemlist)


    datalist_user =[]
    for j in  query_list_user:
        itemlist_user=[]
        for item2 in list_user:

            itemlist_user.append(j.get(item2))
        datalist_user.append(itemlist_user)
    total_data = []
    total_data.append(datalist_user)
    total_data.append(datalist)
    return total_data
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
print(getdata())