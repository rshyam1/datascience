import pandas as pd
import re
data3=pd.read_csv('diabetic_data.csv',header=0,parse_dates=True)
#print data3
insulin_no=0
insulin_yes=0
pri_diabetic_adm=0
pri_diabetic_adm_not=0
age_0_10=0
age_10_20=0
age_20_30=0
age_30_40=0
age_40_50=0
age_50_60=0
age_60_70=0
age_70_80=0
age_80_90=0
age_90_100=0
for i in data3.index:
    if(data3.iloc[i]['readmitted'] != 'NO' and data3.iloc[i]['insulin'] == 'No'):
        insulin_no = insulin_no + 1
    elif(data3.iloc[i]['readmitted'] != 'NO' and data3.iloc[i]['insulin'] != 'No'):
        insulin_yes = insulin_yes + 1
        
    if (re.search('250',data3.iloc[i]['diag_1'])):
        
        if(data3.iloc[i]['readmitted'] != 'NO'):
         # primary diagomsis is diabetic and patient is admitted
            pri_diabetic_adm = pri_diabetic_adm + 1
            if (re.search('0-10',data3.iloc[i]['age'])):
                age_0_10 +=1
            if (re.search('10-20',data3.iloc[i]['age'])):
                age_10_20 +=1
            if (re.search('20-30',data3.iloc[i]['age'])):
                age_20_30 +=1
            if (re.search('30-40',data3.iloc[i]['age'])):
                age_30_40 +=1
            if (re.search('40-50',data3.iloc[i]['age'])):
                age_40_50 +=1
            if (re.search('50-60',data3.iloc[i]['age'])):
                age_50_60 +=1    
            if (re.search('60-70',data3.iloc[i]['age'])):
                age_60_70 +=1
            if (re.search('70-80',data3.iloc[i]['age'])):
                age_70_80+=1
            if (re.search('80-90',data3.iloc[i]['age'])):
                age_80_90+=1
            if (re.search('90-100',data3.iloc[i]['age'])):
                age_90_100+=1
        else:
            pri_diabetic_adm_not = pri_diabetic_adm_not + 1
            
         
print "Total readmitted Pt having no insulin",insulin_no
print "Total redadmitted Pt having  insulin",insulin_yes
print "Primary diabetic patient admitted ", pri_diabetic_adm
print "Primary diabetic patient not admitted ", pri_diabetic_adm_not
print "Primary diabetic patient admitted  age group 0-10",age_0_10
print "Primary diabetic patient admitted  age group 10-20",age_10_20
print "Primary diabetic patient admitted  age group 20-30",age_20_30
print "Primary diabetic patient admitted  age group 30-40",age_30_40
print "Primary diabetic patient admitted  age group 40-50",age_40_50
print "Primary diabetic patient admitted  age group 50-10",age_50_60
print "Primary diabetic patient admitted  age group 60-70",age_60_70
print "Primary diabetic patient admitted  age group 70-80",age_70_80
print "Primary diabetic patient admitted  age group 80-90",age_80_90
print "Primary diabetic patient admitted  age group 90-100",age_90_100


