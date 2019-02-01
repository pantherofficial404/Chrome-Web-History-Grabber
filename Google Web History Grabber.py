import os
import sqlite3
# import pandas as pd
import time
username=os.getlogin()
# ubuntu = "%LocalAppData%\Google\Chrome\User Data\Default\Local Storage"
dir="C:\\Users\\{}\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\".format(username)
files = os.listdir(dir)
history_db = os.path.join(dir, 'history')
print(history_db)

c = sqlite3.connect(history_db)
cursor = c.cursor()
select_statement = "SELECT id,url,title,visit_count,last_visit_time FROM urls"
cursor.execute(select_statement)

results = cursor.fetchall()
ids = []
urls = []
titles = []
visit_counts = []
last_visit_times = []
import pyfiglet 
  
result = pyfiglet.figlet_format("L C O") 
print(result)
time.sleep(5) 
for res in results:
    id,url,title,visit_count,last_visit_time = res
    print(id,url,title,visit_count,last_visit_time)
    ids.append(id)
    urls.append(urls)
    titles.append(title)
    visit_counts.append(visit_count)
    last_visit_times.append(last_visit_time)


result = pyfiglet.figlet_format("Hacked By Saksham Chaudhary") 
print(result)