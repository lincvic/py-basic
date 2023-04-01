import csv


# 将csv读取为List
def csv_loader(csv_path: str) -> list:
    csv_data_list = []
    with open(csv_path, "r", encoding="utf-8") as f:
        csv_data_dict = csv.DictReader(f)
        for item in csv_data_dict:
            csv_data_list.append(item)

    return csv_data_list


def csv_writer(csv_path: str, data: list[dict]):
    headers = data[0].keys()
    with open(csv_path, "w", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=headers)
        writer.writeheader()
        for item in data:
            writer.writerow(item)


if __name__ == '__main__':
    example_data = [{'Name': 'A', 'Score': '98'}, {'Name': 'B', 'Score': '76'}, {'Name': 'C', 'Score': '89'}, {'Name': 'D', 'Score': '80'}, {'Name': 'E', 'Score': '34'}, {'Name': 'F', 'Score': '90'}]

    csv_writer("new.csv", example_data)
    print(csv_loader("new.csv"))
