def find_and_print(messages):
    older = []
    
    for person, age in messages.items():
        keywords = ["18 years old", "legal age", "vote"]
        
        for keyword in keywords:
            if keyword in age:
                older.append(person)
                break
    
    for person in older:
        print(person)

find_and_print({
    "Bob": "My name is Bob. I'm 18 years old.",
    "Mary": "Hello, glad to meet you.",
    "Copper": "I'm a college student. Nice to meet you.",
    "Leslie": "I am of legal age in Taiwan.",
    "Vivian": "I will vote for Donald Trump next week",
     "Jenny": "Good morning."
})