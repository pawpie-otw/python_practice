import datetime as dt


class TripException(Exception):
    "my own exception class"

    def __init__(self, text, description: str) -> None:
        super().__init__(text)
        self.description = description

    def __str__(self) -> str:
        return super().__str__()+"\n"+self.description


class TripNameException(TripException):
    "Error raised when trip's name is missing"

    def __init__(self, text: str) -> None:
        super().__init__(text, 'Name of the trip is missing. You need to name the trip somehow...')


class TripDateException(TripException):
    "Error raised when date is incorrect"

    def __init__(self, text: str) -> None:
        super().__init__(text,
                         'The dates are incorrect. The starting date should be earlier than the ending date...')


class Trip:
    def __init__(self, symbol, title, start, end):
        self.symbol = symbol
        self.title = title
        self.start = start
        self.end = end

    def check_data(self):
        if len(self.title) == 0:
            raise TripNameException("Title is empty!")
        if self.start > self.end:
            raise TripDateException("Start date is later than end date!")

    @classmethod
    def publish_offer(cls, trips):

        list_of_errors = []

        for trip in trips:
            try:
                trip.check_data()
            except TripNameException as e:
                list_of_errors.append("{}: {}".format(trip.symbol, str(e)))
            except TripDateException as e:
                list_of_errors.append("{}: {}".format(trip.symbol, str(e)))
            except Exception as e:
                list_of_errors.append("{}: {}".format(trip.symbol, str(e)))

        if len(list_of_errors) > 0:
            raise Exception(
                "The list of trips has errors: {}".format(list_of_errors))
        else:
            print('the offer will be published...')


trips = [
    Trip('IT-VNC', 'Italy-Venice', dt.date(2023, 6, 1), dt.date(2023, 6, 12)),
    Trip('SP-BRC', '', dt.date(2023, 6, 12), dt.date(2023, 5, 22)),
    Trip('IT-ROM', 'Italy-Rome', dt.date(2023, 6, 21), dt.date(2023, 6, 12))
]

try:
    print('Publishing trips...')
    Trip.publish_offer(trips)
    print('... done')
except TripException as e:
    print('THERE ARE ERRORS')
    print(e)
    print('THE OFFER CANNOT BE PUBLISHED')
