import Student
import JsonDataFile

class BEStudent (Student.MyStudent):
    def __init__(self, student_name):
        self.name = student_name
        self.jdf = JsonDataFile.db(self.name)

    def Set_FamilyBackground(self, data_dict):
        self.jdf.write_json(data_dict)

    def Get_FamilyBackground(self, param):
        return self.jdf.read_json(param)

    def Set_Qualification(self, data_dict):
        self.jdf.write_json(data_dict)

    def Get_Qualification(self, param):
        return self.jdf.read_json(param)

    def Set_Report(self, data_dict):
        self.jdf.write_json(data_dict)

    def Get_Marks(self, sem, subject):
        return self.jdf.read_json(sem)[subject]

    def Get_Report(self, sem):
        return self.jdf.read_json(sem)

    def Get_Total(self, sem, total):
        return self.jdf.read_json(sem)[total]

    def Get_Percentage(self, sem, percent):
        return self.jdf.read_json(sem)[percent]

    #def Get_Class(self, sem, grade):
    #    return self.jdf.read_json(sem)[grade]