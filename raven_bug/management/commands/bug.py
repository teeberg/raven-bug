from django.core.management import BaseCommand
from django.urls import get_resolver
from raven.contrib.django.resolver import RouteResolver


class Command(BaseCommand):
    def handle(self, *args, **options):
        resolver = get_resolver()
        route_resolver = RouteResolver()
        print(route_resolver._resolve(resolver, '/api/v1/thing/'))
