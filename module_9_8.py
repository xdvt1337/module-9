import threading
import time

def write_words(word_count, file_name):
    with open(file_name, 'w') as file:
        for i in range(1, word_count + 1):
            file.write(f"Какое-то слово № {i}\n")
            time.sleep(0.1)
    print(f"Завершилась запись в файл {file_name}")

start_time = time.time()

write_words(10, "example1.txt")
write_words(30, "example2.txt")
write_words(200, "example3.txt")
write_words(100, "example4.txt")

end_time = time.time()
print(f"Время выполнения функций: {end_time - start_time:.6f} секунд")

def threaded_write_words(word_count, file_name):
    write_words(word_count, file_name)

start_time_threads = time.time()

threads = [
    threading.Thread(target=threaded_write_words, args=(10, "example5.txt")),
    threading.Thread(target=threaded_write_words, args=(30, "example6.txt")),
    threading.Thread(target=threaded_write_words, args=(200, "example7.txt")),
    threading.Thread(target=threaded_write_words, args=(100, "example8.txt"))
]

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()

end_time_threads = time.time()
print(f"Время выполнения потоков: {end_time_threads - start_time_threads:.6f} секунд")
