

import json
import webbrowser
import urllib.request



getdata = urllib.request.urlopen("https://api.nasa.gov/planetary/apod?api_key=FIeAe9CzB2EdLQqMX9UiB1LeKtLw97tr8kCol0Jk&date=2017-07-12").read()

data = str(getdata, 'utf-8')
data2 = json.loads(data)

print(data2['url'])
webbrowser.open(data2['url'])
