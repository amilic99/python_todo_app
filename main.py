from fastapi import FastAPI
import uvicorn

app=FastAPI()

class Item:
    
    def __init__(self, name:str, done:bool = False):
        self.name=name
        self.done=done

todo_items = []

@app.post("/createItem/")
def createItem(name):
    item = Item(name)
    todo_items.append(item)
    return("Item " + item.name + " has been added to the TO DO list.") 

@app.put("/updateItem/")
def updateItem(name, index:int):
    oldname = todo_items[index-1].name
    todo_items[index-1].name = name
    return("Changed name from " + oldname + " to " + name + " for item at index " + str(index))

@app.put("/changeDoneFlag/")
def changeDoneFlag(index:int):
    if todo_items[index-1].done == True:
        todo_items[index-1].done = False
    else: todo_items[index-1].done = True
    return("Updated whether item " + todo_items[index-1].name + " is done or not.")

@app.delete("/deleteItem/")
def deleteItem(index:int):
    oldname = todo_items[index-1].name
    todo_items.remove(todo_items[index-1])
    return("Item " + oldname + " removed from list!")

@app.get("/getItems/")
def getItems():
    return_list = []
    for i in range(0, len(todo_items)):
        return_list.append(str(i+1) +": " + todo_items[i].name +" - Done:"+ str(todo_items[i].done))
    return return_list

if __name__ == '__main__':
    uvicorn.run("main:app", host="127.0.0.1", port=5000, log_level="info")

