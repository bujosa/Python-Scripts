import csv
import xlsxwriter

workbook = xlsxwriter.Workbook('output.xlsx')
worksheet = workbook.add_worksheet()

with open('supercarrosdata.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0

    top_car = {}
    # first part "sacar top de vehiculos en base a cantidad de super carros"
    for row in csv_reader:
        top_car[row] += 1
        
    for key in top_car:   
        print(row)
        worksheet.write(line_count,0, key)
        worksheet.write(line_count,1, top_car[key])
        line_count+=1

workbook.close()