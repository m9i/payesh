from django.core.management.base import BaseCommand
from payeshapp.models import WindowsServer, LastCpu, LastMemory
#
# class Command(BaseCommand):
#     def handle(self, **options):
#         clean()
#
# def clean():
LastCpu.objects.filter(server=WindowsServer.objects.get(name='splc')).all().delete()
LastMemory.objects.filter(server=WindowsServer.objects.get(name='splc')).all().delete()
WindowsServer.objects.get(name='splc').delete()


