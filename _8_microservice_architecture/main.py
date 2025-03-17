import requests
import json

def main():
    # create user

    # Set the URL for creating a user
    url = "http://127.0.0.1:5001/register"

    # Prepare the data for the user
    user_data = {
        "username": "John Doe"
    }

    # Send a POST request with the data as JSON
    response = requests.post(url, json=user_data)

    # Print the response from the server
    print(response.json())  # Response body

    # create order
    # Set the URL for creating an order
    url = "http://127.0.0.1:5002/orders"

    # Prepare the data for the order
    order_data = {
        "user_id": 1,
        "product_id": '123',
        "quantity": 2
    }

    # Send a POST request with the data as JSON
    response = requests.post(url, json=order_data)

    # Print the response from the server
    print(response.json())  # Response body

    # check product inventory
    # Set the URL for checking the inventory
    url = "http://127.0.0.1:5003/inventory/check"

    # Prepare the data to check the inventory
    inventory_data = {
        "product_id": '123',
        "quantity": 2
    }

    # Send a POST request with the data as JSON
    response = requests.post(url, json=inventory_data)

    # Print the response from the server
    print(response.json())  # Response body


if __name__ == '__main__':
    main()