while(True):
    query = input("Enter your query : ")

    if 'bye bye' or 'quit' or 'leave' or 'stop' in query:
        print("Exiting...")
        break
    queryProsses(query)