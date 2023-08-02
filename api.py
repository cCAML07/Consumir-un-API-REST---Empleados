import requests

url = 'https://dummy.restapiexample.com/api/v1/employees'

headers = requests.utils.default_headers()
headers.update({
    'User-Agent': 'My User Agent 1.0',
})

response = requests.get(url, headers=headers)

if response.status_code == 200:
    data = response.json()

    # cantidad de empleados
    total_employees = len(data['data'])

    # promedio de salario de los empleados
    total_salary = sum(float(employee['employee_salary']) for employee in data['data'])
    average_salary = total_salary / total_employees if total_employees > 0 else 0  # Evitar división por cero

    # promedio de edad de los empleados
    total_age = sum(int(employee['employee_age']) for employee in data['data'])
    average_age = total_age / total_employees if total_employees > 0 else 0  # Evitar división por cero

    # salario mínimo y máximo
    salaries = [float(employee['employee_salary']) for employee in data['data']]
    min_salary = min(salaries)
    max_salary = max(salaries)

    # edad mínima y máxima
    ages = [int(employee['employee_age']) for employee in data['data']]
    min_age = min(ages)
    max_age = max(ages)

    # Imprimir los resultados
    print(f"Número de empleados: {total_employees}")
    print(f"Promedio de salario: {round(average_salary, 2)}")
    print(f"Promedio de edad: {round(average_age, 2)}")
    print(f"Salario mínimo: {min_salary}")
    print(f"Salario máximo: {max_salary}")
    print(f"Edad menor: {min_age}")
    print(f"Edad mayor: {max_age}")

else:
    print("Error al obtener los datos de empleados. Código de estado:", response.status_code)



