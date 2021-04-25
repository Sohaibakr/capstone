
import json
import os
import unittest
from flask import url_for
from flask_sqlalchemy import SQLAlchemy
from app import create_app
from models import setup_db, Actor, Movie
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()


class AgencyTestCase(unittest.TestCase):

    """This class represents the agency's test case"""

    def setUp(self):
        """Define test variables and initialize app."""

        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = 'capstonefsnd_test'
        self.database_path = 'postgresql://{}:{}@{}/{}'.format(
                             'postgres', 'admin',
                             'localhost:5432', self.database_name)

        setup_db(self.app, self.database_path)

        # binds the app to the current context

        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            self.db.drop_all()

            # create all tables

            self.db.create_all()

        # initiate the test database with dummy records.

        for i in range(5):
            new_actor = self.create_actor()
            actor = Actor(name=new_actor['name'],
                          age=new_actor['age'],
                          gender=new_actor['gender'])
            actor.insert()

            new_movie=self.create_movie()
            movie = Movie(title=new_movie['title'],
                release=new_movie['release'])
            movie.insert()

    def create_actor(self):
        return {
                'name': 'Ashley Young', 'age': 21,
                'gender': 'male'
                }
    def create_movie(self):
        return {
                'title': 'Bad Blood',
                'release': datetime.utcnow()
                }

    def producer_header(self):
        return {'Authorization': 'Bearer {}'.format(os.environ['PRODUCER_TOKEN'])}

    def director_header(self):
        return {'Authorization': 'Bearer {}'.format(os.environ['DIRECTOR_TOKEN'])}
    
    def assistant_header(self):
        return {'Authorization': 'Bearer {}'.format(os.environ['ASSISTANT_TOKEN'])}
    
    def tearDown(self):
        """Executed after reach test"""

        pass

    # movie API test cases

    def test_creating_movie_success(self):

        # POST movie with the PRODUCER TOKEN

        response = self.client().post(
                                      '/movies',
                                      headers=self.producer_header(),
                                      json=self.create_movie())
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_creating_movie_failure(self):

        # POST movie with DIRECTOR TOKEN, no permissions

        response = self.client().post(
                                      '/movies',
                                      headers=self.director_header(),
                                      json=self.create_movie())
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 401)
        self.assertEqual(data['success'], False)

    def test_delete_movie_success(self):

        # DELETE movie with the PRODUCER TOKEN

        movie = Movie.query.all()[0]
        response = self.client().delete('/movies/{}'.format(movie.id),
                                        headers=self.producer_header())
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_delete_movie_failure(self):

        # DELETE movie with DIRECTOR TOKEN, no permissions

        movie = Movie.query.all()[0]
        response = self.client().delete('/movies/{}'.format(movie.id),
                                        headers=self.director_header())
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 401)
        self.assertEqual(data['success'], False)

    def test_patch_movies_success(self):

        # PATCH movie with the PRODUCER TOKEN

        movie = Movie.query.all()[0]
        response = self.client().patch('/movies/{}'.format(movie.id),
                                       headers=self.producer_header(),
                                       json=self.create_movie())
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_patch_movies_failure(self):

        # PATCH movie with no TOKEN

        movie = Movie.query.all()[0]
        response = self.client().patch('/movies/{}'.format(movie.id),
                                       json=self.create_movie())
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 401)
        self.assertEqual(data['success'], False)

    # actor API test cases

    def test_creating_actor_success(self):

        # POST actor with the PRODUCER TOKEN

        response = self.client().post('/actors',
                                      headers=self.producer_header(),
                                      json=self.create_actor())
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_creating_actor_failure(self):

        # POST actor with NO TOKEN

        response = self.client().post('/actors', json=self.create_actor())
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 401)
        self.assertEqual(data['success'], False)

    def test_delete_actor_success(self):

        # DELETE actor with the PRODUCER TOKEN

        actor = Actor.query.all()[0]
        response = self.client().delete('/actors/{}'.format(actor.id),
                                        headers=self.producer_header())
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_delete_actor_failure(self):

        # DELETE actor with NO TOKEN

        actor = Actor.query.all()[0]
        response = self.client().delete('/actors/{}'.format(actor.id))
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 401)
        self.assertEqual(data['success'], False)

    def test_patch_actor_success(self):

        # patching actor with the PRODUCER TOKEN, he have the permissions

        actor = Actor.query.all()[0]
        response = self.client().patch('/actors/{}'.format(actor.id),
                                       headers=self.producer_header(),
                                       json=self.create_actor())
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_patch_actor_failure(self):

        # PATCH with no TOKEN

        actor = Actor.query.all()[0]
        response = self.client().patch('/actors/{}'.format(actor.id),
                                       json=self.create_actor())
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 401)
        self.assertEqual(data['success'], False)

    def test_getting_movies_success(self):

        response = self.client().get('/movies',
                                     headers=self.assistant_header())
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_getting_movies_failure(self):

        # endpoint that cannot be accessed without token

        response = self.client().get('/movies')
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 401)
        self.assertEqual(data['success'], False)

    def test_getting_actors_success(self):

        response = self.client().get('/actors',
                                     headers=self.assistant_header())
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_getting_actors_failure(self):

        # endpoint that cannot be accessed without token

        response = self.client().get('/movies')
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 401)
        self.assertEqual(data['success'], False)


if __name__ == '__main__':
    unittest.main()