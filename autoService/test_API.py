from django.test import TestCase
from django.urls import reverse
from autoService.models import Car, Owner, Booking


class AllAPITestCase(TestCase):
    def setUp(self):
        self.car_data = {
            'make': 'Toyota',
            'model': 'Camry',
            'year': 2022,
            'owner_id': 1,
        }
        self.owner_data = {
            'name': 'John Doe',
            'phone': '88005553535',
            'address': '12345',
        }
        self.booking_data = {
            'name': 'John Doe',
            'phone': '555-1234',
            'date': '2022-01-01',
            'time': '09:00:00',
            'service': 'Oil Change',
        }
        self.client_data = {
            'username': 'johndoe',
            'password': 'password',
            'owner': 1,
        }



    def test_create_owner(self):
        url = reverse('owner-list')
        response = self.client.post(url, data=self.owner_data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Owner.objects.count(), 1)
        owner = Owner.objects.first()
        self.assertEqual(owner.name, self.owner_data['name'])
        self.assertEqual(owner.phone, self.owner_data['phone'])
        self.assertEqual(owner.address, self.owner_data['address'])
    
    def test_create_car(self):
        self.test_create_owner()
        url = reverse('car-list')
        response = self.client.post(url, data=self.car_data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Car.objects.count(), 1)
        car = Car.objects.first()
        self.assertEqual(car.make, self.car_data['make'])
        self.assertEqual(car.model, self.car_data['model'])
        self.assertEqual(car.year, self.car_data['year'])

    def test_create_booking(self):
        url = reverse('save_booking-page')
        response = self.client.post(url, data=self.booking_data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Booking.objects.count(), 1)
        booking = Booking.objects.first()
        self.assertEqual(booking.name, self.booking_data['name'])
        self.assertEqual(booking.phone, self.booking_data['phone'])
        self.assertEqual(booking.date.strftime('%Y-%m-%d'), self.booking_data['date'])
        self.assertEqual(booking.time.strftime('%H:%M:%S'), self.booking_data['time'])


class PageAvailabilityTest(TestCase):
    def test_admin_page(self):
        url = reverse('admin:index')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)

    def test_car_list_page(self):
        url = reverse('car-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_owner_list_page(self):
        url = reverse('owner-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_repair_list_page(self):
        url = reverse('repair-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_main_page(self):
        url = reverse('main-page')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_calendar_page(self):
        url = reverse('calendar-page')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_uslugi_page(self):
        url = reverse('uslugi-page')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_contacts_page(self):
        url = reverse('contacts-page')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_success_page(self):
        url = reverse('success-page')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_bookings_page(self):
        url = reverse('bookings-page')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 405)

    def test_lk_page(self):
        url = reverse('lk-page')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_register_page(self):
        url = reverse('register-page')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
