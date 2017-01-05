import numpy
class Patient:
    def __init__(self,value):
        self.data=value
    def compare(self,patient2):
        ssd=0
        for i in range(len(patient2)):
            if abs(self.data[i]-patient2.data[i])<150:
                pass
            else:
                ssd+=(self.data[i]-patient2.data[i])**2
        return ssd
    def compare2(self,patient2):
        m=0
        mos=0
        mop2=0
        for i in range(len(patient2)):
            m+=self.data[i]*patient2.data[i]
        for i in range(len(self)):
            mos+=self.data[i]**2
        for i in range(len(patient2)):
            mop2+=patient2.data[i]**2
        mos=numpy.sqrt(mos)
        mop2=numpy.sqrt(mop2)
        ratio=m/mos/mop2
        return ratio
    def __len__(self):
        return len(self.data)
            
