import csv, time, sys
from pymarc import Record, Field
from datetime import datetime

# ts = time.time()
# st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d')

with open(sys.argv[1], 'rU', errors='ignore') as csvFile:
    reader = csv.DictReader(csvFile)
    for row in reader:
        title = row['Name']
        medium = row['Secondary Type']
        product = row['Product Name']
        manufacturer = row['Manufacturer']
        model = row['Model']
        year = row['Year']
        extConn = row['External Connections']
        intConn = row['Internal Connections']
        operatingSys = row['Operating System']
        accessionNo = row['Accession Number']
        print(title)

        record = Record()
        record.add_field(
            Field(
                tag = '245',
                indicators = ['0','0'],
                subfields = [
                    'a', title + ' ' + model
                ]))
        # record.add_field(
        #     Field(
        #         tag = '246',
        #         indicators = ['0','1'],
        #         subfields = [
        #             'a', product + ' ' + model
        #
        #         ]))
        record.add_field(
            Field(
                tag = '264',
                indicators = ['#','3'],
                subfields = [
                    'b', manufacturer,
                    'c', year
                ]))
        record.add_field(
            Field(
                tag = '500',
                indicators = ['#','#'],
                subfields = [
                    'a', 'Accession Number:' + accessionNo
                ]))
        record.add_field(
            Field(
                tag = '516',
                indicators = ['#'],
                subfields = [
                    'a', medium
                ]))
        record.add_field(
            Field(
                tag = '793',
                subfields = [
                    'a', 'Media Archeology Lab (Basement, 1320 Grandview Ave. Boulder CO 80302.)'
                ]))
        # record.add_field(
        #     Field(
        #         tag = '520',
        #         indicators = ['#'],
        #         subfields = [
        #             'a', operatingSys + '.' + extConn + '.' + intConn + '.'
        #         ]))
        print(record)
        # with open('malMARC'+str(st)+'.dat', 'wb') as out:
        #
        #     out.write(record.as_marc())
