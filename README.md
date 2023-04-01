# ecom-lambda
A sample REST API for Ecom site using Lambda and DynamoDB

## Sample Item

```json
{
    "quantity": "120",
    "imageURL": "https://example.com/image.png",
    "id": "1",
    "lastModified": "2023-04-01 03:32:13.889317",
    "productName": "Another book"
}

```

## End Points

Domain: `xi3mxeszjj.execute-api.us-east-1.amazonaws.com/default`

### Get all items

```http request
GET /items/
```

### Insert an item

```http request
POST /items/

{
    "productName": "Sapiens 2.0",
    "imageURL": "https://example.com",
    "quantity": 10
}
```

### Get a single item

```http request
GET /items/{itemId}
```


### Delete a single item

```http request
DELETE /items/{itemId}
```

### Update/Overwrite an item

```http request
PUT /items/{itemId}

{
    "productName": "Sapiens 2.0",
    "imageURL": "https://example.com",
    "quantity": 10
}
```

## Response

### Success Response Format
Failure response will have status code of 200
```json
{
  "status": "success",
  "data": "object or array"
}

```

### Failure Response Format
Failure response will have status code of 400
```json
{
  "status": "failure",
  "error": "error message"
}
```

## Example

Get all items:
```http request
GET https://xi3mxeszjj.execute-api.us-east-1.amazonaws.com/default/items

{
    "status": "success",
    "data": [
        {
            "quantity": "120",
            "imageURL": "https://example.com/image.png",
            "id": "1",
            "lastModified": "2023-04-01 03:32:13.889317",
            "productName": "Another book"
        },
        {
            "quantity": "10",
            "imageURL": "https://example.com",
            "id": "c51b957e-7969-44fe-95ff-093ba41f5c18",
            "lastModified": "2023-04-01 03:34:13.085055",
            "productName": "Sapiens 2.0"
        },
        {
            "quantity": "10",
            "imageURL": "https://example.com",
            "id": "cb9aebbb-9a43-4c85-8191-d07629ad5d2e",
            "lastModified": "2023-04-01 03:32:58.739367",
            "productName": "Sapiens 2.0"
        }
    ]
}
```