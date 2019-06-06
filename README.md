# Stackoverflow New Question Desktop Notifier
Automated Desktop notification about new questions being posted for a certain tag in stackoverflow for ubuntu system. Right now the tag name is hardcoded as `'python'`. You can change the tagname inside `scrape7.py` script. Also you may tinker with notification position, colors and widget height and width in the script.

## Run instructions
Run in terminal `python3 scrape7.py`

## Note
Web crawlers retrieve data uch faster than human and also more efficiently. 
Bad scraping practice may have some detrimental effect on the performance of the website being scraped.
That's why many websites check for autobots and restrict their actions.
Stackoverflow is also one of them who practices such behaviour. 
Check out their [`robots.txt`](https://stackoverflow.com/robots.txt).
It clearly states :
```
Disallow: /questions/*answertab=*
Disallow: /questions/tagged/*+*
Disallow: /questions/tagged/*%20*
Disallow: /questions/*/answer/submit
```
So, proceed with caution, 'cause your ip address may be blocked. 
Happened to me as I kept this running half an hour and my ip-address got temporarily banned.
I'll update with a proxy service and rotating alternative IP address and slowing down with `time.sleep()` later.

## Dependencies
* requests
* bs4
* dlib
* tkinter
* webbrowser

## Sample Notification :
Here is one sample notification :
![sample](notification.png)
