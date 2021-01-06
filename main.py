import csv
import xlsxwriter

workbook = xlsxwriter.Workbook('output.xlsx')
worksheet = workbook.add_worksheet()

with open('supercarrosdata2.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        print(row)
        worksheet.write(line_count,0, row[1])
        worksheet.write(line_count,1, row[2])
        worksheet.write(line_count,2, row[3])
        line_count+=1

    #     if line_count == 0:
    #         print(f'Column names are {", ".join(row)}')
    #         line_count += 1
    #     else:
    #         print(f'\t{row[1]} works in the {row[2]} department, and was born in {row[3]}.')
    #         line_count += 1
    # print(f'Processed {line_count} lines.')

workbook.close()