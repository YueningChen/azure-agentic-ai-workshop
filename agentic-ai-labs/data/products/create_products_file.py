import pandas as pd

# Create sample product data
products_data = {
    'Product Name': [
        'Laptop Pro 15"',
        'Wireless Mouse',
        'Mechanical Keyboard',
        'USB-C Hub',
        'External Monitor 24"',
        'Webcam HD',
        'Desk Lamp LED',
        'Office Chair',
        'Smartphone Case',
        'Bluetooth Headphones',
        'Tablet 10"',
        'Power Bank',
        'Cable Organizer',
        'Desk Pad',
        'Standing Desk Converter'
    ],
    'Category': [
        'Electronics',
        'Electronics',
        'Electronics',
        'Electronics',
        'Electronics',
        'Electronics',
        'Office',
        'Office',
        'Electronics',
        'Electronics',
        'Electronics',
        'Electronics',
        'Office',
        'Office',
        'Office'
    ],
    'Price': [
        1299.99,
        29.99,
        89.99,
        49.99,
        299.99,
        79.99,
        39.99,
        249.99,
        19.99,
        149.99,
        399.99,
        39.99,
        15.99,
        25.99,
        189.99
    ],
    'Stock Quantity': [
        25,
        150,
        75,
        100,
        40,
        60,
        80,
        30,
        200,
        45,
        35,
        120,
        95,
        70,
        20
    ],
    'Supplier': [
        'TechCorp',
        'AccessoryPlus',
        'TechCorp',
        'AccessoryPlus',
        'DisplayTech',
        'TechCorp',
        'OfficePro',
        'OfficePro',
        'AccessoryPlus',
        'AudioMax',
        'TechCorp',
        'AccessoryPlus',
        'OfficePro',
        'OfficePro',
        'OfficePro'
    ],
    'Rating': [
        4.8,
        4.2,
        4.6,
        4.3,
        4.7,
        4.1,
        4.4,
        4.5,
        4.0,
        4.6,
        4.5,
        4.2,
        4.0,
        4.3,
        4.4
    ]
}

# Create DataFrame
df = pd.DataFrame(products_data)

# Save to Excel file
df.to_excel('products.xlsx', index=False, sheet_name='Products')

print("✅ Created products.xlsx file successfully!")
print(f"📊 File contains {len(df)} products")
print(f"💰 Average price: ${df['Price'].mean():.2f}")
print(f"📦 Total stock: {df['Stock Quantity'].sum()} items")
print("\nFirst 5 products:")
print(df.head().to_string(index=False))
