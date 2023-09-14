from abc import ABC, abstractmethod

class Car(ABC):
    def __init__(self, last_service_date): # __init__ is known as a constructor and is called when a new object of a class is  created. Allows you to inlitalize attributes of an object So any car that is added or chosen with the class Car will have the varaibels listed
        self.last_service_date = last_service_date   # sets the current last service data for the self to the one identified in the varaibles

    @abstractmethod # way of creating special permissions or an area to place special permissions without defining them but making sure that they are used in the code lateron
    def needs_service(self):
        pass

