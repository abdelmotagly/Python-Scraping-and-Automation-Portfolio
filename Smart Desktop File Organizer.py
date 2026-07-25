import os
import shutil

target_folder = os.path.dirname(os.path.abspath(__file__))
current_script = os.path.basename(__file__)

file_types = {
    '📝 Documents': ['.pdf', '.docx', '.txt', '.xlsx', '.pptx', '.csv'],
    '🎨 Images': ['.jpg', '.jpeg', '.png', '.gif', '.svg', '.webp'],
    '🎬 Videos': ['.mp4', '.mkv', '.avi', '.mov'],
    '🎵 Audio': ['.mp3', '.wav', '.flac'],
    '📦 Compressed': ['.zip', '.rar', '.7z', '.tar']
}

def get_unique_filename(destination, filename):
    """إعادة تسمية الملف تلقائياً إذا كان هناك ملف بنفس الاسم في المجلد الهدف"""
    base, extension = os.path.splitext(filename)
    counter = 1
    new_filename = filename
    while os.path.exists(os.path.join(destination, new_filename)):
        new_filename = f"{base}_{counter}{extension}"
        counter += 1
    return new_filename

print("⏳ جاري فحص المجلد وتنظيم الملفات...")

moved_files_count = 0

try:
    for filename in os.listdir(target_folder):
        file_path = os.path.join(target_folder, filename)

        if os.path.isfile(file_path) and filename != current_script and not filename.startswith('.'):
            file_extension = os.path.splitext(filename)[1].lower()

            # تحديد المجلد المناسب
            target_subfolder = '📂 Others'
            for folder_name, extensions in file_types.items():
                if file_extension in extensions:
                    target_subfolder = folder_name
                    break

            destination_folder = os.path.join(target_folder, target_subfolder)
            if not os.path.exists(destination_folder):
                os.makedirs(destination_folder)

            unique_name = get_unique_filename(destination_folder, filename)
            shutil.move(file_path, os.path.join(destination_folder, unique_name))
            moved_files_count += 1

    print(f"✨ نجاح باهر! تم تصنيف ونقل {moved_files_count} ملف كالمحترفين.")

except Exception as e:
    print(f"❌ حدث خطأ غير متوقع أثناء تنظيم الملفات: {e}")