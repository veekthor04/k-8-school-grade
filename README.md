# k-8-school-grade
Coding Challenge


## Endpoints

#### School (Get)

`GET ​/school/`

List all school

#### Chart (Get)

`GET ​/chart/{chart_id}/`

Retrieves chart details


## Running

Create a .env file using the .env.sample file as a template

To run the app you can use docker-compose:

```
docker-compose up --build -d
```

To stop the app:

```
docker-compose down
```

To run tests:

```
docker-compose run --rm app sh -c "python manage.py test"
```

The app will be accessed at `localhost:8000`.

## API Documentation

ReDoc at `localhost:8000/redoc/`

Swagger-ui at  `localhost:8000/swagger/`
