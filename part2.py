# part2.py

class Product:
    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity


class Store:
    def __init__(self):
        self.__products = []  # private attribute

    def add_product(self, name, quantity):
        # ถ้ามีสินค้าอยู่แล้ว จะอัปเดตจำนวน
        for product in self.__products:
            if product.name.lower() == name.lower():
                product.quantity += quantity
                print(f"🔄 อัปเดต '{name}' เป็น {product.quantity} ชิ้นแล้ว\n")
                return

        # ถ้าเป็นสินค้าใหม่
        new_product = Product(name, quantity)
        self.__products.append(new_product)
        print(f"✅ เพิ่มสินค้า '{name}' จำนวน {quantity} ชิ้นแล้ว\n")

    def show_products(self):
        if not self.__products:
            print("⚠️ ไม่มีสินค้าที่จะแสดง\n")
            return
        print("📦 รายการสินค้า:")
        for i, product in enumerate(self.__products, start=1):
            print(f"{i}. {product.name} - {product.quantity} units")
        print()


# --- ตัวอย่างการใช้งาน ---
if __name__ == "__main__":
    my_store = Store()

    while True:
        print("===== เมนูจัดการสินค้า (OOP) =====")
        print("1. เพิ่ม/อัปเดตสินค้า")
        print("2. แสดงรายการสินค้า")
        print("3. ออกจากโปรแกรม")
        choice = input("เลือกเมนู (1-3): ").strip()

        if choice == "1":
            name = input("ป้อนชื่อสินค้า: ").strip()
            while True:
                try:
                    quantity = int(input("ป้อนจำนวนสินค้า: "))
                    break
                except ValueError:
                    print("❌ กรุณาใส่ตัวเลข")
            my_store.add_product(name, quantity)

        elif choice == "2":
            my_store.show_products()

        elif choice == "3":
            print("👋 ออกจากโปรแกรม")
            break
        else:
            print("❌ เลือกเมนูไม่ถูกต้อง\n")