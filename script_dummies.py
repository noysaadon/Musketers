import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
django.setup()

from login.enums import VolunteerType
from login.models import User, Company
from volnteer.models import Volunteer


class Dummies:

    def __init__(self):
        self.user = self.create_user()
        self.company = self.create_company()

    @staticmethod
    def create_user():
        user, created = User.objects.get_or_create(
            username='user',
            fullname='user',
            email='user@user.com',
            password='1234'
        )

        return user.id

    @staticmethod
    def create_company():
        company, created = Company.objects.get_or_create(
            name='Big From Life',
            address='Tel Aviv',
            phone_number='+972888292',
            mail='bigfromlife@mail.com',
            website='https://gdolim.org.il/'
        )

        return company

    def create_volunteer(self):
        volunteer, created = Volunteer.objects.get_or_create(
            name='Help small children',
            description='Lets help some children to make with them homework, play and eat together',
            company=self.company,
        )
        volunteer.participate.add(self.user)

        volunteer.save()

        return volunteer

    def create_charity(self):
        charity, created = Volunteer.objects.get_or_create(
            name='Help small babys to get them food',
            description='Lets help small babys to buy them food',
            company=self.company,
            type=VolunteerType.CHARITY.value,
        )
        charity.participate.add(self.user)

        charity.save()
        return charity


def main():
    print('start to create!')
    dummies = Dummies()
    dummies.create_volunteer()
    dummies.create_charity()
    print('Done!')

if __name__ == "__main__":
    main()
