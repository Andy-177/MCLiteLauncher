import tkinter as tk
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
    os.system(rf"D:\JRE21\bin\javaw.exe -Xmx2048m -Dfile.encoding=GB18030 -Dstdout.encoding=GB18030 -Dstderr.encoding=GB18030 -Djava.rmi.server.useCodebaseOnly=true -Dcom.sun.jndi.rmi.object.trustURLCodebase=false -Dcom.sun.jndi.cosnaming.object.trustURLCodebase=false -Dlog4j2.formatMsgNoLookups=true -Dlog4j.configurationFile=E:\Minecraft\HMCL\.minecraft\versions\cmpack_1.8.8\log4j2.xml -Dminecraft.client.jar=.minecraft\versions\cmpack_1.8.8\cmpack_1.8.8.jar -XX:+UnlockExperimentalVMOptions -XX:+UseG1GC -XX:G1NewSizePercent=20 -XX:G1ReservePercent=20 -XX:MaxGCPauseMillis=50 -XX:G1HeapRegionSize=32m -XX:-UseAdaptiveSizePolicy -XX:-OmitStackTraceInFastThrow -XX:-DontCompileHugeMethods -Dfml.ignoreInvalidMinecraftCertificates=true -Dfml.ignorePatchDiscrepancies=true -XX:HeapDumpPath=MojangTricksIntelDriversForPerformance_javaw.exe_minecraft.exe.heapdump -Djava.library.path=E:\Minecraft\HMCL\.minecraft\versions\cmpack_1.8.8\natives-windows-x86_64 -Dminecraft.launcher.brand=HMCL -Dminecraft.launcher.version=3.6.12 -cp E:\Minecraft\HMCL\.minecraft\libraries\oshi-project\oshi-core\1.1\oshi-core-1.1.jar;E:\Minecraft\HMCL\.minecraft\libraries\net\java\dev\jna\jna\3.4.0\jna-3.4.0.jar;E:\Minecraft\HMCL\.minecraft\libraries\net\java\dev\jna\platform\3.4.0\platform-3.4.0.jar;E:\Minecraft\HMCL\.minecraft\libraries\com\ibm\icu\icu4j-core-mojang\51.2\icu4j-core-mojang-51.2.jar;E:\Minecraft\HMCL\.minecraft\libraries\net\sf\jopt-simple\jopt-simple\4.6\jopt-simple-4.6.jar;E:\Minecraft\HMCL\.minecraft\libraries\com\paulscode\codecjorbis\20101023\codecjorbis-20101023.jar;E:\Minecraft\HMCL\.minecraft\libraries\com\paulscode\codecwav\20101023\codecwav-20101023.jar;E:\Minecraft\HMCL\.minecraft\libraries\com\paulscode\libraryjavasound\20101123\libraryjavasound-20101123.jar;E:\Minecraft\HMCL\.minecraft\libraries\com\paulscode\librarylwjglopenal\20100824\librarylwjglopenal-20100824.jar;E:\Minecraft\HMCL\.minecraft\libraries\com\paulscode\soundsystem\20120107\soundsystem-20120107.jar;E:\Minecraft\HMCL\.minecraft\libraries\io\netty\netty-all\4.0.23.Final\netty-all-4.0.23.Final.jar;E:\Minecraft\HMCL\.minecraft\libraries\com\google\guava\guava\17.0\guava-17.0.jar;E:\Minecraft\HMCL\.minecraft\libraries\org\apache\commons\commons-lang3\3.3.2\commons-lang3-3.3.2.jar;E:\Minecraft\HMCL\.minecraft\libraries\commons-io\commons-io\2.4\commons-io-2.4.jar;E:\Minecraft\HMCL\.minecraft\libraries\commons-codec\commons-codec\1.9\commons-codec-1.9.jar;E:\Minecraft\HMCL\.minecraft\libraries\net\java\jinput\jinput\2.0.5\jinput-2.0.5.jar;E:\Minecraft\HMCL\.minecraft\libraries\net\java\jutils\jutils\1.0.0\jutils-1.0.0.jar;E:\Minecraft\HMCL\.minecraft\libraries\com\google\code\gson\gson\2.2.4\gson-2.2.4.jar;E:\Minecraft\HMCL\.minecraft\libraries\com\mojang\authlib\1.5.21\authlib-1.5.21.jar;E:\Minecraft\HMCL\.minecraft\libraries\org\apache\commons\commons-compress\1.8.1\commons-compress-1.8.1.jar;E:\Minecraft\HMCL\.minecraft\libraries\org\apache\httpcomponents\httpclient\4.3.3\httpclient-4.3.3.jar;E:\Minecraft\HMCL\.minecraft\libraries\commons-logging\commons-logging\1.1.3\commons-logging-1.1.3.jar;E:\Minecraft\HMCL\.minecraft\libraries\org\apache\httpcomponents\httpcore\4.3.2\httpcore-4.3.2.jar;E:\Minecraft\HMCL\.minecraft\libraries\org\apache\logging\log4j\log4j-api\2.0-beta9\log4j-api-2.0-beta9.jar;E:\Minecraft\HMCL\.minecraft\libraries\org\apache\logging\log4j\log4j-core\2.0-beta9\log4j-core-2.0-beta9.jar;E:\Minecraft\HMCL\.minecraft\libraries\org\lwjgl\lwjgl\lwjgl\2.9.4-nightly-20150209\lwjgl-2.9.4-nightly-20150209.jar;E:\Minecraft\HMCL\.minecraft\libraries\org\lwjgl\lwjgl\lwjgl_util\2.9.4-nightly-20150209\lwjgl_util-2.9.4-nightly-20150209.jar;E:\Minecraft\HMCL\.minecraft\versions\cmpack_1.8.8\cmpack_1.8.8.jar -javaagent:C:\Users\32684\AppData\Roaming\.hmcl\authlib-injector.jar=https://littleskin.cn/api/yggdrasil/ -Dauthlibinjector.side=client -Dauthlibinjector.yggdrasil.prefetched=eyJtZXRhIjp7InNlcnZlck5hbWUiOiJMaXR0bGVTa2luIiwiaW1wbGVtZW50YXRpb25OYW1lIjoiWWdnZHJhc2lsIENvbm5lY3QiLCJpbXBsZW1lbnRhdGlvblZlcnNpb24iOiIwLjAuNiIsImxpbmtzIjp7ImFubm91bmNlbWVudCI6Imh0dHBzOi8vbGl0dGxlc2tpbi5jbi9hcGkvYW5ub3VuY2VtZW50cyIsImhvbWVwYWdlIjoiaHR0cHM6Ly9saXR0bGVza2luLmNuIiwicmVnaXN0ZXIiOiJodHRwczovL2xpdHRsZXNraW4uY24vYXV0aC9yZWdpc3RlciJ9LCJmZWF0dXJlLm5vX2VtYWlsX2xvZ2luIjp0cnVlLCJmZWF0dXJlLm9wZW5pZF9jb25maWd1cmF0aW9uX3VybCI6Imh0dHBzOi8vb3Blbi5saXR0bGVza2luLmNuLy53ZWxsLWtub3duL29wZW5pZC1jb25maWd1cmF0aW9uIn0sInNraW5Eb21haW5zIjpbImxpdHRsZXNraW4uY24iXSwic2lnbmF0dXJlUHVibGlja2V5IjoiLS0tLS1CRUdJTiBQVUJMSUMgS0VZLS0tLS1cbk1JSUNJakFOQmdrcWhraUc5dzBCQVFFRkFBT0NBZzhBTUlJQ0NnS0NBZ0VBckdjTk9PRklxTEpTcW9FM3UwaGpcbnRPRW5PY0VUM3dqOURyc3MxQkU2c0JxZ1BvMGJNdWxPVUxocWprYy91SC93eW9zWW56dzN4YWF6SnQ4N2pUSGhcbko4QlBNeENlUU1veUVkUm9TM0puajFHMEtlemo0QTJiNjFQSkpNMURwdkRBY3FRQllzclNkcEJKKzUyTWpvR1NcbnZKb2VRTzVYVWxKVlFtMjEvSG1KbnFzUGh6Y0E2SGdZNzFSSFlFNXhuaHBXSmlQeExLVVB0bXQ2Q05ZVVFRb1Ncbm8ydjM2WFdnTW1MQlpoQWJOT1B4WVgrMWlveEthbWpoTE8yOVVod3RnWTlVNlBXRU83L1NCZlh6eVJQVHpoUFZcbjJuSHE3S0pxZDhJSXJsdHNsdjZpLzRGRU04MWl2Uy9tbStQTjNoWWxJWUs2ejZZbWlpMW5yUUFwbHNKNjdPR3FcbllIdFdLT3ZwZlR6T29sbHVnc1JpaGtBRzRPQjZoTTBQcjQ1ampDM1RJYzdlTzdrT2dJY0dVR1VRR3V1dWdERXpcbkoxTjlGRlduTi9INlA5dWtGZWc1U21HQzUrd21VUFpaQ3ROQkxyOG84c0k1SDdRaEs3Tmd3Q2FHRm9ZdWlBR0xcbmd6M2svM1l3SjQwQmJ3UWF5UTJnSXFlbnorWE9GSUFsYWp2Ky9ueWZjRHZaSDl2R05LUDlsVmNIWFVUNVlSblNcblpTSG81bHd2VnJZVXJxRUFiaC96RHo4UU1FeWl1ald2VWtQaFpzOWZoNmZpbVVHeHRtOG1GSVBDdFBKVlhqZVlcbndEM0x2dDNhSUIxSkhkVVRKUjNlRWM0ZUlhVEtNd01QeUpSelZuNXpLc2l0YVp6M25uL2NPQS93WkM5b3F5RVVcbm1jOWg2Wk1SVFJVRUU0VHRhSnlnOWxNQ0F3RUFBUT09XG4tLS0tLUVORCBQVUJMSUMgS0VZLS0tLS1cbiJ9 pl.cmpack.Main --username {playername} --version cmpack_1.8.8 --gameDir E:\Minecraft\HMCL\.minecraft\versions\cmpack_1.8.8 --assetsDir E:\Minecraft\HMCL\.minecraft\assets --assetIndex 1.8 --uuid f688f17e20bc4325a55562d29d869ca9 --accessToken eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ijlvc3R5V1VzLXBPempUdmNkQXB2Sjl5Qk1NMF9DNUlkYnlPc3RsUmlaWE0ifQ.eyJqdGkiOiJmNTk4NDYwMS1hODcxLTQxOTYtOWQwMy1kZDhhYmUzNmE2YjUiLCJzdWIiOiIxNzA5NTI1IiwiYXVkIjoiODY1IiwibmJmIjoxNzUxMjA4MTI5LCJleHAiOjE3NTI1MDQxMjgsInNjb3BlcyI6WyJZZ2dkcmFzaWwuUGxheWVyUHJvZmlsZXMuU2VsZWN0IiwiWWdnZHJhc2lsLlNlcnZlci5Kb2luIl0sInNlbGVjdGVkUHJvZmlsZSI6ImY2ODhmMTdlMjBiYzQzMjVhNTU1NjJkMjlkODY5Y2E5IiwiaWF0IjoxNzUxMjA4MTI4LCJpc3MiOiJZZ2dkcmFzaWwgQ29ubmVjdCJ9.rxyEG6pg1BypsRwpLatAgBIZv3qdp3dsifPwGc72ddyMn_lovBq6juiNGAk_Vtb4v0TtyErO91JCQu0UBilI6Diq6dXcYp3BpzkC9Yrt5bwr3fI4O_LmptkISrQfzSzDexrNf_wYZzYD80PgJl51oOABQSqjCpvdBzxlH8NcTN7Mk-FGrS2amEQNs1_Vw5luikdj1nsKWaEVmfi03PXTHNp1r2ULmph11b0to-YpK4brJSaG_TYn3E-3DIMe7fwjO42CYuxkubbvP_cpRT8d034g1zqdOdKPtJzr4wqAfdBmNIJNOrEZB4rLdaO7c5yfeDTQC5j3GswqzG0d71qbBmIIic9dP1SBKrGrZ64-yyuxqS13RuGoNeZuGZvZR2Q_VVaU5T7MdFwprCKegeqw8vns8yEgXxX2CSlJ2BL5hY8NfI7w2z_tTajT_Se-sYtI0z2jOjd9XqvnhLJLRM7aJc2fWW-8NuzDgAMR7O2VntgWECChq-QwjV0v0uih3SaAfMUxl8boXQH9LvBnUMksybJV7LJ47-Kjy5xQfay71B2YZjHiXcWSnG20gbZYTWZNzjvI98bLrsh6Ri6dUaDP5juRKYA_BRiO5cEjd-M0yEIcm4PTpzI-2uN6p1KQXvuVaaaefmt8DJCg5Ag3wRwp_znNs6dMKbfpmQ0LMFFm1wk --userProperties {{}} --userType msa --width 854 --height 480")
    os.system(r"""pause""")
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
