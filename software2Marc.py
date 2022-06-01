import csv, time, sys
from pymarc import Record, Field
import datetime

# ts = time.time()
# st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d')

with open(sys.argv[1], 'rU', encoding='latin-1') as csvFile, open('mal_software.dat', 'wb') as outfile:
    reader = csv.DictReader(csvFile)
    for row in reader:
        title = row['Name']
        medium = row['Medium']
        product = row['Product Name']
        manufacturer = row['Manufacturer']
        model = row['Model']
        year = row['Year']
        extConn = row['External Connections']
        intConn = row['Internal Connections']
        operatingSys = row['Operating System']
        accessionNo = row['Accession Number']


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
                    'f', manufacturer,
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
                indicators = ['#','#'],
                subfields = [
                    'a', medium
                ]))
        record.add_field(
            Field(
                tag = '793',
                indicators = ["#","#"],
                subfields = [
                    'a', 'Media Archeology Lab (Basement, 1320 Grandview Ave. Boulder CO 80302.)'
                ]))
        record.add_field(
            Field(
                tag = '956',
                indicators = ["#","#"],
                subfields = [
                    'a', 'malcu'
                ]))
        # record.add_field(
        #     Field(
        #         tag = '520',
        #         indicators = ['#'],
        #         subfields = [
        #             'a', operatingSys + '.' + extConn + '.' + intConn + '.'
        #         ]))

        outfile.write(record.as_marc())
