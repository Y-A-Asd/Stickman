

def runtime(starttime, endtime, time_in_seconds):
    if end := endtime:
        pass
    else:
        end = time_in_seconds
    return starttime - end
