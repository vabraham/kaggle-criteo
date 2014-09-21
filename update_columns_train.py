import csv

with open("/Users/vabraham24/Documents/Data/samples/train.csv","rb") as fp_in:
    rdr = csv.reader(fp_in)
    with open("/Users/vabraham24/Documents/Data/samples/result_train.csv","wb") as fp_out:
        wtr = csv.writer(fp_out)
        for r in rdr:
            wtr.writerow((r[0], r[1], r[6], r[17], r[18], r[21], r[24], r[25], r[27], r[28], r[35], r[38]))
