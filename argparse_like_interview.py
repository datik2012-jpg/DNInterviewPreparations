#Task: health checks for ULRs
#Ты разрабатываешь инструмент для CI. Он проверяет доступность нескольких сервисов перед запуском интеграционных тестов.
#Запуск:
#python argparse_like_interview.py --urls https://example.com http://127.0.0.1:9999 --timeout 3

#Требования:
#- --urls принимает один или несколько URL.
#- --timeout — число секунд, по умолчанию 5.
#- Для каждого URL выполнить GET-запрос.
#- HTTP-код 200–299 считать успехом.
#- При timeout или ошибке соединения записать ошибку и продолжить проверку остальных URL.
#- Напечатать результат каждого запроса.
#- Завершить скрипт с кодом 0, если все проверки успешны, иначе с кодом 1.
#Пример вывода:
#OK https://example.com status=200
#FAIL http://127.0.0.1:9999 error=connection_error

#Здесь соединяются Python, argparse, HTTP, исключения и поведение инструмента в CI. После этого возьмём практическую диагностику контейнера.

#Next task add attmpts
#conditions:
#Логика:
  # 1. При timeout или connection error повторить запрос, если остались попытки.
   #2. Между попытками — time.sleep(1).
   #3. Если получен HTTP-ответ — проверить статус и выйти из цикла попыток через break.
   #4. had_failure = True ставить при неуспешном HTTP-коде или после последней неудачной попытки, а не после первой.
   
   #run and check last exit code:
   #  python .\argparse_like_interview.py --urls http://127.0.0.1:9999 https://example.com --timeout 3
   # $LASTEXITCODE
    

import argparse
import requests
import time


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="CI argument parser")
    parser.add_argument(
        "--urls",
        nargs="+",
        required=True,
        help="Provide one or more URLs for checks",
    )
    parser.add_argument("--timeout", default=5, type=int)

    args = parser.parse_args()
    had_failure = False
    
    for arg_url in args.urls:
        count_failures = 1
        for attempt in range(1, 4):
            
            try:
                response = requests.get(arg_url, timeout=args.timeout)
            except requests.exceptions.Timeout:
                print(f"FAIL {arg_url} error=timeout")
                #had_failure = True
            except requests.exceptions.ConnectionError:
                print(f"FAIL {arg_url} error=connection_error")
                #had_failure = True
            else:
                if 200 <= response.status_code <= 299:
                    print(f"OK {arg_url} status={response.status_code}")
                else:
                    print(f"FAIL {arg_url} status={response.status_code}")
                    had_failure = True
                break    
            
            
            if count_failures == 3:
                had_failure = True    
            else:
                time.sleep(1)
                  
            count_failures += 1     

    if had_failure:
        raise SystemExit(1)
    
    