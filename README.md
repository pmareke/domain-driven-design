# Domain Driven Design example using Python

This repository is a work in progress exercise applying DDD to a weather app.

The app exposes an API endpoint included in the Delivery layer, this layer talks
with the Use Cases layer using command handlers.

This command handlers talks with the Infrastructure and Domain layers and returns
the result to the Delivery layer again.

## Design
![DDD](./images/DDD.png)

## Components
- Delivery: API Rest using FastAPI.
- Infrastructure: MongoDB and PyMongo.
- Use Cases: CommandHandlers.
- Domain: Domain objects.

## API endpoints
- GET     - `/health`: status of the app.
- GET     - `/api/v1/weather`: list the weather in all cities in the database.
- GET     - `/api/v1/weather/:id`: gets the weather of a given city.
- POST    - `/api/v1/weather`: creates a weather in the database.
- DELETE  - `/api/v1/weather/:id`: deletes the weather of a given city.
- UPDATE  - `/api/v1/weather/:id`: updates the weather of a given city.
