def calculate_sum_of_bonus(data):
    total_bonus = 0
    employees = data['employees']

    for employee in employees:
        name = employee['name']
        salary = employee['salary']
        performance = employee['performance']
        role = employee['role']
        bonus = individual_bonus(salary, performance, role)
        employee['bonus'] = bonus
        total_bonus += bonus
        
        def get_salary(salary):
            if isinstance(salary, str):
                if "USD" in salary:
                    return float(salary.replace("USD", "")) * 30
                else:
                    return float(salary)
            elif isinstance(salary, (int, float)):
                return salary
            else:
                return 0

            def individual_bonus(salary, performance, role):
                base_bonus = get_salary(salary) * 0.02

                performance_bonus = 0
                if performance == "above average":
                    performance_bonus = 2000
                elif performance == "average":
                    performance_bonus = 1000
                elif performance == "below average":
                    performance_bonus = 600

                role_bonus = 0
                if role == "Engineer":
                    role_bonus = base_bonus * 1.2
                elif role == "CEO":
                    role_bonus = base_bonus * 1.5
                elif role == "Sales":
                    role_bonus = base_bonus * 1

                return base_bonus + performance_bonus + role_bonus
                

                print("Total bonus of all employees:", total_bonus, "TWD")


        calculate_sum_of_bonus({
            "employees":[
                {
                    "name":"John",
                    "salary":"1000USD",
                    "performance":"above average",
                    "role":"Engineer"
                },
                {
                    "name":"Bob",
                    "salary":60000,
                    "performance":"average",
                    "role":"CEO"
                },
                {
                    "name":"Jenny",
                    "salary":"50,000",
                    "performance":"below average",
                    "role":"Sales"
                }
            ]
        }) # call calculate_sum_of_bonus function