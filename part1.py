# part1.py

# เก็บรายการสินค้า
product_list = []

def add_product(product_list):
    name = input("ป้อนชื่อสินค้า: ").strip()

    # ตรวจว่ามีสินค้านี้อยู่แล้วหรือไม่
    for product in product_list:
        if product["name"].lower() == name.lower():
            while True:
                try:
                    quantity = int(input("ป้อนจำนวนที่จะเพิ่ม: "))
                    break
                except ValueError:
                    print("❌ กรุณาใส่ตัวเลข")
            product["quantity"] += quantity
            print(f"🔄 อัปเดตสินค้า '{name}' เป็น {product['quantity']} ชิ้นแล้ว\n")
            return

    # ถ้าเป็นสินค้าใหม่
    while True:
        try:
            quantity = int(input("ป้อนจำนวนสินค้า: "))
            break
        except ValueError:
            print("❌ กรุณาใส่ตัวเลข")
    product_list.append({"name": name, "quantity": quantity})
    print(f"✅ เพิ่มสินค้า '{name}' จำนวน {quantity} ชิ้นแล้ว\n")

def show_products(product_list):
    if not product_list:
        print("⚠️ ไม่มีสินค้าที่จะแสดง\n")
        return
    print("📦 รายการสินค้า:")
    for i, product in enumerate(product_list, start=1):
        print(f"{i}. {product['name']} - {product['quantity']} units")
    print()

# --- เริ่มโปรแกรม ---
while True:
    print("===== เมนูจัดการสินค้า =====")
    print("1. เพิ่ม/อัปเดตสินค้า")
    print("2. แสดงรายการสินค้า")
    print("3. ออกจากโปรแกรม")
    choice = input("เลือกเมนู (1-3): ").strip()

    if choice == "1":
        add_product(product_list)
    elif choice == "2":
        show_products(product_list)
    elif choice == "3":
        print("👋 ออกจากโปรแกรม")
        break
    else:
        print("❌ เลือกเมนูไม่ถูกต้อง\n")