import time

timestamp = time.strftime("%H:%M:%S")
print(timestamp)

timestamp = time.strftime("%H")
print(f'Hour : {timestamp}')

timestamp = time.strftime("%M")
print(f'Minutes : {timestamp}')

timestamp = time.strftime("%S")
print(f'Seconds : {timestamp}')