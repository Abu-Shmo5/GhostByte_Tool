import json
from lib.gbe import GhostByte

file_name = input("File name: ")
gbe = GhostByte()
response = gbe.upload_file(open(file_name, 'rb'))
print('File name:', json.loads(response['content'])['original_name'])
print('File ext:', json.loads(response['content'])['file_type'])
print('File path:', response['file_link'])
