import csv

import psycopg2

from django.core.management.base import BaseCommand

from phones.models import Phone

from django.template.defaultfilters import slugify

class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('phones.csv', 'r') as file:
            phones = list(csv.DictReader(file, delimiter=';'))

        connection = psycopg2.connect(user="postgres",
                                      password="y@ppizo9",
                                      host="127.0.0.1",
                                      port="5432",
                                      database="netology_import_phones")
        cursor = connection.cursor()

        for phone in phones:
            Phone.id = phone.get('id')
            Phone.name = str(phone.get('name'))
            Phone.image = str(phone.get('image'))
            Phone.price = phone.get('price')
            Phone.release_date = phone.get('release_date')
            Phone.lte_exists = phone.get('lte_exists')
            Phone.slug = slugify(Phone.name)
            dataQuery = f"INSERT INTO phones_phone (id, name, image, price, release_date, lte_exists, slug)" \
                        f"VALUES ({Phone.id}, '{Phone.name}', '{Phone.image}', {Phone.price}, {Phone.release_date}, {Phone.lte_exists}, '{Phone.slug}')"
            cursor.execute(dataQuery)

        connection.commit()
        cursor.close()
        connection.close()
        return
