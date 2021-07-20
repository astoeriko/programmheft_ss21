import sys

infile1 = sys.argv[1]
infile2 = sys.argv[2]
outfile = sys.argv[3]

with open(infile1) as infile1:
    with open(infile2) as infile2:
        with open(outfile, "w") as outfile:
            for line1, line2 in zip(infile1, infile2):
                line1 = line1.strip()
                line2 = line2.strip()
                if not line1:
                    assert not line2
                    outfile.write("\\versespace\n")
                else:
                    outfile.write(f"\\textvers{{{line1}}}{{{line2}}}\n")

