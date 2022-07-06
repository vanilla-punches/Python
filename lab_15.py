import pickle
for i in range(1,6):
    with open(str(i) + "weekly_report.txt", "w") as report_file:
        report_file.write("- {0} weekly report -" .format(i))
        report_file.write("\n Department :")
        report_file.write("\n Name :")
        report_file.write("\n Summary :")
