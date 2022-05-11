import urllib.request

get_url= urllib.request.urlopen('http://siakad.umb.ac.id')

print("Response Status: "+ str(get_url.getcode()) )

import urllib.request

get_url= urllib.request.urlopen('https://www.youtube.com/')

print("Response Status: "+ str(get_url.getcode()))

print(get_url.read())