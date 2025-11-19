from silver_service_taxi import SilverServiceTaxi


def main():
    """Test Silver Service Taxi class"""
    taxi = SilverServiceTaxi("Silver Service Taxi", 100, 2)
    taxi.drive(18)
    print(taxi)
    print(taxi.get_fare())


main()
