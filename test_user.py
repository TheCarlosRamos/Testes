import unittest
from user_type_util import UserType  

class TestUserType(unittest.TestCase):
    def test_user_type_does_not_exist(self):
        with self.assertRaises(Exception) as context:
            UserType.is_valid_user_type('invalid_type')
        self.assertEqual(str(context.exception), "User type (invalid_type) does not exist")

    def test_university_user_wrong_type(self):
        with self.assertRaises(Exception) as context:
            UserType.is_valid_user_type('wrong_type', models.UniversityUser)
        expected_error = "Wrong User type (wrong_type) for this Model User (<UniversityUser model>)"
        self.assertEqual(str(context.exception), expected_error)

    def test_custom_user_wrong_type(self):
        with self.assertRaises(Exception) as context:
            UserType.is_valid_user_type('wrong_type', models.CustomUser)
        expected_error = "Wrong User type (wrong_type) for this Model User (<CustomUser model>)"
        self.assertEqual(str(context.exception), expected_error)

    def test_get_user_type_by_model_custom_user(self):
        result = UserType.get_user_type_by_model(models.CustomUser)
        self.assertEqual(result, models.CustomUser.super_user_type)

    def test_get_user_type_by_model_university_user(self):
        result = UserType.get_user_type_by_model(models.UniversityUser)
        self.assertEqual(result, models.CustomUser.university_user_type)

if __name__ == '__main__':
    unittest.main()
