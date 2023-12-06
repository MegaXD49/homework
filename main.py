# กำหนดรายการสินค้า
products = [
    {"name": "หมูสับกิโล", "price": 150.0},
    {"name": "เนื้ออกไก่", "price": 105.0},
    {"name": "ไก่บ้าน(ตัว)", "price": 120.0},
    {"name": "มาม่าตัมยํา", "price": 6.50},
    {"name": "ข้าวสาร", "price": 150.0},
    {"name": "น้ำตาล", "price": 20.0},
    {"name": "ปลากระป๋องสามแม่ครัว", "price": 10.0},
    {"name": "ซอสน้ำมันหอย", "price": 18.0},
    {"name": "ผงชูรส", "price": 10.25},
    {"name": "ไข่แผงคละเบอร์", "price": 120.25},
    {"name": "ชาเขียว", "price": 21.50},
    {"name": "Pepsi", "price": 29.50},
    {"name": "กาแฟ", "price": 15.75},
    {"name": "ขนมปังอบเนย", "price": 19.0},
    {"name": "ชาไทย", "price": 11.50},
    {"name": "น้ำเปล่า", "price": 15.15},
    {"name": "น้ำแข็ง", "price": 10.0}
]

#สร้างฟังก์ชั่นเพื่อคำนวณเงินทอน
def calculate_change(products, amount_paid):
    total_price = sum(product["price"] for product in products)
    change = amount_paid - total_price
    return change, total_price


# 15 รายการที่เลือกซื้อ
selected_products = []

# แสดงรายการสินค้า
print("รายการสินค้า: ")
for i, product in enumerate(products, start=1):
    print(f"{i}. {product['name']}: {product['price']:.2f} บาท")

# เลือกรายการสินค้า 15 รายการ
max_selected_items = 17
min_selected_items = 15
selected_item_count = 0
selected_indices = set()

while selected_item_count < max_selected_items:
    while True:
        try:
            choice = int(input("กรุณาเลือกสินค้าที่ต้องการอย่างน้อย 15 รายการจากด้านบน โดยพิมพ์ตัวเลขหน้ารายการลงในนี้ (ห้ามเลือกซ้ำ และถ้าหากต้องการหยุดกรุณาพิมพ์ '0' เมื่อเลือกครบตั้งแต่ 15 อย่างขึ้นไป): "))
            break
        except ValueError:
            print("\nกรุณาป้อนเป็นตัวเลข\n")

    if choice == 0 and selected_item_count >= min_selected_items:
        break
    elif choice == 0 and selected_item_count < min_selected_items:
        print("\nกรุณาเลือกให้ครบ 15 รายการก่อนชำระเงิน")
        continue

    if 1 <= choice <= len(products) and choice not in selected_indices:
        selected_products.append(products[choice - 1])
        selected_indices.add(choice)
        selected_item_count += 1
    elif choice in selected_indices:
        print("\nคุณเลือกรายการนี้ไปแล้ว กรุณาเลือกรายการใหม่")
    else:
        print("\nไม่มีเลขที่เลือกนี้ กรุณาเลือกใหม่")

    # แสดงผลเมื่อเลือกครบ 15 รายการแล้ว
    if min_selected_items <= selected_item_count < max_selected_items:
        print(f"\nคุณได้เลือก {selected_item_count} รายการแล้ว สามารถชำระเงินได้ทันทีโดยพิมพ์ 0 ในครั้งถัดไป")
    if selected_item_count == max_selected_items:
        print("\nคุณได้เลือกครบทุกรายการที่มีแล้ว กรุณาชำระเงิน\n")

    # แสดงยอดเงินที่ต้องชำระ
    total_price = sum(product["price"] for product in selected_products)
    print(f"\nยอดรวมราคาสินค้า: {total_price:.2f} บาท\n")

# รับยอดเงินที่ใช้จากผู้ใช้
while True:
    try:
        amount_paid = float(input("ป้อนยอดเงินที่ชำระ: "))
        break
    except ValueError:
        print("กรุณาป้อนเป็นตัวเลข")

# คำนวณเงินทอนและยอดเงินที่ใช้
change, _ = calculate_change(selected_products, amount_paid)

# แสดงผลลัพธ์
print("\nรายการสินค้าที่ซื้อ:")
for product in selected_products:
    print(f"{product['name']}: {product['price']:.2f} บาท")

print(f"\nยอดเงินที่ชำระ: {amount_paid:.2f} บาท")
print(f"ราคารวมของสินค้า: {total_price:.2f} บาท")
print(f"เงินทอน: {change:.2f} บาท\nขอบคุณที่ใช้บริการครับ")
