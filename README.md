# Discount API

First install the requirements for the project from preferably in a virtual environment by

```
pip install -r src/requirements-dev.txt
```

The main file for running the microservice is called lambda.py, to run the program simply run this file

```
python3 src/lambda.py
```

Now navigate to the following local url in order to test the endpoints, or use postman.

```
http://127.0.0.1:5000/swagger/
```

To save time and simplify the process of testing the code, the database is hardcoded and the data is not persisted after the application is closed. 

There are two hardcoded records available for testing purposes. Otherwise just generate couple of discounts using the POST end-point.

The first discountId is not claimed and can be claimed using any UUID for customerId. 

The second discountId is already claimed and it should be unavailable. 
```
8557f1ad-4c8f-4822-ab4c-c30338289574
3fa85f64-5717-4562-b3fc-2c963f66afa6
```

For generating discounts using the POST method use the brandId and fill the body according the shown schema in swagger.

Here is an example to generate 100 discounts for our black friday sale:


```
brandId = 9bed8d1d-ad80-48d4-9314-1aaa7509f615
```

```
{
  "validFromTime": "2021-11-26T00:00:00.882Z",
  "discountName": "BF",
  "expirationDate": "2021-11-27T00:00:00.882Z",
  "numberOfDiscounts": 100
}
```

