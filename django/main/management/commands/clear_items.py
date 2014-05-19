import csv
from django.core.management.base import BaseCommand, CommandError
from main.models import BaseItem, ItemCategory, BaseItemAbility
import re

class Command(BaseCommand):
    args = ''
    help = 'Clears the items'

    def handle(self, *args, **options):

         global currentItem, abilities
         currentItem = None
         abilities = []
         BaseItem.objects.all().delete()
         BaseItemAbility.objects.all().delete()










