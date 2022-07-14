from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from django.utils.crypto import get_random_string

class Command(BaseCommand):
    help = 'Create random users'

    def add_arguments(self, parser):
        parser.add_argument('total', type=int, help='Indicates the number of users to be created')
        parser.add_argument('-p', '--prefix', type=str, help='Define a username prefix', )

    def handle(self, *args, **kwargs):
        total = kwargs['total']
        prefix = kwargs['prefix']
        for i in range(total):
            if prefix:
                username = '{prefix}_{random_string}'.format(prefix=prefix, random_string=get_random_string())
            else:
                username = get_random_string()
            User.objects.create_user(username=get_random_string(1), email='', password='123')

# class Command(BaseCommand):
#     help = 'Generate random users'

#     def add_arguments(self, parser):
#         parser.add_argument('count', type=int, help='Indicates the number of users to be created')
#         parser.add_argument('-p', '--prefix', type=str, help='Define a username prefix')
#         parser.add_argument('-s', '--superuser', action='store_true', help='Create a superuser account')

#     def handle(self, *args, **kwargs):
#         count = kwargs['count']
#         prefix = kwargs['prefix']
#         superuser = kwargs['superuser']

#         for i in range(count):
#             if prefix:
#                 username = f'{prefix}_{get_random_string()}'
#             else:
#                 username = get_random_string()

#             if superuser:
#                 User.objects.create_superuser(username=username, email='hello@hi.com', password='123')
#             else:
#                 User.objects.create_user(username=username, email='hello@hi.com', password='123')
#                 