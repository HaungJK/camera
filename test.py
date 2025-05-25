import tkinter as tk
from tkinter import messagebox

# 定义相机参数库（示例）
camera_library = [
    {"name": "四百万IDS相机", "resolution": (2048, 2048), "pixel_size": 5.3, "real_size": 10.8544},  # 分辨率(宽度 x 高度)，像元尺寸（单位：微米）
    {"name": "一百万IDS相机", "resolution": (1280, 1024), "pixel_size": 5.3, "real_size": 6.784}
]

# 定义镜头参数库（示例）
lens_library = [
    {"name": "16mm镜头", "focal_length": 16},  # 焦距（单位：mm）
    {"name": "25mm镜头", "focal_length": 25},
    {"name": "50mm镜头", "focal_length": 50}
]

def calculate_camera_and_lens():
#   try:
#         # 获取输入
#         fov = float(fov_entry.get())  # 视场（mm）最大边
#         object_distance = float(object_distance_entry.get())  # 物距（mm）
        
#         # 根据用户输入的视场和物距选择合适的镜头
#         selected_lens = None
#         selected_camera = None
#         real_object_distance = None
#         for lens in lens_library:
#             for camera in camera_library:
#             # 假设物距和视场的关系决定镜头的焦距选择
#                 required_real_size =  fov *  lens["focal_length"] / object_distance
#                 if required_real_size < camera["real_size"] :  # 找到合适的焦距
#                     selected_lens = lens
#                     selected_camera = camera
#                     real_object_distance = fov *  lens["focal_length"] / camera["real_size"] 
#                     # 显示计算结果
#                     result_label.config(text=f"推荐镜头: {selected_lens['name']} (焦距: {selected_lens['focal_length']}mm)\n"
#                                 f"推荐相机: {selected_camera['name']} (分辨率: {selected_camera['resolution'][0]}x{selected_camera['resolution'][1]})\n"
#                                 f"像元尺寸: {selected_camera['pixel_size']} 微米\n"
#                                 f"测量物距: {real_object_distance} mm\n")
#                     break
        
#         if selected_lens is None:
#             messagebox.showwarning("警告", "未找到合适的镜头！")
#             return  
    try:
        # 获取输入
        fov = float(fov_entry.get())  # 视场（mm）最大边
        object_distance = float(object_distance_entry.get())  # 物距（mm）

        # 存储符合条件的结果
        results = []

        # 遍历镜头和相机组合
        for lens in lens_library:
            for camera in camera_library:
                required_real_size = fov * lens["focal_length"] / object_distance
                if required_real_size < camera["real_size"]:
                    real_object_distance = fov * lens["focal_length"] / camera["real_size"]
                    results.append({
                        "lens": lens,
                        "camera": camera,
                        "real_object_distance": real_object_distance
                    })

        # 显示结果
        if not results:
            messagebox.showwarning("警告", "未找到合适的镜头和相机组合！")
            return

        result_text = "推荐的镜头与相机组合：\n"
        for i, res in enumerate(results, start=1):
            result_text += (
                f"{i}. 推荐镜头: {res['lens']['name']} (焦距: {res['lens']['focal_length']}mm)\n"
                f"   推荐相机: {res['camera']['name']} (分辨率: {res['camera']['resolution'][0]}x{res['camera']['resolution'][1]})\n"
                f"   像元尺寸: {res['camera']['pixel_size']} 微米\n"
                f"   测量物距: {res['real_object_distance']:.2f} mm\n\n"
            )

        result_label.config(text=result_text.strip())

    except ValueError:
        messagebox.showerror("输入错误", "请确保所有输入都为有效的数字！")       
        
    except ValueError:
        messagebox.showerror("输入错误", "请确保所有输入都为有效的数字！")

# 创建主窗口
root = tk.Tk()
root.title("相机与镜头选型计算器")

# 设置窗口大小
root.geometry("500x400")

# 视场输入
fov_label = tk.Label(root, text="视场（FOV）最大边（mm）:")
fov_label.pack()
fov_entry = tk.Entry(root)
fov_entry.pack()

# 物距输入
object_distance_label = tk.Label(root, text="物距(mm):")
object_distance_label.pack()
object_distance_entry = tk.Entry(root)
object_distance_entry.pack()

# 计算按钮
calculate_button = tk.Button(root, text="计算", command=calculate_camera_and_lens)
calculate_button.pack()

# 显示结果
result_label = tk.Label(root, text="请输入参数后点击计算。")
result_label.pack()

# 运行主循环
root.mainloop()
