def _timestamp(timestamps):
    minutes, seconds, milliseconds = map(int, timestamps.split(':'))
    time_in_seconds = minutes * 60 + seconds + milliseconds / 1000
    return time_in_seconds