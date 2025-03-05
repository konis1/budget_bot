# test_firebase.py
import unittest
from unittest.mock import patch, MagicMock
from budget_bot.firebase import initialize_firebase, test_firestore_connection


class TestFirebaseIntegration(unittest.TestCase):

    @patch('firebase_admin.initialize_app')
    @patch('firebase_admin.credentials.Certificate')
    @patch('firebase_admin.firestore.client')
    def test_initialize_firebase(self, mock_firestore_client, mock_certificate, mock_initialize_app):
        # Set up mocks
        mock_db = MagicMock()
        mock_firestore_client.return_value = mock_db

        # Test the function
        result = initialize_firebase()

        # Assertions
        mock_certificate.assert_called_once()
        mock_initialize_app.assert_called_once()
        self.assertEqual(result, mock_db)

    @patch('budget_bot.firebase.initialize_firebase')  # Replace with your actual file name
    def test_firestore_operations(self, mock_initialize_firebase):
        # Set up mocks
        mock_db = MagicMock()
        mock_collection = MagicMock()
        mock_doc_ref = MagicMock()
        mock_doc_snapshot = MagicMock()

        # Configure mocks
        mock_initialize_firebase.return_value = mock_db
        mock_db.collection.return_value = mock_collection
        mock_collection.add.return_value = (None, mock_doc_ref)
        mock_doc_ref.get.return_value = mock_doc_snapshot
        mock_doc_snapshot.to_dict.return_value = {'message': 'Test message', 'test_value': 42}

        # Test the function
        success, message = test_firestore_connection()

        # Assertions
        self.assertTrue(success)
        self.assertIn("successful", message)
        mock_db.collection.assert_called_once_with('test_collection')
        mock_collection.add.assert_called_once()
        mock_doc_ref.get.assert_called_once()
        mock_doc_ref.delete.assert_called_once()


if __name__ == '__main__':
    unittest.main()
