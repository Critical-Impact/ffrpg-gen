import csv
from django.core.management.base import BaseCommand, CommandError
from main.models import BaseItem, ItemCategory, BaseItemAbility
import re

class Command(BaseCommand):
    args = '<csv_file>'
    help = 'Imports the specified csv'

    def handle(self, *args, **options):

         global currentItem, abilities
         currentItem = None
         abilities = []
         for csv_file in args:
            with open(csv_file) as f:
                    reader = csv.reader(f)
                    next(reader, None)  # skip the headers
                    count = 1
                    for row in reader:
                        print(count)
                        count += 1
                        lastline = row
                        if row[0] == "" and row[4] != "--":
                            #ability line
                            abilities.append(row[4])
                        else:
                            if currentItem is not None:
                                self.createItem(currentItem,abilities)
                            abilities = []
                            currentItem = {
                                'name': row[0],
                                'tier': row[1],
                                'cost': self.getCost(row[2]),
                                'availability': self.getAvailability(row[3]),
                                'itemSlot': row[6],
                                'itemType': ItemCategory.objects.get(name=row[5])
                            }
                            if row[4] != "--":
                                abilities.append(row[4])

    def createItem(self,item,abilities):
        item = BaseItem.objects.get_or_create(**item)[0]
        for ability in abilities:
            print(ability)
            if ability != "--":
                baseItem = BaseItemAbility.objects.get_or_create(name=ability)[0]
                item.abilities.add(baseItem)
        item.save()

    def getAvailability(self,amount):
        amount = amount.replace('%','')
        amount = amount.replace('Artifact','0')
        amount = amount.replace('Legendary','1')
        return amount
    def getCost(self, cost):
        if cost == "--":
            return -1
        return cost









