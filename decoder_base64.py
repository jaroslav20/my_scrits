"""

Скрипт предназначен для декодирования строки, закодированной в base64 и сжатой с помощью gzip.
Программа выполняет следующие шаги:
1. Добавляет недостающие символы заполнения (=) к строке base64, если это необходимо.
2. Декодирует строку base64 в бинарные данные.
3. Разжимает бинарные данные, используя gzip.
4. Преобразует разжатые данные в строку и выводит её на экран.

"""

import base64
import gzip
import io

encoded_str = "H4sIAAAAAAAA_0q0MrSqLraysFJKK8rPDUhMT1WyLrYyt1JKTixJzMlPV7KuBQQAAP__dhSE3CMAAAA"


def main():
    # Попробуем добавить недостающие символы заполнения (=) и снова декодировать
    padding_needed = 4 - len(encoded_str) % 4
    encoded_str_padded = encoded_str + ("=" * padding_needed)

    # Декодируем строку из base64
    decoded_data = base64.urlsafe_b64decode(encoded_str_padded)

    # Разжимаем данные
    with gzip.GzipFile(fileobj=io.BytesIO(decoded_data)) as gz:
        decompressed_data = gz.read().decode('utf-8')

    print(decompressed_data)


if __name__ == '__main__':
    main()
