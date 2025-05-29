def is_valid_github_username(username):
    cleaned = username.replace("-", "")
    return cleaned.isalnum() and "_" not in username

print(is_valid_github_username("ali-coder"))  # True
print(is_valid_github_username("diyor_123"))  # False