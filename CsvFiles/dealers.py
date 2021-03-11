import csv
import xlsxwriter

workbook = xlsxwriter.Workbook('dealers.xlsx')
worksheet = workbook.add_worksheet()

with open('dealers.csv', encoding='utf8') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    years = { }
    makes = { }
    models = { }

    for row in csv_reader:
        arr = row[1].split(' ')
        x = len(arr)
        years[row[0]] = arr[x-1]
        if(row[2] == 'bmw'):
                makes[row[0]] = 'BMW'
        else:
            makes[row[0]] = row[2].capitalize()
        row[1] = row[1].replace(years[row[0]], "")
        row[1] =  row[1].replace(makes[row[0]], "")
        models[row[0]] = row[1]

    for key in years: 
        worksheet.write(line_count,0, key)
        worksheet.write(line_count,1, makes[key])
        worksheet.write(line_count,2, models[key])
        worksheet.write(line_count,3, years[key])
        line_count+=1
    
    workbook.close()


