import csv
import os


def process_data(input_file, output_file):
    """Функция для обработки CSV-файла без использования pandas"""
    with open(input_file, mode='r', encoding='utf-8') as infile, \
            open(output_file, mode='w', encoding='utf-8', newline='') as outfile:

        reader = csv.DictReader(infile)
        fieldnames = reader.fieldnames
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        writer.writeheader()

        for row in reader:
            # Пример обработки: очистка пробелов и пустых значений
            processed_row = {}
            for key, value in row.items():
                if value.strip() == '':
                    processed_row[key] = 'N/A'  # Заменяем пустые значения
                else:
                    processed_row[key] = value.strip()  # Удаляем лишние пробелы
            writer.writerow(processed_row)


if __name__ == "__main__":
    input_csv = "47.csv"
    output_csv = "47_processed.csv"

    if os.path.exists(input_csv):
        process_data(input_csv, output_csv)
        print(f"Данные успешно обработаны и сохранены в {output_csv}")
    else:
        print(f"Ошибка: файл {input_csv} не найден!")