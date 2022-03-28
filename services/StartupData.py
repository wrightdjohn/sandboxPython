from services.Domain import Person
from services.Domain import Address
from services.Domain import ContactPoint
from services.Domain import ContactPointType
import copy


def make_address(address, addressee):
    new_addr = copy.copy(address)
    new_addr.addressee = addressee
    return new_addr

def copy_person(person):
    return copy.deepcopy(person)


class StartupData:
    def __init__(self):
        self.main_office = Address("","716 Elm Street","Apt 201","Monroeville","Va","55551","United States")
        self.nyc_office = Address("","1616 38th Avenue","Apt 201","New York","NY","40404","United States")

        self.admin = Person("6220f65C8f03315fb10b327c","Administrator","admin", [], [])

        self.joe_black = Person("6220fc388c70850875b5af0a", "Joseph R. Black","x121212",
                          [ContactPoint(ContactPointType.PHONE,"616-555-1212",True)],
                          [make_address(self.main_office,"Joe Black")])

        self.jim_borman = Person("6220f65C8f03315fb10b327c", "James L. Borman", "x131313",
                           [ContactPoint(ContactPointType.PHONE,"616-555-2282",True)],
                           [make_address(self.main_office, "Jim Borman")])

        self.jessica_wilde = Person("6220fc388c70850875b5af0c", "Jessica Wilde", "x232323",
                            [ContactPoint(ContactPointType.PHONE,"616-555-3452",True)],
                            [make_address(self.main_office, "Jessica Wilde")])

        self.martin_lake = Person("6220fc388c70850875b5af0d", "Martin Lake", "y100121",
                               [ContactPoint(ContactPointType.PHONE,"716-555-4112",True)],
                               [make_address(self.nyc_office, "Martin Lake")])

        self.virginia_o_toole = Person("6220fc388c70850875b5af0e", "Virginia O'Toole", "y221134",
                             [ContactPoint(ContactPointType.PHONE,"716-555-4422",True)],
                             [make_address(self.nyc_office, "Ginni O'Toole")])

        self.preeta_smith = Person("6220fc388c70850875b5af0f", "Preeta Smith", "y323554",
                             [ContactPoint(ContactPointType.PHONE,"716-555-4422",True),
                              ContactPoint(ContactPointType.EMAIL,"preeta.smith@bigbiz.com", True)],
                             [make_address(self.main_office, "Preeta Smith"), make_address(self.nyc_office, "Preeta Smith")])

        def person_list():
            return [self.admin,self.joe_black,self.jim_borman,self.jessica_wilde,self.martin_lake,self.virginiaOToole,self.preetaSmith]


startupData = StartupData()


def startup_data():
    return startupData
