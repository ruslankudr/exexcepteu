import re

def is_valid_verilog_number(s):
    pattern = r'^(\+?\d+(\.\d+)?([eE][+-]?\d+)?)$'
    return bool(re.match(pattern, s))
