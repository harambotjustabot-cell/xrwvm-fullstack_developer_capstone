from .models import CarMake, CarModel


def initiate():
    """Populate the CarMake and CarModel tables with sample data."""
    car_make_data = [
        {"name": "Nissan", "description": "Japanese car manufacturer",
         "country": "Japan"},
        {"name": "Mercedes", "description": "Luxury German car manufacturer",
         "country": "Germany"},
        {"name": "Audi", "description": "German premium car manufacturer",
         "country": "Germany"},
        {"name": "Chevrolet", "description": "American car manufacturer",
         "country": "United States"},
        {"name": "Toyota", "description": "Japanese car manufacturer",
         "country": "Japan"},
    ]

    car_make_objects = []
    for make in car_make_data:
        car_make = CarMake.objects.get_or_create(
            name=make['name'],
            defaults={
                'description': make['description'],
                'country': make['country']
            }
        )[0]
        car_make_objects.append(car_make)

    car_model_data = [
        {"name": "Altima", "type": "SEDAN", "year": 2023, "car_make": "Nissan"},
        {"name": "Rogue", "type": "SUV", "year": 2023, "car_make": "Nissan"},
        {"name": "Pathfinder", "type": "SUV", "year": 2021,
         "car_make": "Nissan"},
        {"name": "C-Class", "type": "SEDAN", "year": 2022,
         "car_make": "Mercedes"},
        {"name": "GLC", "type": "SUV", "year": 2023, "car_make": "Mercedes"},
        {"name": "A4", "type": "SEDAN", "year": 2022, "car_make": "Audi"},
        {"name": "Q5", "type": "SUV", "year": 2023, "car_make": "Audi"},
        {"name": "A6", "type": "SEDAN", "year": 2020, "car_make": "Audi"},
        {"name": "Malibu", "type": "SEDAN", "year": 2019,
         "car_make": "Chevrolet"},
        {"name": "Tahoe", "type": "SUV", "year": 2023, "car_make": "Chevrolet"},
        {"name": "Camaro", "type": "COUPE", "year": 2021,
         "car_make": "Chevrolet"},
        {"name": "Corolla", "type": "SEDAN", "year": 2022, "car_make": "Toyota"},
        {"name": "RAV4", "type": "SUV", "year": 2023, "car_make": "Toyota"},
        {"name": "Prius", "type": "HATCHBACK", "year": 2023,
         "car_make": "Toyota"},
    ]

    make_lookup = {make.name: make for make in car_make_objects}
    for model in car_model_data:
        CarModel.objects.get_or_create(
            name=model['name'],
            car_make=make_lookup[model['car_make']],
            defaults={
                'type': model['type'],
                'year': model['year'],
                'dealer_id': 1
            }
        )

    print("Car makes and models populated successfully")
