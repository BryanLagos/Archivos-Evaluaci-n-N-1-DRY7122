import json
import time

file_path = '/home/devasc/labs/devnet-src/parsing/myfile.json'

with open(file_path) as file:
    data = json.load(file)
    token_value = data['access_token']
    expires_in = data['expires_in']
    current_time = int(time.time())
    expires_at = current_time + expires_in
    time_left = expires_at - current_time

print(f"Token value: {token_value}")
print(f"Time left (seconds): {time_left}")

