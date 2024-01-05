import json

input_file_path = r's3://airrflowuserinput/user_input.txt'
output_json_path = 'input.json'

try:
    with open(input_file_path, 'r') as input_file:
        user_data = {}
        for line in input_file:
            if ":" in line:
                key, value = map(str.strip, line.split(':', 1))
                user_data[key] = value
        user_data["index_file"] =input("Enter your true/false:  ").lower()
        user_data["clonal_threshold"] = input("Enter the threshold value: ")
        user_data["umi_length"] = input("Enter the length value: ")
        user_data["umi_position"] = input("Enter your position: ").upper()  
        with open(output_json_path, 'w') as output_json:
            json.dump(user_data, output_json, indent=2)
        print(f"JSON file '{output_json_path}' created successfully.")

except FileNotFoundError:
    print(f"The file '{input_file_path}' does not exist.")
except Exception as e:
    print(f"An error occurred: {e}")