# from fastapi import FastAPI, HTTPException
# from sqlmodel import Session, select
# from config.db import create_tables, engine
# from models.todos import Todo, UpdateTodo
# import uvicorn

# # Initialize FastAPI app
# app = FastAPI()

# # Create tables on startup
# @app.on_event("startup")
# def on_startup():
#     create_tables()

# @app.get('/get_todos')
# def get_todos():
#     with Session(engine) as session:
#         statement = select(Todo)
#         result = session.exec(statement)
#         data = result.all()
#         return data

# @app.post("/create_todos")
# def create_todos(todo: Todo):
#     with Session(engine) as session:
#         # Ensure 'id' is not manually set
#         new_todo = Todo(
#             title=todo.title,
#             description=todo.description,
#             completed=todo.completed
#         )
#         session.add(new_todo)
#         session.commit()
#         session.refresh(new_todo)
#         return {"status": 200, "message": "todo created successfully"}

# @app.put("/update_todo/{id}")
# def update_todo(id: int, todo: UpdateTodo):
#     with Session(engine) as session:
#         db_todo = session.get(Todo, id)
#         if not db_todo:
#             raise HTTPException(status_code=404, detail="todo not found")
#         update_data = todo.dict(exclude_unset=True)
#         for key, value in update_data.items():
#             setattr(db_todo, key, value)
#         session.add(db_todo)
#         session.commit()
#         session.refresh(db_todo)
#         return {"status": 200, "message": "todo updated successfully"}

# @app.delete("/delete_todo/{todo_id}")
# def delete_todo(todo_id: int):
#     with Session(engine) as session:
#         db_todo = session.get(Todo, todo_id)
#         if not db_todo:
#             raise HTTPException(status_code=404, detail="todo not found")
#         session.delete(db_todo)
#         session.commit()
#         return {"status": 200, "message": "todo deleted successfully"}

# def start():
#     uvicorn.run("main:app", host="127.0.0.1", port=8080, reload=True)

# if __name__ == "__main__":
#     start()

import phonenumbers
from phonenumbers import geocoder, carrier

def get_phone_number_info(phone_number):
    try:
        # Parse the phone number
        parsed_number = phonenumbers.parse(phone_number)

        # Get location information
        location = geocoder.description_for_number(parsed_number, "en")

        # Get carrier information
        phone_carrier = carrier.name_for_number(parsed_number, "en")

        return location, phone_carrier
    except phonenumbers.phonenumberutil.NumberParseException as e:
        return str(e), None

# Replace this with the phone number you want to check
phone_number = input("Enter the phone number: ")

# Get phone number information
location, phone_carrier = get_phone_number_info(phone_number)

# Print the information
if phone_carrier:
    print(f"Phone number: {phone_number}")
    print(f"Location: {location}")
    print(f"Carrier: {phone_carrier}")
else:
    print(f"Error: {location}")