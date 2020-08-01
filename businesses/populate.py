from faker import Faker
from .models import Business
import django


django.setup()


def add_data(data1, data2):
    d, created = ModelInApp.objects.get_or_create(data1=data1, data2=data2)
    print("- Data: {0}, Created: {1}".format(str(d), str(created)))
    return d


def populate():
    fake = Faker()
    print(fake.name())

    # for row in data:
    #     data1 = row[0]
    #     data2 = row[1]
    #     add_data(data1, data2)


if __name__ == "__main__":
    populate()

    #     author = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
    # businessname = models.CharField(max_length=255)
    # businesstype = models.CharField(max_length=255, choices=Business_Type)
    # address = models.CharField(max_length=255)
    # address2 = models.CharField(max_length=255, default='None')
    # city = models.CharField(max_length=255)
    # province = models.CharField(max_length=255, choices=Province)
    # postal_code = models.CharField(max_length=255, default='None')
    # logo = models.ImageField(default='None')
