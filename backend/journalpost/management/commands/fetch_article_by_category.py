import requests
import time

from decouple import config
from django.core.management.base import BaseCommand, CommandError
from backend.models import Article


class Command(BaseCommand):
    help = "Adds articles to the database from mediastack API"


    def add_arguments(self, parser):
        parser.add_argument("category", nargs="1", type=str)
    
    def handle(self, *args, **options):
        API_KEY = config("API_KEY")

        request = requests.get(url="http://api.mediastack.com/v1/news?access_key=" + API_KEY + "&languages=en&limit=100&category=" + options['category'])

        data = request.json()
        count = 0
        for article in data['data']:
            if(article['image']):
                Article.objects.create(author=article['author'], title=article['title'], category=options['category'], image_url=article['image'], origin_url=article['url'], body=article['description'])
                count = count + 1
        print("Fetched and added " + str(count) + " articles...")
