import requests

# ดึงคีย์จาก URL
r = requests.get("https://raw.githubusercontent.com/KONgghik/python/main/key.txt")
key = r.text.strip()  # เอาอักษรว่างที่อาจมีอยู่ด้วย

# รับคีย์จากผู้ใช้
user_input = input("key: ")

# เปรียบเทียบคีย์
if user_input == key:
    print("คีย์ถูกต้อง")
else:
    print("คีย์ไม่ถูกต้อง")
    exit()

print("ตัวนี้ขั้นทดลองรออัพเดท")
