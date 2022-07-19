"ファイルの読み込み・書き込みを行うためのクラスライブラリ"
import csv

"csvファイルの読み込みと出力を行うためのクラス"
class CsvFile:
    def __init__(self, filename):
        self.filename = filename

    def read(self, row_num):
        f = open(self.filename)
        reader = csv.reader(f)
        csv_list = [row for row in reader]
        f.close()
        return csv_list[row_num][0]

    def output(self, name, mode, row):
        f = open(name, mode, encoding='utf-8', newline='')
        writer = csv.writer(f)
        writer.writerow(row)
        f.close()
