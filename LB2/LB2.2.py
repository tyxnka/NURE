import hashlib

def generate_file_hashes(*file_paths):
    hashes = {}

    for path in file_paths:
        try:
            with open(path, 'rb') as file:
                content = file.read()
                sha256_hash = hashlib.sha256(content).hexdigest()
                hashes[path] = sha256_hash

        except FileNotFoundError:
            print(f"Файл не знайдено: {path}")
        except IOError as e:
            print(f"Помилка читання файлу {path}: {e}")

    return hashes

result = generate_file_hashes("log1.txt", "log2.txt", "log.txt")

print("\nSHA-256 хеші файлів:")
for path, file_hash in result.items():
    print(f"{path}: {file_hash}")
