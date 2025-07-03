import tkinter as tk
from tkinter import messagebox, ttk
import os
window = tk.Tk()
# 设置窗口标题
window.title("Builder")
# 设置窗口大小
window.geometry("400x250")
# 窗口配置
window.configure(bg="black")
window.resizable(False, False)

# 让主窗口居中显示（无移动过程）
window.withdraw()
window.update_idletasks()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
size = tuple(int(_) for _ in window.geometry().split('+')[0].split('x'))
x = (screen_width - size[0]) // 2
y = (screen_height - size[1]) // 2
window.geometry(f"{size[0]}x{size[1]}+{x}+{y}")
window.deiconify()

# 一切准备完毕后弹窗（窗口加载完后再弹）
def show_startup_tip():
    from tkinter import messagebox
    messagebox.showinfo("提示", "使用前请将启动参数里的用户名全部替换为{playername}")

window.after(100, show_startup_tip)
def builder():
    # 获取用户输入
    launcher_args = launcher_n.get()
    launcher_color = Launcher_color.get()
    script_type = script_type_var.get()
    # 读取模板文件内容（列式字符串）
    template = '''import tkinter as tk
import os
global playername
playername = ""
window = tk.Tk()
# 设置窗口标题
window.title("Launcher")
# 设置窗口大小
window.geometry("400x250")
# 窗口配置
window.configure(bg="black")
window.resizable(False, False)
def Launcher():
    print (playername)
def username_input():
    box = tk.Toplevel(window)
    # 设置窗口标题
    box.title("Name")
    # 设置窗口大小
    box.geometry("250x120")
    # 窗口配置
    box.configure(bg="black")
    box.resizable(False, False)
    # 添加标签和输入框
    lb = tk.Label(box, text="请输入你的MC昵称：", fg="white", bg="black", font=("Arial", 10))
    lb.place(x=10, y=10)
    username = tk.Entry(box, fg="black", bg="white", font=("Arial", 10))
    username.place(x=10, y=40, width=230, height=30)
    def on_ok():
        global playername
        playername = username.get()  # 获取输入框内容
        if not playername:  # 如果输入框为空
            playername = "player"  # 设置默认昵称
        box.destroy()  # 关闭输入框
        Launcher()  # 调用Launcher函数
    OK = tk.Button(
        box,
        text="OK",
        command=on_ok,  # 点击按钮后执行on_ok函数
        fg="white",
        bg="#7902CE",
        activebackground="#7902CE",
        activeforeground="white",  # 按下时字体颜色
        font=("Comic Sans MS", 14, "italic"),
        # 去除立体边框
        bd=0,  # 边框宽度为0
        highlightthickness=0  # 去除高亮边框
    )
    OK.place(x=10, y=80, width=230, height=30)

# 启动按钮
Launcherbutton = tk.Button(
    window,
    text="Launcher",
    command=username_input,
    fg="white",
    bg="#7902CE",
    activebackground="#7902CE",
    activeforeground="white",  # 按下时字体颜色
    font=("Comic Sans MS", 14, "italic"),
    # 去除立体边框
    bd=0,  # 边框宽度为0
    highlightthickness=0  # 去除高亮边框
)
Launcherbutton.place(relx=0.5, rely=0.5, anchor="center", width=250, height=100)
# 让主窗口居中显示（无移动过程）
window.withdraw()
window.update_idletasks()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
size = tuple(int(_) for _ in window.geometry().split('+')[0].split('x'))
x = (screen_width - size[0]) // 2
y = (screen_height - size[1]) // 2
window.geometry(f"{size[0]}x{size[1]}+{x}+{y}")
window.deiconify()
# 窗口主循环
window.mainloop()
'''
    # 替换颜色
    code = template.replace('#7902CE', launcher_color if launcher_color else '#7902CE')
    # 构建启动命令
    # 启动参数支持 {playername} 占位符
    if script_type == 'bat':
        launcher_code = ''
        for line in launcher_args.splitlines():
            if line.strip():
                # 替换 {playername} 为实际变量拼接
                line_with_var = line.replace('{playername}', '" + playername + "')
                launcher_code += f'    os.system(r"""{line_with_var}""")\n'
    elif script_type == 'ps1':
        launcher_code = ''
        for line in launcher_args.splitlines():
            if line.strip():
                line_with_var = line.replace('{playername}', '" + playername + "')
                launcher_code += f'    os.system(r"""& {line_with_var}""")\n'
    else:
        launcher_code = '    print(playername)\n'
    # 替换Launcher函数体，避免re.sub转义问题
    import re
    pattern = r'def Launcher\(\):\n(\s*)print \(playername\)'
    def repl(match):
        return f'def Launcher():\n{launcher_code.rstrip()}'
    code = re.sub(pattern, repl, code)
    # 保存到文件（生成 Launcher.py）
    with open('Launcher.py', 'w', encoding='utf-8') as f:
        f.write(code)
    # 构建成功弹窗提示
    from tkinter import messagebox
    messagebox.showinfo("构建完成", "Launcher.py 构建成功！")
lb1 = tk.Label(window, text="启动参数：",bg="black",fg="white", font=("Arial", 14))
lb1.place(x=0, y=10)
launcher_n = tk.Entry(window, fg="black", bg="white", font=("Arial", 10))
launcher_n.place(x=100, y=14, width=280, height=20)
lb2 = tk.Label(window, text="启动器颜色：",bg="black",fg="white", font=("Arial", 14))
lb2.place(x=0, y=50)
Launcher_color = tk.Entry(window, fg="black", bg="white", font=("Arial", 10))
Launcher_color.place(x=120, y=54, width=100, height=20)
lb3 = tk.Label(window, text="脚本类型：", bg="black", fg="white", font=("Arial", 14))
lb3.place(x=0, y=90)
script_type_var = tk.StringVar()
script_type_menu = ttk.Combobox(window, textvariable=script_type_var, values=["bat", "ps1"], font=("Arial", 10), state="readonly")
script_type_menu.place(x=100, y=94, width=100, height=24)

buildbutton = tk.Button(
    window,
    text="build your Minecraft Launcher",
    command=builder,
    fg="white",
    bg="#7902CE",
    activebackground="#7902CE",
    activeforeground="white",
    font=("Comic Sans MS", 14, "italic"),
    bd=0,
    highlightthickness=0
)
buildbutton.place(x=50, y=160, width=300, height=50)
# 窗口主循环
window.mainloop()