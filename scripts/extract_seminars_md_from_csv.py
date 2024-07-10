import pandas as pd
import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument(
    "filename",
    help="CSV file containing the information")
parser.add_argument(
    "--outdir", "-o",
    help="directory in which to write the md files")
args = parser.parse_args()

filename = args.filename
outdir = args.outdir

seminars = pd.read_csv(filename)
seminars = seminars.loc[~seminars["series"].isna()]
seminars = seminars.loc[seminars["type"].isin(["BCM", "BIGRE"])]
seminars = seminars[
    ["series", "when", "where", "time", "speaker", "affiliation", "title",
    "type"]]

seminars["title"] = seminars["title"].fillna("TBD")
seminars["speaker"] = seminars["speaker"].fillna("TBD")

if outdir is not None:
    os.makedirs(outdir, exist_ok=True)

for _, seminar in seminars.iterrows():
    outname = os.path.join(
        outdir, "".join(seminar["when"].split("/")[::-1]) + ".md")
    with open(outname, "w") as f:
        f.write("---\n")
        f.write("title: \"%s\"\n" % seminar["title"])
        f.write("speaker: \"%s\"\n" % seminar["speaker"])
        if isinstance(seminar["affiliation"], str):
            f.write("affiliation: \"%s\"\n" % seminar["affiliation"])
        f.write("series: \"%s\"\n" % seminar["series"])
        f.write("when: \"%s - %s\"\n" % (seminar["when"], seminar["time"]))
        f.write("type: bigre\n")
        f.write("where: \"%s\"\n" % (seminar["where"]))
        f.write("---\n")
