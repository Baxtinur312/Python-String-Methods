def clean_comment(text):
    cleaned = text.lower().replace("bad", "").strip()
    return True if "bad" not in cleaned else False

print(clean_comment("this is bad"))     # True
print(clean_comment("This is BAD"))     # True
