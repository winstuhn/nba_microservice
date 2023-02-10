# nba_microservice
NBA microservice implementation for Tony Liu

Hey Tony, 
Here's the microservice for your NBA CLI program.

Instructions on how to request data from the service:

1. Run the program in a terminal using the command: py random_player.py
2. Your application will need to make a request to the text file: generate_player.txt
3. Write a request using flags. The flags must be comma-seperated and lower-case in this order:

    g,s,e,p,XXXX
    - g (required) = generates a random NBA or ABA player name
    - s (optional) = adds the date player first played in the league to the response 
    - e (optional) = adds the date player last played in the league to the response
    - p (optional) = adds position of the player to the response
    - XXXX (optional) = adds a filter, filters for players that played in that specific year
    
        NOTE: there is no error-checking for the year, so it must be a valid year.
        
    example requests and responses:
    
    g ['Draymond Green']
    
    g,s ['Draymond Green', '2013']
    
    g,s,e ['Draymond Green', '2013', '2023']
    
    g,s,e,p ['Draymond Green', '2013', '2023', 'F']
    
    g,s,e,p,2020 ['Draymond Green', '2013', '2023', 'F']

4. Response will be made to the same text file: generate_player.txt
    - Responses will be made as comma-seperated lists

Here's the UML Diagram
![image](https://user-images.githubusercontent.com/95652335/217966380-37fc0549-957f-4776-a747-602881a29c5b.png)

