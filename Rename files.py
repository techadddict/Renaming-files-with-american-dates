import re,os,shutil
#regex for the date formats
european=re.compile('[0-3]+[0-9]+-([0][1-9]+|[1][0-2]+)-[0-9]+')
american=re.compile('([0][1-9]+|[1][0-2]+)-([0-3]+[0-9]+)-([0-9]+)')
os.mkdir('path')

os.chdir('path')
for i in range(1,13):
    for j in range(0,32):
        if (i < 10 and j < 10):
            file =open('File '+'0'+str(i)+ '-'+ '0'+str(j)+ '-'+'2019'+'.txt','w')
            file.write('working'+str(i)+ str(j))
        elif (i < 10 and j >= 10):
            file =open('File '+'0'+str(i)+ '-'+str(j)+ '-'+'2019'+'.txt','w')
            file.write('working'+str(i)+ str(j))
        elif (i>9 and j < 10):
            file =open('File '+str(i)+ '-'+ '0'+str(j)+ '-'+'2019'+'.txt','w')
            file.write('working'+str(i)+ str(j))
        else:
            file =open('File '+str(i)+ '-'+str(j)+ '-'+'2019'+'.txt','w')
            file.write('working'+str(i)+ str(j))

    file.close()



"""

american
MM-DD-YYYY
01-22-2009
12-05-2006
09-13-2005


european
DD-MM-YYYY
01-12-2009
12-06-2006
25-11-2005


Program searches all the file names in the current working directory for American-style dates.
When one is found, it renames the file with the month and day swapped to make it European-style.

"""

os.mkdir('path')

american_bool=False
for filename in os.listdir('path'):
    try:
        reg_check=american.findall(filename)
        if(int(reg_check[0][1])>12):
             american_bool=True
             if True:
                month= reg_check[0][0]
                date= reg_check[0][1]
                year=reg_check[0][2]
                new_name=re.sub('-'.join(list(reg_check[0])), date+'-'+month+'-'+year,filename)
                shutil.move('path'+filename, 'path/Renamed/'+new_name)
    except Exception as e:
        continue


