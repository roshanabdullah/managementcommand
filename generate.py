from django.core.management.base import BaseCommand
from articles.models import DocumentModel
from articles.management.factory.DocumentFactory import DocumentFactory
from faker import Faker
from django.db import transaction


fake = Faker()



class Command(BaseCommand):

    help = "Document Model Generator Command"
    
    @transaction.atomic
    def handle(self, *args, **kwargs):
        self.stdout.write("Deleting old data...")
        model = [DocumentModel]
        for m in model:
            m.objects.all().delete()

        
        
        self.stdout.write("Creating new data...")

        documents = []
        for _ in range(100):
            document = DocumentFactory()
            documents.append(document)
