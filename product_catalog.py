# product_catalog.py

# Mock product catalog
products = [ 
    {"name": "Eco Water Bottle", "tags": ["eco-friendly", "durable", "recyclable"]}, 
    {"name": "Trail Backpack", "tags": ["durable", "water-resistant", "lightweight"]}, 
    {"name": "Vegan Leather Wallet", "tags": ["vegan", "stylish", "compact"]}, 
    {"name": "Bamboo Toothbrush", "tags": ["eco-friendly", "vegan", "biodegradable"]}, 
    {"name": "Smartwatch", "tags": ["tech", "durable", "stylish"]},
    {"name": "Solar Charger", "tags": ["eco-friendly", "tech", "portable"]},
    {"name": "Minimalist Desk Lamp", "tags": ["stylish", "compact", "tech"]},
    {"name": "Reusable Grocery Bag", "tags": ["eco-friendly", "durable", "lightweight"]}
]

# Collect customer preferences
customer_preferences = []
while True:
    pref = input("Input a preference:\n").strip().lower()
    if pref:
        customer_preferences.append(pref)
    cont = input("Do you want to add another preference? (Y/N): ").strip().upper()
    if cont != "Y":
        break

# Convert preferences to a set
preference_set = set(customer_preferences)

# Convert product tags to sets
for product in products:
    product["tags"] = set(product["tags"])

# Count matching tags
def count_matches(product_tags, preference_set):
    return len(product_tags & preference_set)

# Recommend products
def recommend_products(products, preference_set):
    recommendations = []
    for product in products:
        matches = count_matches(product["tags"], preference_set)
        if matches > 0:
            recommendations.append((product["name"], matches))
    recommendations.sort(key=lambda x: x[1], reverse=True)
    return recommendations

# Print results
print("\nRecommended Products:")
for name, score in recommend_products(products, preference_set):
    print(f"- {name} ({score} match(es))")

# ---------------- DESIGN MEMO ----------------
"""
Design Memo:

This recommendation tool uses core operations like set intersections and loops to efficiently match customer preferences with product tags. 
Sets are ideal here because they automatically remove duplicates and allow fast comparison using the intersection operator (&). 
Each product’s tags are converted to a set, and the customer’s preferences are also stored as a set. 
We then loop through each product, count the number of matching tags, and return a sorted list of products with at least one match.
If the product catalog scaled to 1,000+ items, the current approach would still perform well due to the efficiency of set operations. 
However, for even larger datasets or real-time performance, we might consider indexing tags using a dictionary or implementing inverted indices to reduce the number of comparisons. 
Additionally, we could cache frequent queries or use a database with tag-based filtering.
This prototype emphasizes clarity and simplicity while laying the groundwork for scalable logic. 
It’s a great example of how thoughtful data structure selection—sets over lists—can make a big difference in performance and readability.
"""
