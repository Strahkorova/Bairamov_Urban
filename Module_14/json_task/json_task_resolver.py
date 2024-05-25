import json


def employees_rewrite(sort_type):
    if sort_type.lower() not in ['firstname', 'lastname', 'department', 'salary']:
        raise ValueError('Bad key for sorting')

    with open('employees.json', 'r') as file:
        data = json.load(file)

    for employee in data['employees']:
        employee_lower = {key.lower(): value for key, value in employee.items()}
        employee.clear()
        employee.update(employee_lower)

    sorted_data = sorted(data['employees'], key=lambda x: x[sort_type.lower()])

    with open(f'employees_{sort_type.lower()}_sorted.json', 'w') as sorted_file:
        json.dump({'employees': sorted_data}, sorted_file, indent=4)


if __name__ == '__main__':
    employees_rewrite('department')
    employees_rewrite('lastName')
    employees_rewrite('firstName')
