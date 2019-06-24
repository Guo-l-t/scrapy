import csv
from xlrd import open_workbook
from xlutils.copy import copy
import xlwt
import os


def csvToexcle(filename, count, content):
    wb = xlwt.Workbook(encoding='utf-8')  # 设置编码格式
    ws = wb .add_sheet('Sheet1')  # 添加sheet表

    style = xlwt.XFStyle()  # 初始化样式
    font = xlwt.Font()  # 为样式创建字体
    font.name = ''
    # font.bold = True # 黑体
    # font.underline = True 下划线
    # font.italic = True # 斜体字
    style.font = font  # 设定样式
    # for i in range(10):
    #     for j in range(5):
    #         # 参数对应 行, 列, 值 self.excel_w.save('Excelw.xls')
    #         excel_w_sheet.write(i, 0, label='admin%d%d' % (i, j))
    ws.write(0, 0, "idfa")
    ex_count = 1
    for i in content:
        ws.write(ex_count, 0, i)
        ex_count = ex_count+1
        if ex_count > 60000:
            break
    wb.save(filename+'_'+str(count)+'.xls')


if __name__ == '__main__':
    filename = 'xiaoyi_idfa_ios.csv'
    csv_file = csv.reader(open(filename, 'r'))
    # 可以先输出看一下该文件是什么样的类型
    print(csv_file)
    # 用来存储整个文件的数据，存成一个列表，列表的每一个元素又是一个列表，表示的是文件的某一行
    content = []
    for line in csv_file:
        # 打印文件每一行的信息
        content.append(line)
    count = (len(content)//60000)+1
    print(count)
    for i in range(count):
        csvToexcle(filename, i, content)