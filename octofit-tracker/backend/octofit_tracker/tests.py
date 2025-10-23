from django.test import TestCase
from .models import User, Team, Activity, Workout, Leaderboard

class ModelTests(TestCase):
    def test_team_creation(self):
        team = Team.objects.create(name='Marvel', description='Marvel superheroes')
        self.assertEqual(str(team), 'Marvel')

    def test_user_creation(self):
        team = Team.objects.create(name='DC', description='DC superheroes')
        user = User.objects.create(name='Superman', email='superman@dc.com', team=team, is_superhero=True)
        self.assertEqual(str(user), 'Superman')

    def test_activity_creation(self):
        team = Team.objects.create(name='Marvel', description='Marvel superheroes')
        user = User.objects.create(name='Iron Man', email='ironman@marvel.com', team=team, is_superhero=True)
        activity = Activity.objects.create(user=user, type='Running', duration=30, date='2025-10-23')
        self.assertEqual(str(activity), 'Iron Man - Running on 2025-10-23')

    def test_workout_creation(self):
        team = Team.objects.create(name='Marvel', description='Marvel superheroes')
        workout = Workout.objects.create(name='Cardio', description='Cardio workout')
        workout.suggested_for.add(team)
        self.assertEqual(str(workout), 'Cardio')

    def test_leaderboard_creation(self):
        team = Team.objects.create(name='Marvel', description='Marvel superheroes')
        leaderboard = Leaderboard.objects.create(team=team, score=100)
        self.assertEqual(str(leaderboard), 'Marvel - 100')
