import uuid

class Product:
    def __init__(self, name, description, price, online_shop):
        self.name = name
        self.description = description
        self.price = price
        self.online_shop = online_shop

class Customer:
    def __init__(self, name, email, address):
        self.name = name
        self.email = email
        self.address = address
        self.cart = []
        self.past_orders = []

class OnlineShop:
    def __init__(self, name, url):
        self.name = name
        self.url = url
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def show_products(self):
        if not self.products:
            print("ยังไม่มีสินค้าในร้าน")
            return
        print("\nสินค้าที่มีในร้าน:")
        for i, p in enumerate(self.products, 1):
            print(f"{i}. {p.name} - {p.price} บาท - {p.description}")

    def addingItemsToCart(self, customer, product_index, quantity):
        if product_index < 1 or product_index > len(self.products):
            print("เลือกสินค้าผิดพลาด")
            return
        product = self.products[product_index - 1]
        customer.cart.append((product, quantity))
        print(f"เพิ่ม {product.name} จำนวน {quantity} ชิ้น ลงในตะกร้าของ {customer.name}")

    def checkOut(self, customer):
        if not customer.cart:
            print("ตะกร้าว่าง ไม่สามารถชำระเงินได้")
            return
        total_price = sum(p.price * qty for p, qty in customer.cart)
        order_id = str(uuid.uuid4())[:8]

        order = {
            "order_id": order_id,
            "items": [(p.name, qty, p.price) for p, qty in customer.cart],
            "total_price": total_price
        }
        customer.past_orders.append(order)
        customer.cart.clear()

        print(f"\nชำระเงินสำเร็จ! รหัสคำสั่งซื้อ: {order_id}")
        print(f"ยอดรวม: {total_price:.2f} บาท")

    def orderTracking(self, customer, order_id):
        for order in customer.past_orders:
            if order["order_id"] == order_id:
                print(f"\nรายละเอียดคำสั่งซื้อ {order_id}:")
                for name, qty, price in order["items"]:
                    print(f"- {name} x {qty} = {price*qty:.2f} บาท")
                print(f"ยอดรวม: {order['total_price']:.2f} บาท")
                return
        print("ไม่พบคำสั่งซื้อที่ระบุ")

def main():
    print("=== สร้างร้านค้าออนไลน์ ===")
    shop_name = input("ชื่อร้านค้า: ")
    shop_url = input("URL ร้านค้า: ")
    shop = OnlineShop(shop_name, shop_url)

    # สร้างลูกค้า
    print("\n=== สร้างบัญชีลูกค้า ===")
    cust_name = input("ชื่อ-นามสกุล: ")
    cust_email = input("อีเมล: ")
    cust_address = input("ที่อยู่: ")
    customer = Customer(cust_name, cust_email, cust_address)

    while True:
        print("\n--- เมนู ---")
        print("1. เพิ่มสินค้าในร้าน")
        print("2. แสดงสินค้าทั้งหมด")
        print("3. เลือกสินค้าลงตะกร้า")
        print("4. ดูตะกร้าสินค้า")
        print("5. ชำระเงิน")
        print("6. ตรวจสอบคำสั่งซื้อ")
        print("7. ออกจากโปรแกรม")

        choice = input("เลือกเมนู: ")

        if choice == "1":
            name = input("ชื่อสินค้า: ")
            desc = input("คำอธิบายสินค้า: ")
            while True:
                try:
                    price = float(input("ราคาสินค้า: "))
                    break
                except:
                    print("กรุณาใส่ราคาที่ถูกต้อง")
            product = Product(name, desc, price, shop)
            shop.add_product(product)
            print("เพิ่มสินค้าเรียบร้อย")
        elif choice == "2":
            shop.show_products()
        elif choice == "3":
            if not shop.products:
                print("ยังไม่มีสินค้าในร้าน")
                continue
            shop.show_products()
            try:
                idx = int(input("เลือกสินค้าด้วยเลขที่: "))
                qty = int(input("จำนวน: "))
                if qty <= 0:
                    print("จำนวนต้องมากกว่า 0")
                    continue
                shop.addingItemsToCart(customer, idx, qty)
            except:
                print("กรุณาใส่ตัวเลขให้ถูกต้อง")
        elif choice == "4":
            if not customer.cart:
                print("ตะกร้าว่าง")
            else:
                print("\nสินค้าที่อยู่ในตะกร้า:")
                for p, q in customer.cart:
                    print(f"- {p.name} x {q} = {p.price * q} บาท")
        elif choice == "5":
            shop.checkOut(customer)
        elif choice == "6":
            order_id = input("ใส่รหัสคำสั่งซื้อ: ")
            shop.orderTracking(customer, order_id)
        elif choice == "7":
            print("ขอบคุณที่ใช้บริการ")
            break
        else:
            print("เลือกเมนูไม่ถูกต้อง")

if __name__ == "__main__":
    main()
