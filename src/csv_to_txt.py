import csv
import codecs

def get_proper_strings(csv_file):
    strings = []
    with open(csv_file, newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for row in spamreader:
            strings.append(', '.join(row))

    for idx, s in enumerate(strings):
        strings[idx] = s[1:-1]
    
    return strings


if __name__ == "__main__":

    import sys

    strs = get_proper_strings(sys.argv[1])
    f = codecs.open(f"cw_demo/{sys.argv[1][:-4]}.txt", "w+", "utf-8")
    for s in strs:
        f.write(f"{s}\n")
    f.close()
