def filter_ips(input_file_path, output_file_path, allowed_ips):
    ip_counts = {}

    try:
        with open(input_file_path, 'r', encoding='utf-8') as file:
            for line in file:
                parts = line.split()
                if len(parts) > 0:
                    ip = parts[0]
                    if ip in allowed_ips:
                        ip_counts[ip] = ip_counts.get(ip, 0) + 1

    except FileNotFoundError:
        print(f"Файл не знайдено: {input_file_path}")
        return
    except IOError as e:
        print(f"Помилка читання файлу: {e}")
        return

    try:
        with open(output_file_path, 'w', encoding='utf-8') as out_file:
            for ip, count in ip_counts.items():
                out_file.write(f"{ip} - {count}\n")

        print(f"Результат збережено у файл: {output_file_path}")

    except IOError as e:
        print(f"Помилка запису до файлу: {e}")

allowed_ips = ['127.0.0.1', '192.168.0.1']
filter_ips('apache_logs.txt', 'filtered_ips.txt', allowed_ips)
