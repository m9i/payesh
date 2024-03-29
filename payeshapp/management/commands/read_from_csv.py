from django.core.management.base import BaseCommand
from payeshapp.models import SqlDataAuth
import pandas as pd


def read_from_csv():
    where_file()


def where_file():
    file = '/home/mahsa/PycharmProjects/payesh/payesh/sql_data.csv'
    xl = pd.read_csv(file)
    read_csv_action(file)


def read_csv_action(file):
    try :
        s = SqlDataAuth.objects.filter(id__isnull=False).all()
        s.delete()
        for i in range(0, list(pd.read_csv(file)._values).__len__()):
            #det = pd.read_csv(file)._values[i][0].split(';')
            det = pd.read_csv(file)._values[i]
            name = det[0]
            host = det[1]
            server = det[2]
            port = det[3]
            user = det[4]
            password = det[5]
            save_distinct(host, name, password, port, server, user)
    except IndexError:
        pass

def save_distinct(host, name, password, port, server, user):
    if not SqlDataAuth.objects.filter(host=host).exists():
        sql_data_auth = SqlDataAuth(name=name, host=host, server=server, port=port, user=user, password=password)
        sql_data_auth.save()

class Command(BaseCommand):
    def handle(self, **options):
        read_from_csv()

