import sys
import datetime

def main():
    # 1. 正常输出
    print("Hello, my Python journey starts today!")
    
    # 2. 打印环境信息（方便记录）
    print(f"Python Version: {sys.version.split()[0]}")
    print(f"Current Date: {datetime.date.today()}")
    
    # 3. 模拟一个失败场景处理：检查 Python 版本是否过低
    # 如果当前 Python 版本低于 3.10，就给出友好的错误提示，而不是报错崩溃
    if sys.version_info < (3, 10):
        print("\n[Error] Your Python version is too old. Please upgrade to 3.10 or higher.")
        sys.exit(1)
    else:
        print("\n[Check] Python version is good. Ready to code!")

if __name__ == "__main__":
    main()