import json
import requests

class GhostByte:
    file_upload_api_link = "https://gbe.lol/upload.php"
    
    def upload_file(self, file_bytes):
        response = requests.post(self.file_upload_api_link, data={"captcha_original": "do you love me?", "captcha_input": "do you love me?"}, files={"file": file_bytes})
        try:
            return {'status_code': response.status_code, 'content': response.content, 'file_link': json.loads(response.content)['downloadLink']}
        except:
            print(response.status_code)
            print(response.headers)
            print(response.content)

if __name__ == "__main__":

    # # Upload File Test ( Bypass Captcha )
    # gbe = GhostByte()
    # print(gbe.upload_file(open('../test/test.txt', 'rb')))

    # # Upload File Test ( Bypass Max Upload Size )
    # gbe = GhostByte()
    # print(gbe.upload_file(open('../test/above_50mb_test.mp4', 'rb')))


    pass