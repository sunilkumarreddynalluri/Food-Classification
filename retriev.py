import redis
import json

# Connect Redis
r = redis.Redis(
    host='127.0.0.1',
    port=6379,
    decode_responses=True
)

# Food name to retrieve
food_name = "pizza"

# Get data from Redis
data = r.get(food_name)

# Check if exists
if data is None:
    print("Food not found")

else:
    nutrition = json.loads(data)

    print("Food Name:", food_name)
    print("Nutrition Data:")
    print(nutrition)