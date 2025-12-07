import os
from PIL import Image, ImageDraw, ImageFont


def add_num(image_path, save_path, text):

    try:
        img = Image.open(image_path)
        draw = ImageDraw.Draw(img)

        width, height = img.size
        font_size = int(height / 4)
        try:
            my_font = ImageFont.truetype("arial.ttf", font_size)
        except OSError:
            my_font = ImageFont.load_default()


        position = (width - font_size + 10, 0)

        draw.text(position, text, fill="red", font=my_font)


        img.save(save_path)
        print(f"处理成功：保存为 -> {save_path}")

    except Exception as e:
        print(f"出错跳过：{image_path}，原因：{e}")


def batch_process_sequential(input_folder, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)


    all_files = os.listdir(input_folder)

    all_files.sort()
    count = 0
    for filename in all_files:
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp')):
            count = count + 1
            full_input_path = os.path.join(input_folder, filename)
            new_filename = f"{count}.png"
            full_output_path = os.path.join(output_folder, new_filename)
            number_text = str(count)
            add_num(full_input_path, full_output_path, number_text)

if __name__ == '__main__':
    input_dir = r"F:\python\.venv\project\picture"
    output_dir = r"F:\python\.venv\project\output_numbered"
    print("开始按顺序编号处理...")
    batch_process_sequential(input_dir, output_dir)
    print("全部搞定！去 output_numbered 文件夹看看吧。")