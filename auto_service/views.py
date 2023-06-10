from django.shortcuts import render
from autoService.models import Car, Owner, Repair, Booking, Client
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseServerError
import json


def car_list(request):
    if request.method == 'POST':
        car = Car(
            make=request.POST.get('make'),
            model=request.POST.get('model'),
            year=request.POST.get('year'),
            owner_id=request.POST.get('owner_id'),
            )
        car.save()

        return JsonResponse({'message': 'Car created successfully.'})
    elif request.method == 'GET':
        cars = Car.objects.all()
        return render(request, 'car_list.html', {'cars': cars})
    elif request.method == 'DELETE':
        data = request.body.decode('utf-8')
        json_data = json.loads(data)
        car_id = json_data.get('car_id')
        try:
            car = Car.objects.get(id=car_id)
            car.delete()
            return JsonResponse({'message': 'Car deleted successfully'})
        except Car.DoesNotExist:
            return JsonResponse({'message': 'Car not found'}, status=404)

    else:
        return JsonResponse({'message': 'Invalid request method.'})


def owner_list(request):
    if request.method == 'POST':
        owner = Owner(
            name=request.POST.get('name'),
            address=request.POST.get('address'),
            phone=request.POST.get('phone'),
            )
        owner.save()
        return JsonResponse({'message': 'Owner created successfully.'})
    elif request.method == 'GET':
        owners = Owner.objects.all()
        return render(request, 'owner_list.html', {'owners': owners})
    elif request.method == 'DELETE':
        data = request.body.decode('utf-8')
        json_data = json.loads(data)
        owner_id = json_data.get('owner_id')
        try:
            owner = Owner.objects.get(id=owner_id)
            owner.delete()
            return JsonResponse({'message': 'Owner deleted successfully'})
        except Car.DoesNotExist:
            return JsonResponse({'message': 'Owner not found'}, status=404)


def repair_list(request):
    repairs = Repair.objects.all()
    return render(request, 'repair_list.html', {'repairs': repairs})


def main_page(request):
    return render(request, 'index.html')


def calendar_page(request):
    booked_dates = []
    bookings = Booking.objects.all()
    for booking in bookings:
        booked_dates.append(str(booking.date))
    context = {'booked_dates': booked_dates}
    return render(request, 'calendar.html', context=context)


def uslugi_page(request):
    username = request.session.get('username')
    if username:
        try:
            client = Client.objects.get(username=username)
            context = {
                'client': client,
            }
            return render(request, 'uslugi.html', context)
        except Client.DoesNotExist:
            return lk_page(request)
    else:
        return lk_page(request)


def contact_page(request):
    return render(request, "contacts.html")


def success_page(request):
    return render(request, "success.html")


def lk_page(request):
    username = request.session.get('username')
    if username:
        try:
            return profile(request)
        except Client.DoesNotExist:
            lk_page(request)
    else:
        return render(request, "lk.html")


def save_booking(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        date = request.POST.get('date')
        service = request.POST.get('service').replace("_", " ")
        booking = Booking(name=name, phone=phone, date=date, time=request.POST.get('time'), service=service)
        booking.save()

        return JsonResponse({'status': 'success'})


def bookings(request):
    if request.method == 'DELETE':
        try:
            booking_id = int(str(request.body).split(":")[1].replace('"', "").replace('}', '').replace("'", ""))
            booking = Booking.objects.get(id=booking_id)
            booking.delete()
            return JsonResponse({'message': 'Запись успешно удалена'})
        except Booking.DoesNotExist:
            return JsonResponse({'error': 'Запись не найдена'}, status=404)
        except Exception as exception:
            return JsonResponse({'error': str(exception)}, status=500)
    else:
        return JsonResponse({'error': 'Метод не поддерживается'}, status=405)


@csrf_exempt
def register_page(request):
    if request.method == 'POST':
        login = request.POST.get('username')
        password = request.POST.get('password')
        address = request.POST.get('address')
        owner = Owner(name=request.POST.get('name'), address=address, phone=request.POST.get('phone'))
        owner.save()
        user = Client(username=login, password=password, owner=owner)
        user.save()
        return JsonResponse({'status': 'success'})


@csrf_exempt
def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            client = Client.objects.get(username=username)
        except Client.DoesNotExist:
            return HttpResponseServerError('Неверное имя пользователя или пароль.')
        if client.password == password:
            request.session['username'] = username
            return render(request, 'profile.html')
    else:
        return HttpResponseServerError('Метод запроса должен быть POST.')


def profile(request):
    username = request.session.get('username')
    if username:
        try:
            client = Client.objects.get(username=username)
            all_bookings = Booking.objects.all()
            print(all_bookings)
            context = {
                'client': client,
                'bookings': all_bookings,
            }
            return render(request, 'profile.html', context)
        except Client.DoesNotExist:
            return lk_page(request)
    else:
        lk_page(request)
