from abc import ABC
import JsonDataFile

class MyStudent(ABC):

    def __init__(self, StudentName):
        self.Name = StudentName

    def Set_FamilyBackground(self,FName,MName,Age,Gen):
        pass

    def Get_FamilyBackground(self, Param):
        pass

    def Set_Qualification(self, DName, Sem):
        pass

    def Get_Qualification(self, Param):
        pass

    def Set_Report(self, Subject, Marks):
        pass

    def Get_Marks(self, Sem, Subject):
        pass

    def Get_Report(self, Sem):
        pass

    def Get_Total(self, Sem):
        pass

    def Get_Percentage(self, Sem):
        pass

    def Get_Class(self, Sem):
        pass


