from src.front import IHM

# Create the application
if __name__ == "__main__":
    app = IHM.IHM()
    #app.mainloop()
    for key, value in IHM.sc.users_dico.items():
        print(key, value)
    print(IHM.sc.dijkstra("user1"))
