"""
Example usage of Kwork API Library (Sync)
"""

import os
import sys

from dotenv import load_dotenv

# Add library to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "pykwork"))

from pykwork import KworkAuthError, KworkRequestError, KworkSyncClient

# Load environment variables from .env file
load_dotenv()


def main():
    # Initialize client
    client = KworkSyncClient(
        username=os.getenv("KWORK_USERNAME"),
        password=os.getenv("KWORK_PASSWORD"),
        uad=os.getenv("KWORK_UAD", "test"),
        device=os.getenv("KWORK_DEVICE", "test"),
    )

    try:
        with client:
            # Login
            auth_response = client.login()
            print("Logged in successfully")
            print(f"Token: {client.token[:20]}...")
            print(f"Expires in: {auth_response['response']['expired']} seconds")
            print()

            # Get current user info
            actor = client.get_actor()
            print(f"User: {actor['response']['username']}")
            print(f"ID: {actor['response']['id']}")
            print(f"Email: {actor['response']['email']}")
            print(f"Type: {actor['response']['type']}")
            print()

            # Get connects info (коннекты)
            connects = client.get_connects()
            print(f"Коннекты: {connects['active_connects']} из {connects['all_connects']}")
            print()

            # Get categories
            categories = client.get_categories()
            print(f"Got {len(categories)} categories:")
            for cat in categories:
                print(f"  - {cat['name']} (ID: {cat['id']})")
            print()

            # Get projects (first 2 pages)
            projects = client.get_all_projects(max_pages=2)
            print(f"Got {len(projects)} projects")
            if projects:
                print(f"First project: {projects[0]['title']}")
                print(f"Price: {projects[0]['price']} RUB")
            print()

            # Get projects filtered by category (IT & Development)
            it_projects = client.get_all_projects(max_pages=1, categories="11")
            print(f"Got {len(it_projects)} IT projects")
            print()

            # Get user's offers
            offers = client.get_all_offers()
            print(f"Got {len(offers)} offers")
            if offers:
                print(f"First offer: {offers[0]['title']}")
                print(f"Price: {offers[0]['price']} RUB")
                print(f"Status: {offers[0]['status']}")
            print()

            # Get user by ID
            user = client.get_user(user_id=1)
            print(f"User: {user['response']['username']}")
            print(f"Full name: {user['response']['fullname']}")
            print()

            print("All operations completed successfully!")

    except KworkAuthError as e:
        print(f"Authentication error: {e}")
    except KworkRequestError as e:
        print(f"Request error: {e}")
        if e.status_code:
            print(f"Status code: {e.status_code}")
    except Exception as e:
        print(f"Unexpected error: {e}")


if __name__ == "__main__":
    main()
