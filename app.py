def calculate_restaurant_bill(meal_cost,people):
    
    service_charge = 10 / 100 * meal_cost
    Amount_service = meal_cost + service_charge
    Tax = 5 / 100 * Amount_service
    Tip = 5 / 100 * Amount_service
    Total_bill = Amount_service + Tax + Tip
    Amount_per_person = Total_bill / people
    print(f'Meal Cost {meal_cost}')
    print(f'Service charge (10%): {service_charge}')
    print(f'Amount after service: {Amount_service}')
    print(f'Tax (5%): {Tax}')
    print(f'Tip (5%) {Tip}')
    print(f'Total Bill: {Total_bill}')
    print(f'Amount per person: {Amount_per_person}')
      
meal_cost = float(input(f"Enter the meal cost:"))
people = int(input("Emter number of people: "))

calculate_restaurant_bill(meal_cost)
