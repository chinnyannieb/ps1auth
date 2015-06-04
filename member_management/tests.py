from accounts.models import PS1User
from .models import Person
from django.test import Client, TestCase
from pprint import pprint


class PersonTest(TestCase):

    def setUp(self):
        self.user = PS1User.objects.create_superuser("testuser", password="Garbage1",  email="foo@bar.com")
        self.client = Client()
        result = self.client.login(username='testuser', password='Garbage1')
        self.assertTrue(result)

    def tearDown(self):
        PS1User.objects.delete_user(self.user)

    def test_page_without_user(self):
        person = Person(
            first_name = "no_user",
            last_name = "none"
        )
        person.save()
        url = '/mm/person/{}'.format(person.pk)
        #print(url)
        response = self.client.get(url)

        self.assertEquals(200, response.status_code)

    def test_page_with_user_and_no_groups(self):
        lonely_person = Person(
            first_name = "lonely",
            last_name = "person"
        )
        lonely_person.save()
        lonely = PS1User.objects.create_user("lonely", password="Garbage1",  email="lonely@example.com")
        self.assertIsNotNone(lonely_person)
        lonely_person.user = lonely
        lonely_person.save()

        # view a person with a user account and no groups
        url = '/mm/person/{}'.format(lonely_person.id)
        response = self.client.get(url)
        self.assertEquals(200, response.status_code)

        #clieanup
        PS1User.objects.delete_user(lonely)


class QuorumTest(TestCase):

    def test_no_members(self):
        self.assertEqual(1, Person.objects.quorum())

    def test_no_full_members(self):
        Person.objects.create(first_name=".", last_name=".", membership_status="starving_hacker")
        self.assertEqual(1, Person.objects.quorum())

    def test_quorum(self):
        # no members
        self.assertEqual(1, Person.objects.quorum())

        Person.objects.create(first_name="1", last_name=".", membership_status="full_member")
        self.assertEqual(1, Person.objects.quorum())

        Person.objects.create(first_name="2", last_name=".", membership_status="full_member")
        self.assertEqual(1, Person.objects.quorum())

        Person.objects.create(first_name="3", last_name=".", membership_status="full_member")
        self.assertEqual(1, Person.objects.quorum())

        Person.objects.create(first_name="4", last_name=".", membership_status="full_member")
        self.assertEqual(2, Person.objects.quorum())
