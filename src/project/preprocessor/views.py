import csv
from django.http import HttpResponse
from project.dashboard.models import Dataset

# class PreProcessor():
def test_save_data(request):
    save_data('DOF', 'url', 'desc', '/src/project/preprocessor/dof.csv')
    return HttpResponse('OK')

def save_data(name, url, desc, data_file):
    json_data = format_csv(data_file)

    dataset = Dataset(name=name, url=url, description=desc, chart_type='bar', rating=0, popularity=0, score=0, data=json_data)
    dataset.save()

def format_csv(csv_file):
    json_data = {}

    with open(csv_file) as f:
        reader = csv.reader(f, delimiter=',')

        row_num = 0
        for row in reader:
            # row = unicode(str, errors='ignore')
            # print(row)
            if row_num == 0:
                label_row = []
                for item in row:
                    label_row.append(item)

                json_data['labels'] = label_row
                json_data['series'] = []

            else:
                item_counter = 0
                class_name = ""
                name = ""
                data = []

                for item in row:
                    if item_counter == 0:
                        class_name = str(item)
                        name = str(item)
                    else:
                        data.append(item)

                    item_counter += 1
                
                json_data['series'].append({
                    'className': class_name,
                    'name': name,
                    'data': data
                })

            row_num += 1

    return json_data

# preprocessor = PreProcessor()
# preprocessor.format_csv('DOF', 'url', 'desc', 'dof.csv')
