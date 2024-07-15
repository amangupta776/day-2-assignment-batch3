# test_info.py
# Copyright (c) 2024, Aman and Contributors
# See license.txt

import frappe
from frappe.tests.utils import FrappeTestCase

class TestInfo(FrappeTestCase):

    def setUp(self):
        # Setup code to initialize necessary data
        self.test_doc = frappe.get_doc({
            'doctype': 'Info',
            'name': 'John Doe',
            'age': 30,
            'number': '1234567890'
        })
        self.test_doc.insert()
        

    def tearDown(self):
        # Clean up code
        if frappe.db.exists('Info', self.test_doc.name):
            frappe.delete_doc('Info', self.test_doc.name)

    def test_create_record(self):
        # Test creating a new record
        new_doc = frappe.get_doc({
            'doctype': 'Info',
            'name': 'Jane Doe',
            'age': 25,
            'number': '0987654321'
        })
        new_doc.insert()
        self.assertEqual(new_doc.name, 'Jane Doe')
        self.assertEqual(new_doc.age, 25)
        self.assertEqual(new_doc.number, '0987654321')

    def test_name_validation(self):
        # Test validation for name field
        invalid_doc = frappe.get_doc({
            'doctype': 'Info',
            'name': '',
            'age': 30,
            'number': '1234567890'
        })
        with self.assertRaises(frappe.exceptions.ValidationError):
            invalid_doc.insert()

    def test_age_validation(self):
        # Test validation for age field
        invalid_doc = frappe.get_doc({
            'doctype': 'Info',
            'name': 'John Doe',
            'age': -1,
            'number': '1234567890'
        })
        with self.assertRaises(frappe.exceptions.ValidationError):
            invalid_doc.insert()

    def test_number_validation(self):
        # Test validation for number field
        invalid_doc = frappe.get_doc({
            'doctype': 'Info',
            'name': 'John Doe',
            'age': 30,
            'number': 'invalid_number'
        })
        with self.assertRaises(frappe.exceptions.ValidationError):
            invalid_doc.insert()

    def test_update_record(self):
        # Test updating a record
        self.test_doc.age = 31
        self.test_doc.number = '0987654321'
        self.test_doc.save()
        updated_doc = frappe.get_doc('Info', self.test_doc.name)
        self.assertEqual(updated_doc.age, 31)
        self.assertEqual(updated_doc.number, '0987654321')

    def test_delete_record(self):
        # Test deleting a record
        doc_name = self.test_doc.name
        self.test_doc.delete()
        with self.assertRaises(frappe.DoesNotExistError):
            frappe.get_doc('Info', doc_name)