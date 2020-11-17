import random

class Transport():
    class Plane():
        plane_value = str(input("Вкажіть вартість літака"))
        plane_speed = int(random.uniform(300, 1000))
        plane_height = int(random.uniform(1000, 11000))
        plane_year = str(input("Вкажіть рік випуску літака"))
        plane_passengers = int(random.uniform(5, 320))
    class Car():
        car_value = str(input("Вкажіть вартість автомобіля"))
        car_speed = int(random.uniform(10, 180))
        car_year = str(input("Вкажіть рік випуску автомобіля"))
        car_passengers = int(random.uniform(1, 5))
    class Ship():
        ship_value = str(input("Вкажіть вартість корабля"))
        ship_speed = int(random.uniform(5, 80))
        ship_year = str(input("Вкажіть рік випуску корабля"))
        ship_port = "Одеса"

    print("Літак: ", + plane_value, + str(plane_speed), + str(plane_height), + plane_year, + str(plane_passengers))

    print("Автомобіль: ", + car_value, + str(car_speed), + car_year, + str(car_passengers))

    print("Корабель: ", + ship_value, + str(ship_speed), + ship_year, + ship_port)

    