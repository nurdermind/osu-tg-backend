# Бекенд сервисы для проекта "Адаптивный интерфейс"
### *(сделано для ОГУ)


## Сервис для преобразования речи в текст

### Сборка:
```shell
docker build . -t osu/voiceai
```
### Запуск:
```shell
docker run -p 8000:8000 osu/voiceai
```

### Примеры запросов

#### CURL
```shell
curl --location 'http://localhost:8000/speech-to-text/' \
--form 'file=@"~/Запись-2.wav"
```

#### Python
```python
import requests

url = "http://localhost:8000/speech-to-text/"

payload = {}
files = [
    ('file',
    ('Запись 2.flac', open('/home/Запись-2.wav', 'rb'), 'application/octet-stream'))
]
headers = {}

response = requests.request("POST", url, headers=headers, data=payload, files=files)

print(response.text)
```

#### C#
```cs
var options = new RestClientOptions("http://localhost:8000")
{
  MaxTimeout = -1,
};
var client = new RestClient(options);
var request = new RestRequest("/speech-to-text/", Method.Post);
request.AlwaysMultipartFormData = true;
request.AddFile("file", "/home/Запись-2.wav");
RestResponse response = await client.ExecuteAsync(request);
Console.WriteLine(response.Content);
```
