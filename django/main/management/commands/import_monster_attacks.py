import csv
from decimal import Decimal
from django.core.management.base import BaseCommand
from main.models import  MonsterAttackModifier, BaseMonsterAttackModifier


class Command(BaseCommand):
    args = '<csv_file>'
    help = 'Imports the specified csv'

    def handle(self, *args, **options):
        MonsterAttackModifier.objects.all().delete()
        BaseMonsterAttackModifier.objects.all().delete()
        for csv_file in args:
            with open(csv_file) as f:
                reader = csv.reader(f)
                count = 1
                for row in reader:
                    print(count)
                    modifier = {
                        'name': row[0],
                        'description': row[4],
                    }
                    if row[5]:
                        modifier['attackType'] = row[5]
                    if row[6]:
                        modifier['attackSubType'] = row[6]
                    if row[3]:
                        modifier['cos'] = row[3]
                    if "x" in row[1]:
                        modifier['isMultiplier'] = True
                        modifier['xpModifier'] = Decimal(row[1].replace("x", ""))
                        modifier['gilModifier'] = Decimal(row[2].replace("x", ""))
                    else:
                        modifier['xpModifier'] = Decimal(row[1])
                        modifier['gilModifier'] = Decimal(row[2])
                        modifier['isMultiplier'] = False
                    baseMonsterAttackModifier = BaseMonsterAttackModifier.objects.get_or_create(**modifier)[0]
                    baseMonsterAttackModifier.save()
                    count += 1









