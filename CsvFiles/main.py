import csv
import xlsxwriter

workbook = xlsxwriter.Workbook('output.xlsx')
worksheet = workbook.add_worksheet()

# workbook_two = xlsxwriter.Workbook('output2.xlsx')
# worksheet_two = workbook_two.add_worksheet()

with open('supercarrosdata_v2.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    line_count_two = 0

    top_car = {}
    top_car_viewers = {}
    url_car = {}

    # first part "sacar top de vehiculos en base a cantidad de super carros"
    for row in csv_reader:
        if top_car.get(row[2]) == None:
            top_car[row[2]] = 1
            url_car[row[2]] = row[18] 
        else:
            top_car[row[2]] +=1                         

    for key in top_car:   
        worksheet.write(line_count,0, key)
        worksheet.write(line_count,1, top_car[key])
        worksheet.write(line_count,2,url_car[key] )
        line_count+=1
    
    workbook.close()
    # second part "sacar top de vehiculos en base a cantidad de visitas"
    # for row in csv_reader:
    #     if row[19] == 'vehicleViews':
    #         continue
        
    #     if top_car_viewers.get(row[2]) == None:
    #         top_car_viewers[row[2]] = int(row[19])
    #         url_car[row[2]] = row[18]
    #     else:
    #         top_car_viewers[row[2]] += int(row[19])                         

    # for key in top_car_viewers:   
    #     worksheet_two.write(line_count_two,0, key)
    #     worksheet_two.write(line_count_two,1, top_car_viewers[key])
    #     worksheet_two.write(line_count_two,2, url_car[key])
    #     line_count_two+=1
    
    # workbook_two.close()

