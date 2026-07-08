import csv

def export_builders(builders, filename):
    with open(filename, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Builder Name"])
        for builder in builders:
            writer.writerow([builder])
