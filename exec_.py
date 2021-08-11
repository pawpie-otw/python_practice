from datetime import datetime


def generate_func(span='m'):
    div = 60 if span == 'm' else 60**2 if span == 'h' else 60**3 if span == "d" else 1
    code = f"""
def time_span(start, end):
    duration = end - start
    duration_in_s = duration.total_seconds()
    return divmod(duration_in_s, {div})[0]
    """
    exec(code, globals())
    return time_span


start = datetime(2019, 1, 1, 0, 0, 0)
end = datetime.now()
time_span_m, time_span_h, time_span_d = generate_func(
), generate_func('h'), generate_func('d')
print(time_span_m(start, end))
print(time_span_h(start, end))
print(time_span_d(start, end))
