import requests

API_KEY = "t1.9euelZqQzZqKzsiQiZyLyJyclcqczO3rnpWamouYnJSKkZ6Zk5Cai5TLlszl9PdlGnFO-e9KWhmk3fT3JUluTvnvSloZpM3n9euelZqTx4mWmI6bjIucz4qMyI2bke_8xeuelZqTx4mWmI6bjIucz4qMyI2bkb3rnpWaycyXy5WXx5iQjJGezciRnoq13oac0ZyQko-Ki5rRi5nSnJCSj4qLmtKSmouem56LntKMng.iV7VPkc_4QbEM27T5TSniHEModFmIpD6142jnm8AwKuWE0gUIX6jdGJs1fmn4sOn1H9VKesfan9vJDXgOqYfCQ"
folder_ID = 'b1gg4891rufkm43he5im'
MAX_USER_SST_BLOCKS = 12


def speech_to_text(data):
    iam_token = API_KEY
    folder_id = folder_ID
    params = "&".join([
        "topic=general",
        f"folderId={folder_id}",
        "lang=ru-RU"
    ])
    headers = {
        'Authorization': f'Bearer {iam_token}',
    }
    response = requests.post(
        f"https://stt.api.cloud.yandex.net/speech/v1/stt:recognize?{params}",
        headers=headers,
        data=data
    )
    # Читаем json в словарь
    decoded_data = response.json()

    # Проверяем, не произошла ли ошибка при запросе
    if decoded_data.get("error_code") is None:
        return True, decoded_data.get("result")  # Возвращаем статус и текст из аудио
    else:
        return False, "При запросе в SpeechKit возникла ошибка"


if __name__ == "__main__":
    # Укажи путь к аудиофайлу, который хочешь распознать
    audio_file_path = '/Users/alexkobenko/PycharmProjects/4_module/speech-to-text/output.ogg'

    # Открываем аудиофайл в бинарном режиме чтения
    with open(audio_file_path, "rb") as audio_file:
        audio_data = audio_file.read()

    # Вызываем функцию распознавания речи
    success, result = speech_to_text(audio_data)

    # Проверяем успешность распознавания и выводим результат
    if success:
        print("Распознанный текст: ", result)
    else:
        print("Ошибка при распознавании речи: ", result)