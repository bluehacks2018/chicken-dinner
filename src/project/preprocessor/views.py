import csv
from django.http import HttpResponse
from project.dashboard.models import Dataset

# class PreProcessor():
def test_save_data(request):
    # save_data(
    #     'Internal Revenue Allotment - Region V', 
    #     'https://data.gov.ph/sites/default/files/albay_legazpi_city_ira_utilization_122012_q4.csv', 
    #     'This dataset contains the quarterly submitted of the utilization of Special Development Funds documents of Region V',
    #     'Finance',
    #     'DILG',
    #     'bar',
    #     3,
    #     250,
    #     8,
    #     '/src/project/preprocessor/datasets/albay_legazpi_city_ira_utilization_122012_q4.csv'
    # )

    save_data(
        'State University and Colleges - Faculty-Student Ratio', 
        'https://data.gov.ph/sites/default/files/State%20Universities%20and%20Colleges%20Faculty-Student%20Ratio%20AY%202016-17.csv', 
        'This dataset contains State Universities and College (SUCs) Faculty Student Ratio',
        'Education',
        'CHED',
        'bar',
        2,
        501,
        10,
        '/src/project/preprocessor/datasets/State Universities and Colleges Faculty-Student Ratio AY 2016-17.csv'
    )

    # save_data(
    #     'Balance Sheet and Key Ratios - Philippine Banking System', 
    #     'https://data.gov.ph/sites/default/files/bsp_balance_sheet_key_ratios_2014.csv', 
    #     'Balance Sheet/Consolidated Statement of Condition and Key Ratios of Philippine Banking System (PBS)',
    #     'Business',
    #     'BSP',
    #     'bar',
    #     5,
    #     1000000,
    #     10,
    #     '/src/project/preprocessor/datasets/bsp_balance_sheet_key_ratios_2014.csv'
    # )

    # save_data(
    #     'NSCB Health Expenditure by Source of Funds', 
    #     'https://data.gov.ph/sites/default/files/nscb_health_expenditure_by_source_of_funds_2009-2011.CSV', 
    #     'This dataset contains NSCB Health Expenditure by source of funds. *Amount in million pesos.',
    #     'Health',
    #     'PSA',
    #     'bar',
    #     4,
    #     684253,
    #     7,
    #     '/src/project/preprocessor/datasets/nscb_health_expenditure_by_source_of_funds_2009-2011.csv'
    # )

    save_data(
        'NSCB Awareness of Laws providing protection to Land', 
        'https://data.gov.ph/sites/default/files/nscb_awareness_of_laws_providing_protection_to_land_2012.csv',
        'This dataset contains NSCB Awareness of Laws providing protection to Land. Percent of Respondents Aware of Laws. Total may exceed one hundred percent due to multiple responses',
        'Environment',
        'PSA',
        'bar',
        4,
        572,
        5,
        '/src/project/preprocessor/datasets/nscb_awareness_of_laws_providing_protection_to_land_2012.csv'
    )

    # save_data('DOF', 'url', 'desc', '/src/project/preprocessor/datasets/dof.csv')
    return HttpResponse('OK')

def save_data(name, url, desc, tag, gov_org, chart_type, rating, popularity, score, data_file):
    json_data = format_csv(data_file)

    dataset = Dataset(name=name, url=url, description=desc, tag=tag, gov_org=gov_org, chart_type=chart_type, rating=rating, popularity=popularity, score=score, data=json_data)
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
