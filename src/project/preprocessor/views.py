import csv
from django.http import HttpResponse
from project.dashboard.models import Dataset

# class PreProcessor():
def test_save_data(request):
    save_data(
        'Internal Revenue Allotment - Region V', 
        'https://data.gov.ph/sites/default/files/albay_legazpi_city_ira_utilization_122012_q4.csv', 
        'This dataset contains the quarterly submitted of the utilization of Special Development Funds documents of Region V',
        'Finance',
        'DILG',
        'bar',
        3,
        250,
        8,
        '/src/project/preprocessor/datasets/albay_legazpi_city_ira_utilization_122012_q4.csv'
    )

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

    save_data(
        'Metro Rail Transit Line 3 - Passenger Traffic (Saturdays)', 
        'https://data.gov.ph/sites/default/files/2011_saturdays_ave.csv',
        'This dataset contains the saturdays number of passengers who have entered and exited per station by average, percentage and total in MRT Line 3',
        'Transportation',
        'MRT Line 3',
        'line',
        5,
        7384,
        1,
        '/src/project/preprocessor/datasets/2011_saturdays_ave.csv'
    )

    save_data(
        'Climatological Normal Values', 
        'https://data.gov.ph/sites/default/files/pagasanormvalalabatquez1999-2010.csv',
        'Period averages computed for a uniform and relative long period comprising at least three (3) consecutive 10-year period.',
        'Environment',
        'PAGASA',
        'bar',
        4,
        4125,
        8,
        '/src/project/preprocessor/datasets/pagasanormvalalabatquez1999-2010.csv'
    )

    save_data(
        'Administration of Probation Systems and Parole Systems', 
        'https://data.gov.ph/sites/default/files/ppa_pardon_supervision_caseload_1989-2013.csv',
        'This dataset contains the total number of investigation of court referrals for the applicant or petitioner for probation. The post-sentence investigation is conducted to provide the courts with relevant information and judicious recommendations for the selection of offenders to be placed on probation. It also includes number pre-parole/executive clemency investigation conducted to provide the Board (Board of Pardons and Parole) with necessary and relevant information which it can use in determining a prisoner’s fitness for parole or any form of executive clemency. Moreover, it contains the number of probationers, parolees, and pardonees supervised by the Agency to effect the rehabilitation and reintegration of these clients (i.e.,probationers, parolees, and pardonees) as productive, law-abiding and socially responsible members of the community. It also shows the Courts\' and Boards\' actions on the investigation and supervision reports submitted to them by the Agency.',
        'Justice',
        'Parole and Probation Administration',
        'bar',
        5,
        52389,
        9,
        '/src/project/preprocessor/datasets/ppa_pardon_supervision_caseload_1989-2013.csv'
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
