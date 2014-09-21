import csv

with open("/Users/vabraham24/Documents/Data/samples/test_sample_60K.csv","rb") as fp_in:
    rdr = csv.reader(fp_in)
    with open("/Users/vabraham24/Documents/Data/samples/result_test60.csv","wb") as fp_out:
        wtr = csv.writer(fp_out)
        for r in rdr:
            wtr.writerow((r[0], r[5], r[16], r[17], r[20], r[23], r[24], r[26], r[29], r[34], r[37]))
