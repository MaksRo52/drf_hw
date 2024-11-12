from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from lms.models import Course, Lesson, Subscription
from users.models import User


class LTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(email="admin@example.com")
        self.course = Course.objects.create(title='Test Course', description='Test Course Description', owner=self.user)
        self.lesson1 = Lesson.objects.create(title='Lesson 1', course=self.course, owner=self.user)
        self.lesson2 = Lesson.objects.create(title='Lesson 2', course=self.course, owner=self.user)
        self.client.force_authenticate(user=self.user)

    def test_course_retrieve(self):
        url = reverse("lms:course-detail", args=(self.course.pk,))
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get('title'), self.course.title)

    def test_course_create(self):
        url = reverse("lms:course-list")
        data = {
            "title": "New Course",
            "description": "New Course Description",
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Course.objects.count(), 2)

    def test_course_update(self):
        url = reverse("lms:course-detail", args=(self.course.pk,))
        data = {
            "title": "Updated Course",
            "description": "Updated Course Description",
        }
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Course.objects.get(pk=self.course.pk).title, "Updated Course")

    def test_course_delete(self):
        url = reverse("lms:course-detail", args=(self.course.pk,))
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Course.objects.count(), 0)

    def test_course_list(self):
        url = reverse("lms:course-list")
        response = self.client.get(url)
        data = response.json()
        result = {
            "count": 1,
            "next": None,
            "previous": None,
            "results": [
                {
                    "id": self.course.pk,
                    "lessons": ['Lesson 1', 'Lesson 2'],  # list(self.course.lesson.all())
                    "title": self.course.title,
                    "description": self.course.description,
                    "image": None,
                    "owner": self.user.pk
                },
            ]
        }
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data, result)

    def test_lesson_retrieve(self):
        url = reverse("lms:lessons_retrieve", args=(self.lesson1.pk,))
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get('title'), self.lesson1.title)

    def test_lessons_create(self):
        url = reverse("lms:lessons_create")
        data = {
            "title": "New Lesson",
            "description": "New Lesson Description",
            "course": self.course.pk,
            "owner": self.user.pk,
            "video_url": "http://youtube.com/new_lesson",
        }
        response = self.client.post(url, data)
        print(response.status_code)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Lesson.objects.count(), 3)

    def test_lessons_list(self):
        url = reverse("lms:lessons_list")
        response = self.client.get(url)
        data = response.json()
        result = {
            "count": 2,
            "next": None,
            "previous": None,
            "results": [
                {
                    "id": self.lesson1.pk,
                    "video_url": self.lesson1.video_url,
                    "title": self.lesson1.title,
                    "description": None,
                    "image": None,
                    "course": self.course.pk,
                    "owner": self.user.pk,
                }, {
                    "id": self.lesson2.pk,
                    "video_url": self.lesson2.video_url,
                    "title": self.lesson2.title,
                    "description": None,
                    "image": None,
                    "course": self.course.pk,
                    "owner": self.user.pk,
                }
            ]}
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data, result)

    def test_lesson_update(self):
        url = reverse("lms:lessons_update", args=(self.lesson1.pk,))
        data = {
            "title": "Updated Lesson",
            "description": "Updated Lesson Description",
            "course": self.course.pk,
            "owner": self.user.pk,
            "video_url": "http://youtube.com/updated_lesson",
        }
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Lesson.objects.get(pk=self.lesson1.pk).title, "Updated Lesson")

    def test_lesson_delete(self):
        url = reverse("lms:lessons_delete", args=(self.lesson1.pk,))
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Lesson.objects.count(), 1)


    def test_subscription(self):
        url = reverse("lms:subscriptions")
        data = {
            "course": self.course.pk,
        }
        response = self.client.post(url, data)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Subscription.objects.count(), 1)
        self.assertEqual(data, {'message': 'подписка добавлена'})
