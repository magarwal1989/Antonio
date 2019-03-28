from util.json_parser import parse_json_from_file
import json
import os
from conftest import get_test_data_directory
file_path = os.path.join(get_test_data_directory(),"construction_quote.json")
data = parse_json_from_file(file_path)
item_dict = json.loads(file_path)
print (item_dict)
