import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','first_project.settings')

import django
django.setup()

##FAKE POP SCRIPT
import random

from first_app.models import Accessrecord,Topic,Webpage
from faker import Faker

fakegen = Faker()

topics = ['social', 'search', 'marketplace', 'news', 'games']

def add_topic():
    t = Topic.objects.get_or_create(top_name = random.choice(topics))[0]
    t.save()
    return t

def populate(N=5):
    
    for entry in range(N):
        
        #get topic for the entry
        top = add_topic()
        
        #create fake data for that entry
        fake_url = fakegen.url()
        fake_date = fakegen.date()
        fake_name = fakegen.company()
        
        #Create the new web page entry
        webpg = Webpage.objects.get_or_create(topic = top, name = fake_name, url = fake_url)[0]
        
        #create fake access record for that webpage]
        acc_rec = Accessrecord.objects.get_or_create(name=webpg, date = fake_date)[0]
        
if __name__ == "__main__":
    print("Populating script!")
    populate(20)
    print("Population complete!")