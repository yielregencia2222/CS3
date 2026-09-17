class Lab:
    def __init__(self,room_number):
        self.room_number = room_number
class Technician:
    assign_lab = None
    def __init__(self,assign_lab):
        self.assign_lab = assign_lab
    def assigned_lab(self,lab_obj):
        self.lab_obj = lab_obj
        
chem_lab = Lab("302")
mr_cruz = Technician("Mr Cruz")
mr_cruz.assigned_lab(chem_lab)
print(mr_cruz.lab_obj.room_number)