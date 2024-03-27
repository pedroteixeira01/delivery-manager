# Delivery Manager v0.1

## How to install
1. Clone or download this repository;
2. go to the project directory and run in terminal `pip install -r requirements.txt` to install python project dependencies;
3. after, go to the vue_app directory and run in terminal `npm install` to install vue dependencies;

## How to Run
1. If you want seeds to test it, go to the root of the project and run in terminal `python manage.py importcsv --truck ./seeds/trucks.csv --cargo ./seeds/cargo.csv`;
2. then, start the api with `python manage.py runserver` and the frontend with `npm run serve`;
3. open your browser and access `http://localhost:8080`;
4. enjoy ✨

## Features
- List all trucks saved on the database
- List all teh cargos saved on database
- List optimal mapping for trucks and cargo based on distance between origin. each truck can only carry up to one cargo and each truck can only make up to one trip.
