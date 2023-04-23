# Paired

Paired is a roommate and shared flats search service that helps users find compatible roommates and ideal living spaces. With Paired, users can create profiles, search for roommate and room ads, and connect with potential matches.

## Installation

To run Paired locally, you'll need to have Python 3.6 or higher installed on your machine. Clone the repository, navigate to the root directory, and install the required dependencies using the following command:

pip install -r requirements.txt

Start the application by running:

uvicorn app.main:app
You can access the application at `http://localhost:8000.`

## Usage

Paired's API provides the following endpoints:

/roommate_ads: endpoints for creating, updating, and retrieving roommate ads
/room_ads: endpoints for creating, updating, and retrieving room ads
/users: endpoints for creating, updating, and retrieving user profiles
/auth: endpoints for user authentication
To use the API, you'll need to send requests to the appropriate endpoints using an HTTP client such as cURL or Postman.

## Contributing

Contributions to Paired are always welcome! If you'd like to contribute, please follow these steps:

Fork the repository
Create a new branch for your feature or bug fix
Write your code and tests
Make sure your code passes the tests
Create a pull request

## License

Paired is licensed under the MIT License. See LICENSE for more information.
