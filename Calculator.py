class Calculator:
    """
    一个简单的计算器类，支持加减乘除四则运算
    """
    
    def add(self, a, b):
        """加法"""
        return a + b
    
    def subtract(self, a, b):
        """减法"""
        return a - b
    
    def multiply(self, a, b):
        """乘法"""
        return a * b
    
def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Error: Division by zero is undefined. Please provide a non-zero divisor."
    except TypeError:
        return "Error: Invalid input types. Please provide numbers for division."


# 使用示例
if __name__ == "__main__":
    calc = Calculator()
    
    print(f"10 + 5 = {calc.add(10, 5)}")           # 15
    print(f"10 - 5 = {calc.subtract(10, 5)}")      # 5
    print(f"10 * 5 = {calc.multiply(10, 5)}")      # 50
    print(f"10 / 5 = {calc.divide(10, 5)}")        # 2.0
