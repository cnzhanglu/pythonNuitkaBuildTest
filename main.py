import sys
from PySide6.QtWidgets import QApplication, QLabel

def main():
    # 创建 Qt 应用程序对象
    app = QApplication(sys.argv)

    # 创建一个 QLabel 控件并设置文本
    label = QLabel("Hello, World!")

    # 显示 QLabel 控件
    label.show()

    # 运行 Qt 应用程序
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
