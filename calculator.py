import math

# Định nghĩa một số hàm cho logarit và mũ
def eval_safe(expression):
    # Tạo một môi trường an toàn với các hàm được phép sử dụng
    safe_dict = {
        'log': math.log,  # log cơ số e
        'log10': math.log10,  # log cơ số 10
        'pow': math.pow,  # hàm lũy thừa
        'sqrt': math.sqrt,  # hàm căn bậc hai
        'exp': math.exp,  # hàm mũ e^x
        'pi': math.pi,  # hằng số pi
        'e': math.e  # hằng số e
    }
    
    # Tính toán chuỗi đầu vào trong môi trường an toàn
    return eval(expression, {"__builtins__": None}, safe_dict)

# Chuỗi phép tính chứa logarit và mũ
expression = input("Nhập chuỗi phép tính (logarit và mũ): ")
print(type(expression))

try:
    # Tính toán kết quả
    result = eval_safe(expression)
    print(f"Kết quả: {result}")
except Exception as e:
    print(f"Có lỗi xảy ra: {e}")
