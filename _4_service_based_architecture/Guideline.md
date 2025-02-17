In , an application is composed of discrete, independent  that provide specific functionalities. These services communicate with each other via well-defined . This architecture is very popular in modern cloud-native applications, especially in -based architectures, where each service is typically small, focused on a specific domain, and can be developed, deployed, and scaled independently.

* Each service is a distinct unit responsible for specific business functionality. Each service can be independently deployed, managed, and scaled.
* : Services interact with each other using  or  communication methods like HTTP/REST, gRPC, or messaging queues.
* : Services are loosely coupled, meaning one service does not directly depend on the internal logic of another service. They interact through well-defined interfaces.
* : Since services are isolated, you can scale each service independently based on load.
* : Each service owns its own data, and communication between services typically happens through APIs (REST, gRPC, etc.).


For the lab session, let’s implement a  where:
* Handles user-related operations (e.g., registration, login).
* Handles product-related operations (e.g., adding products, viewing products).
* A Gateway Service that interacts with other services (users and products).
We'll use  to build RESTful APIs for each service and simulate the communication between the services.


The  will handle user registration and login.
* /register (POST) – Registers a new user.
* /login (POST) – Authenticates a user based on credentials.
The  will handle product-related operations like adding and viewing products.
* /add_product (POST) – Adds a new product.
* /get_products (GET) – Returns all products.
The  will act as the main entry point that interacts with the  and .
 routes incoming requests to the appropriate service (User or Product) by making HTTP requests to the other services.
* Handles user registration and login. 
Runs on localhost:5001.
* :Handles product management (adding and viewing products).Runs on localhost:5002.4.3 
* :The  serves as the entry point to the system.It routes requests to either the  or  depending on the action being requested.Runs on localhost:5000.

5. How to Run the Services:
* : Install Flask (if not already installed) via:pip install flask
* Step 2: Save each of the services (User, Product, and Gateway) into separate Python files (user_service.py, product_service.py, gateway_service.py).
* Step 3: Run the services:
  * First, start the `python user_service.py`
  * Next, start the `python product_service.py`
  * Finally, start the `python gateway_service.py`
  * Test the services by sending HTTP requests to the .

Use tools like  or  to test the services. (POST request to http://localhost:5000/register_user):
```
{
"username": "john_doe",
"password": "1234"
}
```
 (POST request to http://localhost:5000/login_user):
```
{
"username": "john_doe",
"password": "1234"
}
```
 (POST request to http://localhost:5000/add_product):
```
{
"product_id": "1",
"product_name": "Laptop"
}
```
 (GET request to http://localhost:5000/get_products): This will return the list of products stored in the .


In this lab, we built a  using Flask to simulate a basic system with three services:: Manages user-related operations.: Manages product-related operations.: Acts as a central entry point to interact with the other services.

This setup demonstrates how services can be independently developed, deployed, and scaled while communicating over APIs.