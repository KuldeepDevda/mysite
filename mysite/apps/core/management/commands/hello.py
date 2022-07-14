from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Displays.'

    def handle(self, *args, **kwargs):
        self.stdout.write("Hello User!")
