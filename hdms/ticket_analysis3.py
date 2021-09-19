import pandas as pd
from dateutil.parser import parse


def timediff(t1, t2):
    print("Ticket Close Time: ",t2)
    print("Ticket Open Time: ",t1)
    tdiff = t2- t1
    print(tdiff)
    tdiff_sec = tdiff.total_seconds()
    print(tdiff_sec)
    tdiff_min = tdiff_sec / 60
    tdiff_hr = tdiff_min / 60
    tdiff_day = int(tdiff_hr / 24)
    tdiff_sec = int(tdiff_sec % 60)
    tdiff_min = int(tdiff_min % 60)
    tdiff_hr = int(tdiff_hr % 24)
    if tdiff_day > 0:
        print("Days: %d Hours: %d Minutes: %d Seconds: %d" % (tdiff_day, tdiff_hr, tdiff_min, tdiff_sec))
    elif tdiff_hr > 0:
        print("Hours: %d Minutes: %d Seconds: %d" % (tdiff_hr, tdiff_min, tdiff_sec))
    elif tdiff_min > 0:
        print("Minutes: %d Seconds: %d" % (tdiff_min, tdiff_sec))
    else:
        print("Seconds: %d" % tdiff_sec)
    tdiff = t2 - t1
    tdiff_sec = tdiff.total_seconds()
    return tdiff_sec


if __name__ == '__main__':
    tkt_data = pd.read_csv("C:/Users/Linux/PycharmProjects/hdms/datasets/finale.csv")
    row, column = tkt_data.shape
    col_names = list(tkt_data.columns)
    print(col_names)
    case_id = list(tkt_data[col_names[0]])
    unique_case_id = list(tkt_data[col_names[0]].unique())
    k = 0
    tdiff = []
    for i in range(5):
        topen = parse(str(tkt_data[col_names[3]][k]))
        k += (case_id.count(unique_case_id[i])-1)
        print("Unique Case Id: ",unique_case_id[i])
        print("Unique Case ID Count: ",case_id.count(unique_case_id[i]))
        print("Current Case ID: ",case_id[k])
        print("Next Case ID: ",case_id[k+1])
        tclose = parse(str(tkt_data[col_names[3]][k]))
        tdiff.append(timediff(topen,tclose))
        k += 1
    print("\n",tdiff)
    avg_time = 0
    for i in range(len(tdiff)):
        avg_time += tdiff[i]
    avg_time /= len(tdiff)
    print("\nAverage Time per Ticket: %d seconds" % (avg_time%60))
    avg_time /= 60
    print("Average Time per Ticket: %d minutes" % (avg_time%60))
    avg_time /= 60
    print("Average Time per Ticket: %d hours" % (avg_time%60))
    avg_time /= 24
    print("Average Time per Ticket: %d days" % avg_time)
    print("\nsuccess")
