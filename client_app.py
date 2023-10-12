import requests
import json
from concurrent.futures import ThreadPoolExecutor

from conf import *


def json_data_receiver():
    print('Create new request:')
    while True:
        command_type = input('Enter command type (os/compute):')
        if command_type in ['os', 'compute']:
            break
    command_name = input('Enter command name:')
    parameters_str = input('Enter parameters (separate them with comma):')
    parameters = parameters_str.split(",")
    print(f'Command type: {parameters}')

    json_data = {
        'command_type': command_type,
        'command_name': command_name,
        'parameters': parameters
    }

    json_str = json.dumps(json_data, ensure_ascii=False)
    print("Created json:", json_str, '\n---------------------------------------------')
    return json_data


def send_request(json_data):
    url = f'{SERVER_ADDRESS}:{SERVER_PORT}'
    response = requests.post(url, json=json_data)
    return response.json()


def main():
    print('Request sender client app started')
    while True:
        json_data = json_data_receiver()
        with ThreadPoolExecutor(max_workers=5) as executor:
            future = executor.submit(send_request, json_data)
            response = future.result()
            print(response)


if __name__== '__main__':
    main()