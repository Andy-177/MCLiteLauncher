import tkinter as tk
from tkinter import ttk
import os
from tkinter import messagebox
messagebox.showwarning("警告", "这是Lite版构建器，只会生成固定玩家名称的启动器")
# 创建主窗口
window = tk.Tk()
# 设置窗口标题
window.title("Builderlite")
# 设置窗口大小
window.geometry("400x250")
# 窗口配置
window.configure(bg="black")
window.resizable(False, False)
def builder():
    from tkinter import messagebox
    # 获取颜色输入
    color = Launcher_color.get().strip()
    if not color:
        color = "#7902CE"
    # 获取启动参数
    launch_param = launcher_n.get().strip()
    # 获取脚本类型
    script_type = script_type_var.get().strip()
    # 校验
    if not launch_param:
        messagebox.showwarning("提示", "请输入启动参数！")
        return
    if not script_type:
        messagebox.showwarning("提示", "请选择脚本类型！")
        return

    # 生成命令
    if script_type == "ps1":
        launch_cmd = f'    os.system("powershell \"& {launch_param}\"")'
    else:
        launch_cmd = f'    os.system(r"""{launch_param}""")'

    # 合并模板逻辑
    # 没有合并模板逻辑

    # 只生成无 playername 相关内容的模板
    template_code = f'''import tkinter as tk
import os
window = tk.Tk()
window.title("Launcher")
window.geometry("400x250")
window.configure(bg="black")
window.resizable(False, False)

def Launcher():
{launch_cmd}

Launcherbutton = tk.Button(
    window,
    text="Launcher",
    command=Launcher,
    fg="white",
    bg="{color}",
    activebackground="{color}",
    activeforeground="white",
    font=("Comic Sans MS", 14, "italic"),
    bd=0,
    highlightthickness=0
)
Launcherbutton.place(relx=0.5, rely=0.5, anchor="center", width=250, height=100)
window.withdraw()
window.update_idletasks()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
size = tuple(int(_) for _ in window.geometry().split('+')[0].split('x'))
x = (screen_width - size[0]) // 2
y = (screen_height - size[1]) // 2
window.geometry(f"{{size[0]}}x{{size[1]}}+{{x}}+{{y}}")
window.deiconify()
window.mainloop()
'''

    # 写入 Launcher.py
    with open("Launcher.py", "w", encoding="utf-8") as f:
        f.write(template_code)
    messagebox.showinfo("完成", f"Launcher.py 已生成，主色为 {color}")
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