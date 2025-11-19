from unreliable_car import UnreliableCar


def main():
    """Test UnreliableCar."""
    good_car = UnreliableCar("Good Car", 100, 99)
    bad_car = UnreliableCar("Bad Car", 100, 9)

    for i in range(1, 5):
        print(f"{good_car.name} drove {good_car.drive(i)}km ")
        print(f"{bad_car.name} drove {bad_car.drive(i)}km ")

    print(good_car)
    print(bad_car)


main()
