import csv
import codecs

def get_proper_strings(csv_file):
    strings = []
    with open(csv_file, newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for row in spamreader:
            strings.append(', '.join(row))

    for idx, s in enumerate(strings):
        strings[idx] = s[:-5]
    
    return strings


if __name__ == "__main__":

    strs = get_proper_strings("ghidra_string_exports(cw_demo).csv")

    f = codecs.open("cw_strings.txt", "w+", "utf-8")
    for s in strs:
        f.write(f"{s}\n")
    f.close()
