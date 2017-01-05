import xlwt
import xlrd
from patient import Patient
def compute(best):
    sign=[]
    judge=0
    for i in range(7):
        if best[i]<=99:
            sign.append(1)
        else:
            sign.append(0)
    for i in range(7):
        judge+=(7-i)*sign[i]
    if judge>=10:
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
        ssds.append(patientdata1.compare2(patientdata2))
    best7=sorted(ssds,cmp=None,key=None,reverse=True)[0:7]
    best7i=[]
    for k in range(7):
        best7i.append(ssds.index(best7[k]))
    lable=compute(best7i)
    print(best7i)
    sheet.write(i,0,lable)
f.save('gongjingyu1.xlsx')
