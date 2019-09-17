# filter strings by extension
import codecs

def get_string(file_name, extension):

    f = codecs.open(file_name, "r", "utf-8")
    strings = f.readlines()
    f.close()

    filtered_strings = []
    for st in strings:
        st = st[1:-2]
        ext = st.split(".")[-1]
        if ext == extension:
            filtered_strings.append(st)
    
    return filtered_strings

if __name__ == "__main__":

    import sys

    f = codecs.open(f"{sys.argv[2]}_strings.txt", "w+", "utf-8")
    strings = get_string(sys.argv[1], sys.argv[2])

    for st in strings:
        f.write(f"{st}\n")

    f.close()

