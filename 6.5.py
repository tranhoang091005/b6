print("TRẦN DANH HOÀNG")
print("MSSV:235752021610064")

class StringReverser:
    def __init__(self, input_string):
        self.input_string = input_string  # Lưu trữ chuỗi đầu vào
    
    def reverse_words(self):
        # Tách chuỗi thành các từ, sau đó đảo ngược thứ tự các từ
        words = self.input_string.split()  # Tách chuỗi theo khoảng trắng thành các từ
        reversed_words = words[::-1]  # Đảo ngược danh sách các từ
        return ' '.join(reversed_words)  # Kết hợp các từ lại thành chuỗi mới

# Ví dụ sử dụng class để đảo ngược chuỗi
if __name__ == "__main__":
    # Dữ liệu đầu vào
    input_string = 'hello .py'
    
    # Tạo đối tượng của lớp StringReverser
    reverser = StringReverser(input_string)
    
    # Gọi phương thức reverse_words để đảo ngược chuỗi
    result = reverser.reverse_words()
    
    # In kết quả ra
    print(f"Dữ liệu vào: {input_string}")
    print(f"Đầu ra: {result}")
