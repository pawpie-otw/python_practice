import datetime as dt


class Trip:
    def __init__(self, symbol, title, start, end):
        self.symbol = symbol
        self.title = title
        self.start = start
        self.end = end

    def check_data(self):
        assert len(self.title) > 0, "Title must be longer than 0"
        assert self.start < self.end, "Start date is later than end date!"

    @staticmethod
    def publish_offer(tour_list):
        list_of_errors = []

        for tour in tour_list:
            try:
                tour.check_data()
            except ValueError as e:
                print(f"ValueError: <{tour.symbol}>: <{e}>")
                list_of_errors.append(f"<{tour.symbol}>: <{e}>")
            except Exception as e:
                print(f"Exception: <{tour.symbol}>: <{e}>")
                list_of_errors.append(f"<{tour.symbol}>: <{e}>")
            else:
                print("the offer will be published")


trips = [
    Trip('IT-VNC', 'Italy-Venice', dt.date(2023, 6, 1), dt.date(2023, 6, 12)),
    Trip('SP-BRC', 'Spain-Barcelona', dt.date(2023, 6, 12), dt.date(2023, 5, 22)),
    Trip('IT-ROM', 'Italy-Rome', dt.date(2023, 6, 21), dt.date(2023, 6, 12))]

try:
    print("następuje sprawdzanie wycieczek...")
    Trip.publish_offer(trips)
except Exception:
    print("to jebło!!!!")
finally:
    print("done!")
