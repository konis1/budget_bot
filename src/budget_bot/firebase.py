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
        # Check if Firebase is already initialized
        if not firebase_admin._apps:
            load_dotenv()

            env_value = os.getenv('GOOGLE_APPLICATION_CREDENTIALS')

            if not env_value:
                raise ValueError("GOOGLE_APPLICATION_CREDENTIALS is not set or is empty.")

            # If it's a file path, read from the file
            if os.path.exists(env_value):
                with open(env_value, 'r') as f:
                    cred_dict = json.load(f)
            else:
                raise ValueError(f"Firebase credentials file not found at: {env_value}")

            cred = credentials.Certificate(cred_dict)
            firebase_admin.initialize_app(cred)

        # Return Firestore client
        return firestore.client()

    except Exception as e:
        print(f"Error initializing Firebase: {e}")
        raise


def add_expense(user_id: int, amount: float, category: str, description: str = "", date: datetime = None):
    """
    Adds an expense record to Firestore
    """
    try:
        db = initialize_firebase()

        if not date:
            date = datetime.now()

        expense_data = {
            "user_id": user_id,
            "amount": amount,
            "category": category,
            "description": description,
            "date": date,
        }

        expense_collection = db.collection("expenses")
        expense_collection.add(expense_data)

    except Exception as e:
        return f"Firebase add_expense failed: {e}"

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
