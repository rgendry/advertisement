from django.shortcuts import get_object_or_404
from django.http import HttpResponse, JsonResponse, Http404
from django.core.paginator import Paginator    
from .serializers import AdSerializer, CreateAdSerilizer, FieldsSerializer     
from .models import Ad
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

def get_only_one_photo(data):
    d = {}
    for key in data:
        if key == 'photos':
            d['photo'] = data[key][0]
        else: 
            d[key] = data[key]
    return d

def get_sorts(sort_date, sort_price):
    sort = []
    if sort_date and (sort_date == 'asc' or sort_date == 'desc'):
        sort.append('date' if sort_date == 'asc' else '-date')
    if sort_price and (sort_price == 'asc' or sort_price == 'desc'):
        sort.append('price' if sort_price == 'asc' else '-price')
    return sort

def get_list(request):
    page = request.GET.get('page', 1)
    sort_date = request.GET.get('sort_date')
    sort_price = request.GET.get('sort_price')
    objects = Ad.objects.order_by(*get_sorts(sort_date, sort_price))
    pagination = Paginator(objects, 10)
    ads = pagination.get_page(page)
    serializer = AdSerializer(ads, many=True)
    d = []
    for value in serializer.data:
        d.append(get_only_one_photo(value))
    return JsonResponse(d, safe=False)

@csrf_exempt
def create(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = CreateAdSerilizer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'id': serializer.data['id']}, status=201)
        return JsonResponse(serializer.errors, status=400)

def get_item(request, id):
    fields = request.GET.get('fields')
    try:
        ad = Ad.objects.get(id=id)
    except Ad.DoesNotExist:
        return JsonResponse({'message': "Page doesn't exist"}, status=404)
    d = {}
    if fields:
        d = FieldsSerializer(ad).data
    else:
        d = get_only_one_photo(AdSerializer(ad).data)
    return JsonResponse(d, status=201)
