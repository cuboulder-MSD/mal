# mal

This repository contains code for transforming MAL metadata into the MARC21 schema for import into the Library Catalog. You will need .csv files from the MAL to run these. 

python 2 is required

```python [python code] [csv]```

How to import into Sierra:

1) Open Data Exchange in Sierra
2) Change Select Process dropdown to: Load records via locally-created load profiles.
3) Select Get PC (upper right) and navigate to the appropriate directory and select the MARC file you created – make sure the file has the extension “.dat”
4) Click Upload.
5) In the Rename File dialog box, choose the “.lfts” extension, and click OK.
6) Highlight your file (hint: sort the Last Modified column to find the most recent files).
7) Click Prep.
8) Click Start (at bottom). The number of input/output records should match the number of records in your DAT file.
9) Click Close.
10) Make sure Select Process still says Load records via locally-created load profiles.
11) Highlight the file you just created/prepped – it ends with the extension “lmarc”
12) Click Load.
13) Choose “d” Outsourced.
14) Click Test if desired. Otherwise, click Load.
