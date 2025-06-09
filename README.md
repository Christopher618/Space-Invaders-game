# Space Invader
#### Video Demo: <https://www.youtube.com/watch?v=i_XogIWox9A>
#### Description: 

This project was initially supposed to be a chess game. 
After watching many tutorials on how to, I realized that the Pygame library was the common denominator of all those videos. So I started working on learning Pygame which I believe took me one week. Later on, I came across a FreeCodeCamp crash course video where they were explaining some of Pygame functionality while building a Space Invader game. That's where the idea for my final project came from.

The project file (project.py) contains all the codes needed to create this game.
I began by creating a basic screen and I chose the designs for my spacecraft and aliens. Then, I gave each element their positioning and drew them on the screen with different functions such as "player" and "enemy". After setting that up, I called them in a while loop inside my "main" function so that they would continuously be called.

In the next step, I needed to add movement since a game is not functional without the possibility to move your player. I used a combination of logic to create the idea of movement and if statements to make the movement possible. It was definitely more easy to do because there was no need for gravity in this game, knowing that It was suppose to be a space oriented game. I also added boundaries so the elements do not go out of bounds. 

However, can we name a game "Space Invader" while not being able to defend yourself against those invaders ? I don't believe that. I proceeded to define a "Fire_bullet" function with the purpose to draw the bullet on the screen and having a state of either "ready" or "fire". Using the state I made it possible to fire only one bullet at the time. Next, I coded the logic behind the bullet movement when it's fired and I also added some boundaries.

To wrap things up, I added sound effects and background music to the game. Additionally, I established the conditions for the game to be over and added a score element that count how many invaders the player have defeaded.

This project taught me a lot about Pygame, considering that I was completely new to it. It also helped me deepen my understanding of the basic of python, among others, while loop and if statement. To conclude, It was a fun and challenging project that I am really proud of.
