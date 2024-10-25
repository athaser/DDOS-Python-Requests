import requests
import concurrent.futures
import time

# URL to send requests to
url = "https://url.com"

# Function to make a request
def make_request(attempt):
    try:
        response = requests.get(url)
        print(f"Request {attempt + 1}: Status Code {response.status_code}")
    except Exception as e:
        print(f"Request {attempt + 1}: Failed - {str(e)}")

# Start the timer to measure time
start_time = time.time()

# Use ThreadPoolExecutor for multithreading
with concurrent.futures.ThreadPoolExecutor(max_workers=50) as executor:
    # Submit 200 requests in parallel
    futures = [executor.submit(make_request, i) for i in range(210)]

    # Ensure all futures are completed
    concurrent.futures.wait(futures)

# End the timer and print the duration
end_time = time.time()
print(f"Total time taken: {end_time - start_time} seconds")
