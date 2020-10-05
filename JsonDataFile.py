import json
import os
import inspect

class db():
    def __init__(self, FileName):
        """
        :param FileName: Variable for json file name that is to be created.
        """
        self.FileName = FileName
        self.BaseFolder = 'C:/Students_Records'

        """
        Inspecting live object to find out the python file name where the object is being created.
        input is : E:\PythonTest\CallerFile.py
        """
        self.Directory = str(inspect.stack()[1][1].split("\\")[-1].split(".")[0])

        self.path = os.path.join(self.BaseFolder, self.Directory)
        os.makedirs(self.path, exist_ok = True)
        self.FileName_Abs = os.path.join(self.path, self.FileName)

    def write_json(self, DataDict):
        """
        :param DataDict: Student's data in dictionary format
        :return: None
        """
        if os.path.exists(self.FileName_Abs):
            f = open(self.FileName_Abs,)
            data = json.load(f)
            data.update(DataDict)
            f.close
        else:
            with open(self.FileName_Abs, "w") as outfile:
                json.dump(DataDict, outfile)

    def read_json(self, DataElement):
        """
        :param DataElement: Key in the dictionary of student data fetched from json file.
        :return: Value of the relevent key passed by the used in student data dictionary.
        """
        if os.path.exists(self.FileName_Abs):
            f = open(self.FileName_Abs,)
            data = json.load(f)
            f.close
            return data[str(DataElement)]
        else:
            print("Data not present for requested candidate.")



