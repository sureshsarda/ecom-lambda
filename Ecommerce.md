# ecom-lambda
A sample REST API for Ecom site using Lambda and DynamoDB

## Sample Item

```json
{
    "address": "India",
    "imageURL": "https://example.com/image.png",
    "id": "1",
    "lastModified": "2023-04-01 03:32:13.889317",
    "productName": "Another book"
}

```

## End Points

Domain: `https://dloddoqiie.execute-api.us-east-1.amazonaws.com/default`

### Get all items

```http request
GET /cart/
```

### Insert an item

```http request
POST /cart/

{
    "productName": "Sapiens 2.0",
    "imageURL": "https://example.com",
    "address": "India"
}
```

### Get a single item

```http request
GET /cart/{itemId}
```


### Delete a single item

```http request
DELETE /cart/{itemId}
```

### Update/Overwrite an item

```http request
PUT /cart/{itemId}

{
    "productName": "Sapiens 2.0",
    "imageURL": "https://example.com",
    "address": "Bangalore, India"
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
GET https://dloddoqiie.execute-api.us-east-1.amazonaws.com/default/cart/

{
    "status": "success",
    "data": [
        {
            "imageURL": "https://example.com",
            "address": "Bangalore, India",
            "id": "8e3ce002-a9dc-4549-b43e-13987497197f",
            "lastModified": "2023-04-01 04:54:39.977765",
            "productName": "Sapiens"
        }
    ]
}
```