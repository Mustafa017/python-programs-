# -*- coding: utf-8 -*-
"""
Created on Tue Feb  7 20:50:03 2017

@author: mustafa
"""
import requests

r = requests.get("http://google.com")
print(r)
print (r.status_code)
print(r.encoding)
print(r.text)

contact_info = {
    "email": "mustafangure@gmail.com",
    "lastname": "khamisi",
    "message": "I am really excited to be in this bootcamp. I have learned something new",
    "name": "mustafa"
}

r = requests.post("https://lambdaschool.com/contact-form", json = contact_info)

print("response: %s status code: %s" % (r.text, r.status_code))