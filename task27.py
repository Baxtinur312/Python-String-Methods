def is_valid_file(filename):
    return filename.endswith(".pdf") or filename.endswith(".docx") or filename.endswith(".txt")

print(is_valid_file("report.pdf"))  # True
print(is_valid_file("photo.jpeg"))  # False