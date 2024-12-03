print("TRẦN DANH HOÀNG")
print("MSSV:235752021610064")

class RomanToInteger:
    def __init__(self):
        # Bảng ánh xạ các ký tự La Mã sang giá trị số nguyên
        self.roman_map = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
    
    def roman_to_int(self, roman):
        # Hàm chuyển đổi từ số La Mã sang số nguyên
        total = 0  # Tổng kết quả
        prev_value = 0  # Giá trị của ký tự trước đó
        
        # Duyệt qua các ký tự trong chuỗi La Mã từ phải sang trái
        for char in reversed(roman):
            current_value = self.roman_map[char]  # Lấy giá trị của ký tự hiện tại
            
            # Nếu giá trị hiện tại nhỏ hơn giá trị trước đó, ta trừ đi
            if current_value < prev_value:
                total -= current_value
            else:
                total += current_value
            
            # Cập nhật giá trị trước đó
            prev_value = current_value
        
        return total

# Ví dụ sử dụng class để chuyển đổi số La Mã
if __name__ == "__main__":
    roman_converter = RomanToInteger()
    
    # Nhập số La Mã từ người dùng
    roman_number = input("Nhập số La Mã: ").upper()
    
    # Chuyển đổi và hiển thị kết quả
    result = roman_converter.roman_to_int(roman_number)
    print(f"Số nguyên tương ứng là: {result}")
