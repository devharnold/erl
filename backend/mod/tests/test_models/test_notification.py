from django.test import TestCase
from mod.models import Notification
from django.contrib.auth.models import User

class NotificationTestCase(TestCase):
    """Test case for the { Notification } class model"""
    @classmethod
    def setUpTestData(cls):
        cls.test_user = User.objects.create(username='testuser', email='test@example.com', name='Test Name')
        cls.test_notification = Notification.objects.create(user=cls.test_user, title='Test Title', message='Test message', read_on_default=False)

    def test_notification_create(self):
        """Test for Notification created"""
        notification = Notification.objects.get(id=1)
        self.assertEqual(
            notification.user.username, 'testuser',
            notification.title, 'Test Title',
            notification.message, 'Test Message',
        )
        self.assertIsNotNone(notification.updated_at)
        self.assertTrue(notification.read_on_default, False)

    def test_notification_title_max_length(self):
        """Test to ensure the Notification title max_legnth is okay"""
        notification = self.notification
        max_length = self.notification._meta.get_field('title').max_length
        self.assertEqual(max_length, 225)

    def test_notification_created_at_auto_add_now(self):
        """Tests for auto add"""
        notification = self.notification
        self.assertIsNotNone(notification.created_at)

    def test_notification_by_category(self):
        """Test for the ntification object according to their linked categories"""
        notification1 = Notification.objects.create(username='testuser', title='Test Title 1', message='Test Message 1')
        notification2 = Notification.objects.create(username='testuser', title='Test Title 2', messsage='Test Message 2')
        notification1.category = 'Category 1'
        notification2.category = 'Category 2'
        self.assertEqual()
