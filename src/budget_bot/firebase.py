import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import os
import json
from datetime import datetime
from dotenv import load_dotenv



def initialize_firebase():
    """Initialize Firebase with service account credentials."""
    try:
        # Check if already initialized
        if not firebase_admin._apps:
            load_dotenv()
            if os.getenv('GOOGLE_APPLICATION_CREDENTIALS'):
                cred_dict = json.loads(os.getenv('GOOGLE_APPLICATION_CREDENTIALS'))
                cred = credentials.Certificate(cred_dict)
            else:
                raise ValueError("Firebase credentials not found. Please provide either a firebase-credentials.json file or set the FIREBASE_CREDENTIALS environment variable.")
            firebase_admin.initialize_app(cred)

        # Return Firestore client
        return firestore.client()

    except Exception as e:
        print(f"Error initializing Firebase: {e}")
        raise


def test_firestore_connection():
    """Test writing to and reading from Firestore."""
    try:
        # Initialize Firebase
        db = initialize_firebase()

        # Create test document data
        test_data = {
            'message': 'Test message',
            'timestamp': datetime.now(),
            'test_value': 42
        }

        # Reference to test collection
        test_collection = db.collection('test_collection')

        # Write data
        doc_ref = test_collection.add(test_data)[1]
        print(f"Document written with ID: {doc_ref.id}")

        # Read the data back
        read_data = doc_ref.get().to_dict()
        print(f"Read data: {read_data}")

        # Clean up - delete the test document
        doc_ref.delete()
        print("Test document deleted")

        return True, "Firebase connection test successful!"

    except Exception as e:
        return False, f"Firebase connection test failed: {e}"


if __name__ == "__main__":
    success, message = test_firestore_connection()
    print(message)
