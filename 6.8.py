print("TRẦN DANH HOÀNG")
print("MSSV:235752021610064")

class ATM:
    def __init__(self):
        self.balance = 10000  # Khởi tạo số dư tài khoản, ví dụ 10,000
        self.pin = "1234"  # Mã PIN mặc định

    def authenticate(self):
        # Xác thực mã PIN
        attempts = 3  # Số lần thử tối đa
        while attempts > 0:
            entered_pin = input("Nhập mã PIN của bạn: ")
            if entered_pin == self.pin:
                print("Mã PIN hợp lệ.")
                return True
            else:
                attempts -= 1
                print(f"Mã PIN sai. Bạn còn {attempts} lần thử.")
        print("Quá số lần thử. Thử lại sau.")
        return False

    def check_balance(self):
        # Kiểm tra số dư tài khoản
        print(f"Số dư tài khoản của bạn là: {self.balance} VND")

    def withdraw(self):
        # Rút tiền
        amount = float(input("Nhập số tiền bạn muốn rút: "))
        if amount <= self.balance:
            self.balance -= amount
            print(f"Bạn đã rút {amount} VND. Số dư còn lại là: {self.balance} VND.")
        else:
            print("Số dư không đủ để thực hiện giao dịch này.")

    def deposit(self):
        # Gửi tiền
        amount = float(input("Nhập số tiền bạn muốn gửi: "))
        self.balance += amount
        print(f"Bạn đã gửi {amount} VND. Số dư hiện tại là: {self.balance} VND.")

    def start(self):
        # Hàm chính để bắt đầu giao dịch ATM
        if not self.authenticate():
            return  # Nếu xác thực thất bại, thoát chương trình
        
        while True:
            print("\nChọn một chức năng:")
            print("1. Kiểm tra số dư")
            print("2. Rút tiền")
            print("3. Gửi tiền")
            print("4. Thoát")
            
            choice = input("Nhập lựa chọn của bạn: ")
            
            if choice == '1':
                self.check_balance()
            elif choice == '2':
                self.withdraw()
            elif choice == '3':
                self.deposit()
            elif choice == '4':
                print("Cảm ơn bạn đã sử dụng dịch vụ ATM. Hẹn gặp lại!")
                break
            else:
                print("Lựa chọn không hợp lệ. Vui lòng thử lại.")

# Chạy chương trình ATM
if __name__ == "__main__":
    atm = ATM()
    atm.start()
