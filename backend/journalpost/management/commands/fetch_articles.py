import requests
import time

from decouple import config
from django.core.management.base import BaseCommand, CommandError
from journalpost.models import Article


class Command(BaseCommand):
    help = "Adds articles to the database from mediastack API"
    
    def handle(self, *args, **options):
        categories = ["business", "entertainment", "health", "science", "sports", "tech"]
        API_KEY = config("API_KEY")
        for category in categories:
            request = requests.get(url="http://api.mediastack.com/v1/news?access_key=" + API_KEY + "&keywords=" + category)

            data = request.json()
            count = 0
            for article in data['data']:
                if(article['image']):
                    Article.objects.create(author=article['author'], title=article['title'], category=category, image_url=article['image'], origin_url=article['url'], body=article['description'])
                    count = count + 1
            print("Fetched and added " + str(count) + " " + category + " articles...")
