from django.db import models


class Owner(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)

    def str(self):
        return self.name

class Car(models.Model):
    make = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    year = models.IntegerField()
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)

    def str(self):
        return f'{self.make} {self.model} ({self.year})'

class Repair(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    description = models.TextField()
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    repair_date = models.DateField()

    def str(self):
        return f'Repair #{self.pk} - {self.car}'

class Maintenance(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    description = models.TextField()
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    maintenance_date = models.DateField()

    def str(self):
        return f'Maintenance #{self.pk} - {self.car}'

class Appointment(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    appointment_date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()

    def str(self):
        return f'Appointment #{self.pk} - {self.car}'

class Booking(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    date = models.DateField()
    time = models.TimeField()
    service = models.CharField(max_length=100)

class Client(models.Model):
    username = models.CharField(max_length=150)
    password = models.CharField(max_length=128)
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)