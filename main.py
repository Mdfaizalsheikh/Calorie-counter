import json 

def load_food_database(filename):
  with open (filename, 'r') as file:
    return json.load(file)

def calc_nutrition (food_database,food_items ):
  total_nutrition={
    "calories":0, 
    " protein":0, 
    "carbs":0, 
    " fat":0, 
    
  }
  for item in food_items:
      food, quantity = item["food"], item["quantity"]
      if food in food_database:
          total_nutrition["calories"] += food_database[food]["calories"] * quantity
          total_nutrition["protein"] += food_database[food]["protein"] * quantity
          total_nutrition["carbs"] += food_database[food]["carbs"] * quantity
          total_nutrition["fat"] += food_database[food]["fat"] * quantity
      else:
          print(f"Warning: {food} not found in the database")

  return total_nutrition

def main():
  food_database=load_food_database('food_database.json')
  food_items=[]
  while True:
    food=input("Enter food item (or 'done' to finish : )").strip().lower() 
    if food=='done':
      break
    quantity=float(input("Enter quantity: "))
    food_items.append({" food":food, 'quantity':quantity})

  total_nutrition = calc_nutrition(food_database, food_items)
  print("\nTotal Nutritional Values:")
  print(f"Calories: {total_nutrition['calories']:.2f}")
  print(f"Protein: {total_nutrition['protein']:.2f}g")
  print(f"Carbs: {total_nutrition['carbs']:.2f}g")
  print(f"Fat: {total_nutrition['fat']:.2f}g")

if __name__ =="__main__" :
  main()



    



