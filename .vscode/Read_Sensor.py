from ast import While
import time
import ir
import oled
import RED

#this script will be the script that runs the reading and filtering of data.


threshold = 10000
last_peak_time = 0
last_was_above = False

def peak_detection(ir_value):
    global last_peak_time, last_was_above
    is_above = ir_value > threshold
    now = time.ticks_ms()
    time_since_last_peak = time.ticks_diff(now, last_peak_time)

    peak_detected = False

    if is_above and not last_was_above:
        if time_since_last_peak > 600:
        peak_detected = True
        last_peak_time = now
        
    last_was_above = is_above
    return peak_detected

def calculate_bpm(current_peak_time, last_peak_time):
    interval.ms = time.ticks_diff(current_peak_time, last_peak_time)
    if interval_ms <= 0:
        return 0
    
    bpm = 60000 / interval_ms
    return int(bpm)