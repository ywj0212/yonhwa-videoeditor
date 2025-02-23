import re, sys, os

def is_valid_time_str(time_str):
    pattern = r'^(\d+:[0-5]?\d|\d{1,2})$'
    return bool(re.match(pattern, time_str))

def time_str_to_seconds(time_str):
    if ':' in time_str:
        # 분:초 형식일 경우 분과 초로 분리
        minutes, seconds = map(int, time_str.split(':'))
        return minutes * 60 + seconds
    else:
        # 초 단독 형식일 경우
        return int(time_str)
    
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except AttributeError:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)
