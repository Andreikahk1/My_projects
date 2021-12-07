import sqlite3
import sys
class NameExc(Exception):
    def __init__(self, head="TODOTaskNameError", message="Bad name!"):
        super().__init__(message)
        self.head = head
        self.message = message

class PriorityExc(NameExc):
    def __init__(self, head="TODOPriorityError", message="Bad priority!"):
        super().__init__(message)
        self.head = head
        self.message = message

class IdExc(NameExc):
    def __init__(self, head="TODOIdError", message="Bad Id number!"):
        super().__init__(message)
        self.head = head
        self.message = message

class Todo:
    def __init__(self):
        self.conn = sqlite3.connect('todo.db')
        self.c = self.conn.cursor()
        self.create_task_table()

    def create_task_table(self):
        self.c.execute('''CREATE TABLE IF NOT EXISTS tasks(id integer primary key, name text not null, priority integer not null);''')
    
    def add_task(self):
        name = input('Enter task name: ')
        if len(name) == 0 or name.isspace():
            raise NameExc
        
        priority  = int(input('Enter task priotity: '))
        if priority < 1:
            raise PriorityExc
        
        self.c.execute('INSERT into tasks (name,priority) VALUES (?,?)', (name,priority))
        self.conn.commit()
    
    def show_tasks(self):
        print("List of tasks:")
        print("ID        | Task Name            | Priority")
        for row in self.c.execute('''SELECT * from tasks;'''):
            print(row)

    def find_task(self, task_name):
        self.task_name = task_name
        res = False
        query = '''SELECT id, name, priority from tasks;'''
        rows = self.c.execute(query)
        for row in rows:
            if row[1] ==self.task_name:
                res = True
            return row
        else:
            return None

    def update_priority(self):
        priority = int(input('Enter new priority: '))
        if priority < 1:
            raise PriorityExc
        numid = int(input('Enter id: '))
        if numid < 1:
            raise IdExc
        query = '''UPDATE tasks SET priority = ? WHERE id = ?;'''
        self.c.execute(query,(priority,numid))
        self.conn.commit()

    def delete_task(self):
        numid = int(input('Enter id which you want to delete: '))
        if numid < 1:
            raise IdExc
        self.c.execute('''DELETE FROM tasks WHERE id = ?;''',(numid,))
        self.conn.commit

    def exit(self):
        pass

def main():
    def menu_controller(put = 0):
        if put == 1: # show task 
            app.show_tasks()
        elif put == 2: # add task 
            try:
                app.add_task()
            except NameExc as e:
                print(e.message)
            except PriorityExc as e:
                print(e.message)
            except:
                print("Something went wrong")
            else:
                print("Task has been added successfully.")
            finally:
                print()
        elif put == 3: # update priority
            try:
                app.update_priority()
            except NameExc as e:
                print(e.message)
            except PriorityExc as e:
                print(e.message)
            except IdExc as e:
                print(e.message)
            except:
                print("Something went wrong")
            else:
                print("Task priority has been updated successfully.")
            finally:
                print()
        elif put == 4: # delete task
            try:
                app.delete_task()
            except IdExc as e:
                print(e.message)
            except:
                print("Seomthing went wrong")
            else:
                print("Task was deleted successfully.")
            finally:
                print()
        elif put == 5: # exit
            app.exit()
        else:
            pass

    app = Todo()
    while True:
        print('''
1. Show Tasks
2. Add Task
3. Change Priority
4. Delete Task
5. Exit''')
        try:
            put = int(input("Select option 1-5: "))
            if put == 5:
                # menu_controller(put)
                break
        except:
            print("Bad operation")
        else:
            if put in [1,2,3,4]:
                menu_controller(put)

main()