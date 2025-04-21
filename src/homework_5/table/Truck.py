from homework_5.table.Table import Table
from homework_5.table.JournalTable import JournalTable
from homework_5.table.DinnerTable import DinnerTable

class Truck:
    __maxMass = 0
    __tables = []
    __current_load_mass = 0

    def __init__(self, max_mass):
        self.__maxMass = max_mass

    def add_table(self, table):
        if self.__maxMass - self.__current_load_mass >= table.get_mass():
            self.__current_load_mass += table.get_mass()
            self.__tables.append(table)
            print(table, "has been loaded")
            print("The truck is loaded with", self.__current_load_mass, "of", self.__maxMass, "\n")
        else:
            print(table, "can not be loaded\n")

truck = Truck(50)

table1 = Table(10)
table2 = Table(12)
table3 = DinnerTable(15)
table4 = DinnerTable(20)
table5 = JournalTable(8)
table6 = JournalTable(7)

truck.add_table(table1)
truck.add_table(table2)
truck.add_table(table3)
truck.add_table(table4)
truck.add_table(table5)
truck.add_table(table6)
