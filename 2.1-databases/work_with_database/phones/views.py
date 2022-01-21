import psycopg2

from django.shortcuts import render, redirect

from operator import  itemgetter

def index(request):
    return redirect('catalog')

def get_sql_data():
    connection = psycopg2.connect(user="postgres",
                                  password="y@ppizo9",
                                  host="127.0.0.1",
                                  port="5432",
                                  database="netology_import_phones")
    cursor = connection.cursor()
    dataQuery = 'SELECT * FROM phones_phone'
    cursor.execute(dataQuery)
    rawPhones = list(cursor.fetchall())
    cursor.close()
    connection.close()
    return rawPhones

def context_maker (rawDataPhones):
    phone = {}
    phones = []
    for i in range(len(rawDataPhones)):
        phone['id'] = rawDataPhones[i][0]
        phone['name'] = rawDataPhones[i][1]
        phone['price'] = rawDataPhones[i][2]
        phone['image'] = rawDataPhones[i][3]
        phone['release_date'] = rawDataPhones[i][4]
        phone['lte_exists'] = rawDataPhones[i][5]
        phone['slug'] = rawDataPhones[i][6]
        phones.append(phone)
        phone = {}
    return phones

def sorting(request, phones, sort):
    if sort == 'name':
        phones.sort(key=itemgetter('name'))
    elif sort == 'min_price':
        phones.sort(key=itemgetter('price'))
    elif sort == 'max_price':
        phones.sort(key=itemgetter('price'), reverse=True)
    return phones

def show_catalog(request):
    template = 'catalog.html'
    phones = context_maker(get_sql_data())
    sort = request.GET.get('sort')
    newPhones = sorting(request, phones, sort)
    context = {
        'phones': newPhones
    }
    return render(request, template, context)

def show_product(request, slug):
    template = 'product.html'
    phones = context_maker(get_sql_data())
    for i in range(len(phones)):
        if phones[i].get('slug') == slug:
            phone = phones[i]
            break
    context = {
        'phone': phone,
    }
    return render(request, template, context)
