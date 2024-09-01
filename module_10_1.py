from time import sleep
import threading
import time

def write_words(word_count, file_name):
  """
  Записывает слова в файл с заданным количеством и паузой.

  Args:
    word_count: Количество слов для записи.
    file_name: Имя файла для записи.
  """
  with open(file_name, 'w') as file:
    for i in range(1, word_count + 1):
      file.write(f"Какое-то слово № {i}\n")
      sleep(0.1)
    print(f"Завершилась запись в файл {file_name}")

# Замеры времени работы функций
start_time_functions = time.time()

write_words(10, "example1.txt")
write_words(30, "example2.txt")
write_words(200, "example3.txt")
write_words(100, "example4.txt")

end_time_functions = time.time()
time_functions = end_time_functions - start_time_functions
print(f"Время работы функций: {time_functions:.2f} секунд")

# Замеры времени работы потоков
start_time_threads = time.time()

threads = []
threads.append(threading.Thread(target=write_words, args=(10, "example5.txt")))
threads.append(threading.Thread(target=write_words, args=(30, "example6.txt")))
threads.append(threading.Thread(target=write_words, args=(200, "example7.txt")))
threads.append(threading.Thread(target=write_words, args=(100, "example8.txt")))

for thread in threads:
  thread.start()

for thread in threads:
  thread.join()

end_time_threads = time.time()
time_threads = end_time_threads - start_time_threads
print(f"Время работы потоков: {time_threads:.2f} секунд")