def analyze_log_file(log_file_path):
    response_codes = {}

    try:
        with open(log_file_path, 'r', encoding='utf-8') as file:
            for line in file:
                parts = line.split()
                if len(parts) > 8:
                    try:
                        code = int(parts[8])
                        response_codes[code] = response_codes.get(code, 0) + 1
                    except ValueError:
                        print(f"Неправильний код відповіді в рядку: {line.strip()}")
                        continue

    except FileNotFoundError:
        print(f"Помилка: файл '{log_file_path}' не знайдено.")
    except IOError as e:
        print(f"Помилка при читанні файлу: {e}")

    return response_codes


result = analyze_log_file("apache_logs.txt")
print("Коди HTTP та їх кількість:")
for code, count in result.items():
    print(f"{code}: {count}")
