import xlwt
import xlrd
from patient import Patient
def compute(best):
    sign=[]
    judge=0
    for i in range(5):
        if best[i]<=99:
            sign.append(1)
        else:
            sign.append(0)
    for i in range(5):
        judge+=(5-i)*sign[i]
    if judge>=8:
        lable=1
    else:
        lable=0
    return lable
sjxl=xlrd.open_workbook('sjxl.xlsx')
sjcs=xlrd.open_workbook('sjcs.xlsx')
sjxlsheet=sjxl.sheet_by_index(0)
sjcssheet=sjcs.sheet_by_index(0)
f=xlwt.Workbook()
sheet=f.add_sheet(u'sheet1',cell_overwrite_ok=True)
for i in range(92):
    patientdata1=Patient(sjcssheet.col_values(i))
    ssds=[]
    for j in range(200):
        patientdata2=Patient(sjxlsheet.col_values(j))
        ssds.append(patientdata1.compare(patientdata2))
    best5=sorted(ssds)[0:5]
    best5i=[]
    for k in range(5):
        best5i.append(ssds.index(best5[k]))
    lable=compute(best5i)
    print(best5i)
    sheet.write(i,0,lable)
f.save('gongjingyu0.xlsx')
    
            
