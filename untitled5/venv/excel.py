import xlrd

def get_data(file_name):
    # create an empty list to store rows
    rows = []
    # open the specified Excel spreadsheet as workbook
    book = xlrd.open_workbook(file_name)
    # get the first sheet
    sheet = book.sheet_by_index(0)
    # iterate through the sheet and get data from rows in list
    # for row_idx in range(1, sheet.nrows):
    #     rows.append(list(sheet.row_values(row_idx, 0, sheet.ncols)))
    #     return rows

    for row_idx in range(sheet.nrows):
        rows.append(sheet.row_values(row_idx))

    return rows

if __name__=="__main__":
    print(get_data("D:\\Users\\Administrator\\PycharmProjects\\untitled\\venv\\userinfo.xlsx"))