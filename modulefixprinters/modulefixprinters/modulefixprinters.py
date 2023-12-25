import os
import subprocess
import sys

def clear_print_queue():
    # Очищаем очередь печати
    subprocess.run(["powershell", "Get-WmiObject -Query 'Select * From Win32_PrintJob' | ForEach-Object { $_.Delete() }"], check=True)
    print("Очередь печати очищена")

def restart_print_spooler():
    # Перезапускаем диспетчер печати
    subprocess.run(["net", "stop", "Spooler"], check=True)
    subprocess.run(["net", "start", "Spooler"], check=True)
    print("Диспетчер печати перезапущен")

def main():
    user_input = input("Пофиксим принтеры? (да/нет): ")
    
    if user_input.lower() == "да":
        clear_print_queue()
        restart_print_spooler()
    else:
        print("Отменено пользователем.")
        sys.exit()

if __name__ == "__main__":
    main()
