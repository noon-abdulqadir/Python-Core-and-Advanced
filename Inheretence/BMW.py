class BMW:

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def start(self):
        print("Starting the car.")

    def stop(self):
        print("Stopping the car.")


class ThreeSeries(BMW):  # inherit

    def __init__(self, CruiseControlEnabled, make, model, year):  # or def __init__(self,CruiseControlEnabled,*args,**kwargs)
        #BMW.__init__(self, make, model, year)
        super().__init__(make, model, year)  # or super(ThreeSeries, self).__init__(*args,**kwargs)
        self.CruiseControlEnabled = CruiseControlEnabled

    def display(self):
        print(self.CruiseControlEnabled)

    def start(self):
        super().start()
        print("Button Start.")


class FiveSeries(BMW):  # inherit

    def __init__(self, ParkingAssistEnabled, make, model, year):
        BMW.__init__(self, make, model, year)
        #super().__init__(make, model, year)
        self.ParkingAssistEnabled = ParkingAssistEnabled


threeSeries = ThreeSeries(True, "BMW", "328i", 2018)
print(threeSeries.CruiseControlEnabled)
print(threeSeries.make)
print(threeSeries.model)
print(threeSeries.year)

threeSeries.start()
threeSeries.stop()
threeSeries.display()

fiveSeries = FiveSeries(True, "BMW", "328i", 2018)
