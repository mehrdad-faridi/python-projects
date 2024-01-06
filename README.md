# python-projects
This repository includes all my Python projects.

### 1. Tic_Tac_Toe_Game
> Tic-tac-toe, noughts and crosses, or Xs and Os is a paper-and-pencil game for two players who take turns marking the spaces in a three-by-three grid with X or O. The player who succeeds in placing three of their marks in a horizontal, vertical, or diagonal row is the winner. 

you can find python code in `main.py` file.
Also, provided Dockerfile to bring the application up in container.


<br><br>

```bash
# To dockerize the app, run below command:

cd Tic_Tac_Toe_Game
docker build -t tictactoe-game -f Dockerfile .

# To run the docker you built:
docker run --rm -it tictactoe-game
```
