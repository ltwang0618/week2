def calculate_sum_of_bonus(data):
    allSalary = 0
    roleBonus = 0
    baseBonus = 0
    performanceBonus = 0
    calSum=0

    for object in data["employees"]:
        defSalary = str(object["salary"])
        Salary1 = 0
        Salary2 = 0
        Salary3 = 0

        if "USD" in defSalary:
            Salary1 = int(defSalary.replace("USD", "")) * 30
        elif "," in defSalary:
            Salary2 = int(defSalary.replace(",", ""))
        else:
            Salary3 = int(defSalary)

        allSalary = (Salary1 + Salary2 + Salary3) * 0.02
        baseBonus += allSalary

        if object["performance"] == "above average":
            calSum=2000
            performanceBonus += calSum
        elif object["performance"] == "average":
            calSum=1000
            performanceBonus += calSum
        elif object["performance"] == "below average":
            calSum=600
            performanceBonus += calSum

        if object["role"] == "Engineer":
            roleBonus = baseBonus * 0.8
        elif object["role"] == "CEO":
            roleBonus = baseBonus * 1
        elif object["role"] == "Sales":
            roleBonus = baseBonus * 0.4

    totalbonus = baseBonus+ performanceBonus + roleBonus
    print("Total bonus of all employees:", totalbonus, "TWD")

calculate_sum_of_bonus({
    "employees": [
        {
            "name": "John",
            "salary": "1000USD",
            "performance": "above average",
            "role": "Engineer"
        },
        {
            "name": "Bob",
            "salary": 60000,
            "performance": "average",
            "role": "CEO"
        },
        {
            "name": "Jenny",
            "salary": "50,000",
            "performance": "below average",
            "role": "Sales"
        }
    ]
})

