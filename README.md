# FastAPI User Registration and Authentication

This is a project for implementing user registration and authentication in FastAPI, using JWT tokens and email verification. The project is still in progress, and the following features are planned:

- User registration
- JWT authentication with FastAPI
- Email verification using FastAPI-Mail

## Installation

1. Clone the repository:

  git clone https://github.com/vishalrajputt/FastAPI--E-Commerce-API-.git

  cd FastAPI--E-Commerce-API


2. Install the requirements:

pip install -r requirements.txt


3. Create a `.env` file and add the following variables:

DATABASE_URL=sqlite:///./database.sqlite3

SECRET_KEY=your-secret-key

EMAIL_USERNAME=your-email-username

EMAIL_PASSWORD=your-email-password

EMAIL_FROM=email-address-to-send-from


Replace `your-secret-key`, `your-email-username`, `your-email-password`, and `email-address-to-send-from` with your own values.


4. Start the server:

uvicorn main:app --reload


The server will start on `http://127.0.0.1:8000/docs#/`.

![image](https://user-images.githubusercontent.com/49341676/222263169-a8dc5bda-a3af-4186-aa8f-93cd6adfc1f2.png)


Register a new user. Requires the following parameters in the request body:

- `username`: a string with the username
- `email`: a string with the email
- `password`: a string with the password

Returns a JSON object with the following keys:

- `id`: the user's ID
- `username`: the user's username
- `email`: the user's email

### Execute 
![Capture](https://user-images.githubusercontent.com/49341676/222263374-774cf490-10af-4d2a-825e-70ba93152e96.JPG)

### Responses
![image](https://user-images.githubusercontent.com/49341676/222263617-e99064eb-7edc-4275-9492-59f6fda37aba.png)

---------------------------------------------------------------------------------------------------------------------------------------------------------
![360_F_520484683_j4f2om7llvZD1aoL9HPZ2LmDeWWZoWK0](https://user-images.githubusercontent.com/49341676/222263855-76573757-fbd5-40de-bdbb-056d12774211.jpg)







