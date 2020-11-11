import csv

rows=list()
record=dict()

fields=['ID', 'Action']

with open('synciq.txt') as f:
    lines = f.read().splitlines()

    for line in lines:

        # new record, save to list
        if line[0] == "-":
            # write it out?
            rows.append(record)
            record=dict()

            continue

        l = line.split(":")
        if l[0].strip() in fields:
            record[l[0].strip()] = l[1].strip()

    rows.append(record)


# print(rows)
# # print(list(d.keys()))
# # for k in d.keys():
# #     print(k, type(k))
# fields = list(d.keys())
# cleprint(fields[0])

with open('mycsvfile.csv', 'w', newline='') as f:  # Just use 'w' mode in 3.x
 
    w = csv.DictWriter(f, fieldnames=rows[0].keys() )
    w.writeheader()

    for r in rows:
        w.writerow(r)
