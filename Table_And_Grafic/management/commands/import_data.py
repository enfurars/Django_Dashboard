import json
from django.core.management.base import BaseCommand
from Table_And_Grafic.models import Simulation, User

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        with open('Table_And_Grafic/data/simulations.json', encoding='utf-8') as f:
            simulations = json.load(f)['simulations']
            for sim in simulations:
                simulation, created = Simulation.objects.get_or_create(
                    simulation_id=sim['simulation_id'],
                    defaults={
                        'simulation_name': sim['simulation_name'],
                        'company_id': sim['company_id'],
                        'company_name': sim['company_name'],
                    }
                )
                if not created:
                    simulation.simulation_name = sim['simulation_name']
                    simulation.company_id = sim['company_id']
                    simulation.company_name = sim['company_name']
                    simulation.save()

        with open('Table_And_Grafic/data/users.json', encoding='utf-8') as f:
            users = json.load(f)['users']
            for user in users:
                simulation = Simulation.objects.get(simulation_id=user['simulation_id'])
                user_obj, created = User.objects.get_or_create(
                    user_id=user['user_id'],
                    defaults={
                        'user_name': user['user_name'],
                        'user_surname': user['user_surname'],
                        'simulation': simulation,
                        'signup_datetime': user['signup_datetime'],
                        'progress_percent': user['progress_percent'],
                    }
                )
                if not created:
                    user_obj.user_name = user['user_name']
                    user_obj.user_surname = user['user_surname']
                    user_obj.simulation = simulation
                    user_obj.signup_datetime = user['signup_datetime']
                    user_obj.progress_percent = user['progress_percent']
                    user_obj.save()