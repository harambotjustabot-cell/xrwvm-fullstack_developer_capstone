# Full Stack Application Development Capstone Project

**Project name:** Dealerships - Car Dealership Review Portal

**Capstone project for:** IBM Full Stack Software Developer Professional Certificate
(Full Stack Application Development Capstone Project, Module 6 - Share Your Project)

## Overview

Dealerships is a full stack web application that lets customers browse car
dealerships across the United States, read reviews left by other buyers, and post
their own reviews with a sentiment indicator. The application is built from four
independently deployable pieces that talk to each other over HTTP:

| Component | Technology | Responsibility |
| --- | --- | --- |
| `server/djangoapp` | Django 4.2 | Server-side rendering, user authentication, session handling, REST endpoints |
| `server/frontend` | React 18 | Single page application for login, registration, dealer list, dealer detail and review submission |
| `server/database` | Node.js / Express / Mongoose | REST API that serves dealerships, car makes and reviews from MongoDB |
| `server/djangoapp/microservices` | Flask + NLTK Vader | Microservice that returns the sentiment (positive / neutral / negative) of review text |

MongoDB stores the `dealerships` and `reviews` collections; Django stores users,
car makes and car models in SQLite.

## Features

* Static pages: Home, About Us, Contact Us, with a shared Bootstrap navigation bar.
* User management: registration, login, logout and an admin-only root account.
* Back end services: Express/Mongo REST API (`/fetchDealers`, `/fetchDealers/:state`,
  `/fetchDealer/:id`, `/fetchReviews`, `/fetchReviews/dealer/:id`, `/insert_review`).
* Dynamic pages: dealer list with state filter, dealer detail page with reviews,
  post-review form with car make/model selection.
* Sentiment analysis on every review through the Flask microservice.
* CI/CD: GitHub Actions workflow that installs the Python and Node dependencies,
  runs Django system checks and builds the React bundle on every push to `main`.
* Containerisation and cloud deployment (Docker, Kubernetes / Code Engine).

## Django endpoints

| Method | Endpoint | Description |
| --- | --- | --- |
| POST | `/djangoapp/login` | Authenticate a user |
| GET | `/djangoapp/logout` | Log the current user out |
| POST | `/djangoapp/register` | Register a new user |
| GET | `/djangoapp/get_dealers` | All dealerships |
| GET | `/djangoapp/get_dealers/<state>` | Dealerships filtered by state |
| GET | `/djangoapp/dealer/<dealer_id>` | Details of one dealership |
| GET | `/djangoapp/reviews/dealer/<dealer_id>` | Reviews of one dealership, with sentiment |
| POST | `/djangoapp/add_review` | Submit a review (authenticated users only) |
| GET | `/djangoapp/get_cars` | All car makes and models |

## Project structure

```
.
├── .github/workflows/main.yml     # CI pipeline
├── README.md
├── django_server                  # Terminal output: Django server running
├── loginuser / logoutuser         # cURL output: login and logout
├── getalldealers                  # cURL output: all dealers
├── getdealerbyid                  # cURL output: dealer by id
├── getdealersbyState              # cURL output: dealers in Kansas
├── getdealerreviews               # cURL output: reviews for a dealer
├── getallcarmakes                 # cURL output: car makes and models
├── analyzereview                  # cURL output: sentiment analysis
├── CICD                           # Terminal output: GitHub Actions run
├── deploymentURL                  # Public URL of the deployed application
├── *.png                          # Screenshots of completed tasks
└── server
    ├── database/                  # Express + Mongoose API
    ├── djangoapp/                 # Django app (models, views, views for admin)
    ├── djangoproj/                # Django project settings and urls
    ├── frontend/                  # React application and static pages
    └── manage.py
```

## Running the application locally

1. Start MongoDB:

   ```bash
   mongod --dbpath ~/data/db --port 27017
   ```

2. Start the Express/Mongo service on port 3030:

   ```bash
   cd server/database
   npm install
   MONGO_URL=mongodb://localhost:27017/ node app.js
   ```

3. Start the sentiment analyzer microservice on port 5050:

   ```bash
   cd server/djangoapp/microservices
   pip install -r requirements.txt
   python app.py
   ```

4. Start the Django application on port 8000:

   ```bash
   cd server
   python -m venv .venv && source .venv/bin/activate
   pip install -r requirements.txt
   python manage.py migrate
   python manage.py runserver
   ```

5. Build the React front end (served by Django from the same origin):

   ```bash
   cd server/frontend
   npm install
   npm run build
   ```

The application is then available at <http://localhost:8000>.

## Notes

* The admin user `root` can sign in at `/admin/` to manage car makes and car models.
* `server/djangoapp/.env` holds the URLs of the Express back end and the sentiment
  microservice, so either can be pointed at a cloud deployment without code changes.
