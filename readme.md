#  Product and Order Management API – HROne Task

This is a simple FastAPI project that allows users to:
- ✅ Create and list products
- ✅ Place orders with multiple items
- ✅ Retrieve orders by user ID

It uses **MongoDB Atlas** as the backend database.

---

##  Tech Stack

- **FastAPI** – for building APIs
- **MongoDB Atlas** – cloud database
- **PyMongo** – MongoDB client for Python
- **Uvicorn** – ASGI server
- **Pydantic** – for schema validation

---

## Setup Instructions

### 1. Clone the repo and navigate:

```bash
git clone <your-repo-link>
cd hrone_task

2. Create a virtual environment:
python -m venv venv
venv\Scripts\activate

3. Install dependencies:
pip install -r requirements.txt

4. Add .env file with MongoDB URI:
    Add your MongoDB URI

Run the Server
uvicorn main:app --reload
Visit http://127.0.0.1:8000/docs to test all endpoints via Swagger UI.

API Endpoints
Create a product
{
  "name": "T-Shirt",
  "description": "White cotton round neck",
  "price": 499,
  "sizes": ["S", "M", "L"]
}

GET /products
Returns all products.

POST /orders
Place an order:
{
  "user_id": "chirag123",
  "items": [
    {
      "product_id": "PRODUCT_OBJECT_ID",
      "quantity": 2
    }
  ]
}

GET /orders/{user_id}
Returns all orders for the given user.
