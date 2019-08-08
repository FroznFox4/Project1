from requests import post
import json
import argparse
import base64
from ReadFromWindow import new_image_string
from ParsOnText import ParsOnText

# Функция возвращает IAM-токен для аккаунта на Яндексе.
def get_iam_token(iam_url, oauth_token):
    response = post(iam_url, json={"yandexPassportOauthToken": oauth_token})
    json_data = json.loads(response.text)
    if json_data is not None and 'iamToken' in json_data:
        return json_data['iamToken']
    return None

# Функция отправляет на сервер запрос на распознавание изображения и возвращает ответ сервера.
def request_analyze(vision_url, iam_token, folder_id, image_data):
    response = post(vision_url, headers={'Authorization': 'Bearer '+ iam_token}, json={
        'folderId': folder_id,
        'analyzeSpecs': [
            {
                'content': image_data,
                'features': [
                    {
                        'type': 'TEXT_DETECTION',
                        'textDetectionConfig': {'languageCodes': ['en', 'ru']}
                    }
                ],
            }
        ]})
    return response.text


def MainYandex():
    iam_url = 'https://iam.api.cloud.yandex.net/iam/v1/tokens' 

    oauth_token = "AgAAAAAGg6eyAATuwWwJRFQmXUwDp4RCH-96fRc" 

    iam_token = get_iam_token(iam_url, oauth_token)
    
    vision_url = 'https://vision.api.cloud.yandex.net/vision/v1/batchAnalyze'

    folder_id="b1gneif5vbojdoubsq1d"

#    iam_token = "CggaATEVAgAAABKABGpvdJWrMiN0GIJtioMMmFcbtp8oIyD15ply3SU8iLfpSS8yabiP2U8ar1vYibjhCbmbLcwQZu12fLA3wtelEAFb6WiHyMtpXIKsStx3w9K0QVfW9n-6CEzrbzeIpfdRgcCH6oonbDJusNPYePXJ-bfXGqAXcVJVsBJ8W1WKmy1LRJdIZh3stv9dP23-334JnnlO0Hna2uKrb_wwuKruBu1P_EFECnn8f11N8UllADo5MbD5YFdvRhLCHvsAaAPH0lzwGadUDSqvU1OmZOMZqGNktgmiKUIH7QJpYb-879VZtEFtCm7TVSBAKPZCDF_kBPDEymLZY5foRWvb0nTrI9-7XspfCdyoUVcH9fGyni5d7NtFtydsv9Vyuf0EQUcCv8cJ03SZWZZXze63i785VUq1rYoCc12j_Qo8Qela_RWNnsDWTw0Va0rzk9csN0vhUz9aYnpJhb-F0i_T0NCrABsBGShAauhz20FgEaUgrQ7NdA0GwTFApJ6zsCQfzc1o0YMhUS7C2YDQ9RmTTbe1PRr5s4qNx8vVuJ-whdz0aeKUdgPVOOdxyGXFxhpkDY8ykHgQMWeFr6MomppHrXAf8qwt6Ob__rehJYEVV8iOcAxb9ust3gaobxv-QRspyRnNLvWrp7fa-iWqB2nwdXL0bRz6be6B--Qjg8PRbbyVkixxGmYKIGYyMjM1M2EwMzBlODRkYWFhNjY0ODJiZjUzMjMzMGE2EJCmpuoFGND3qOoFIiQKFGFqZTJ2b2VyZWc3aHNidmgwbjFhEgx0YWtzaGVldi5rcmlaADACOAFKCBoBMRUCAAAAUAEg9QQ"
    
    image_data = new_image_string()
    
    response_text = request_analyze(vision_url, iam_token, folder_id, image_data)
#    with open('output.json', 'w') as f:
#        f.write(response_text)
    print(ParsOnText(response_text))
    

if __name__ == '__main__':
    MainYandex()        
