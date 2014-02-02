# -*- coding: utf-8 -*-
import csv


with open('./variants_custom.csv') as files:
    csv_files = list(csv.reader(files))

with open('./variants.csv') as files:
    csv_files.extend(list(csv.reader(files)))

address = '台北市大安區金華街187號東樓204室'

for a, b in csv_files:
    address = address.replace(a, b)

print address
