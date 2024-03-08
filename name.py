import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QVBoxLayout, QWidget, QFileDialog, QMessageBox, QTextEdit
from PyQt5.QtGui import QPixmap
import random

class RandomCaller(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        # 设置窗口标题和大小
        self.setWindowTitle('随机点名程序')
        self.setGeometry(500, 500, 500, 500)

        layout = QVBoxLayout()

        # 创建两个标签，用于显示名单和点名结果
        self.label1 = QLabel(self)
        self.label1.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.label1)

        self.label2 = QLabel(self)
        self.label2.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.label2)

        # 创建点名按钮，点击时调用call_name方法
        self.button = QPushButton('点名', self)
        self.button.clicked.connect(self.call_name)
        layout.addWidget(self.button)

        # 创建选择名单文件按钮，点击时调用select_file方法
        self.file_button = QPushButton('选择名单文件', self)
        self.file_button.clicked.connect(self.select_file)
        layout.addWidget(self.file_button)

        # 创建文本编辑框，用于显示名单内容
        self.text_edit = QTextEdit(self)
        layout.addWidget(self.text_edit)

        # 添加预览开关按钮
        self.preview_button = QPushButton('预览/关闭', self)
        self.preview_button.clicked.connect(self.toggle_preview)
        layout.addWidget(self.preview_button)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        self.show()

    def call_name(self):
        # 从文件中读取学生名单，随机选择一个名字并显示在label2上
        with open(students_file_path, 'r', encoding='utf-8') as f:
            students = [line.strip() for line in f.readlines()]
        name = random.choice(students)
        self.label2.setText(f'<font weight="bold" color="red" size="16">点到的同学是：{name}</font>')

    def select_file(self):
        # 选择名单文件，将文件路径保存到全局变量students_file_path中，并将名单内容显示在文本编辑框中
        global students_file_path
        file_path, _ = QFileDialog.getOpenFileName(self, '选择名单文件', '', '文本文件 (*.txt)')
        if file_path:
            students_file_path = file_path
            with open(students_file_path, 'r', encoding='utf-8') as f:
                students = [line.strip() for line in f.readlines()]
                self.text_edit.setPlainText(''.join(students))

    def update_images(self):
        # 更新label1的图片显示
        pixmap1 = QPixmap("C:\\Users\\3588223252_176470409\\Desktop\\3.jpg")
        self.label1.setPixmap(pixmap1)

    def show_copyright(self):
        # 显示版权声明信息框
        QMessageBox.about(self, "版权声明", "作者：Cy_5")

    def toggle_preview(self):
        # 切换名单内容预览的开关状态
        if self.text_edit.isVisible():
            self.text_edit.hide()
        else:
            self.text_edit.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    caller = RandomCaller()
    caller.update_images()
    caller.show()
    caller.show_copyright()
    sys.exit(app.exec_())
