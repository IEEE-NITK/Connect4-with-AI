
<p style="color: red; font-weight: bold">>>>>>  gd2md-html alert:  ERRORs: 0; WARNINGs: 0; ALERTS: 4.</p>
<ul style="color: red; font-weight: bold"><li>See top comment block for details on ERRORs and WARNINGs. <li>In the converted Markdown or HTML, search for inline alerts that start with >>>>>  gd2md-html alert:  for specific instances that need correction.</ul>

<p style="color: red; font-weight: bold">Links to alert messages:</p><a href="#gdcalert1">alert1</a>
<a href="#gdcalert2">alert2</a>
<a href="#gdcalert3">alert3</a>
<a href="#gdcalert4">alert4</a>

<p style="color: red; font-weight: bold">>>>>> PLEASE check and correct alert issues and delete this message and the inline alerts.<hr></p>


**Minimax Algorithm:**

This was used to implement the single player version of the game, i.e, the user playing against the computer. The minimax algorithm explores all possible moves in a game tree upto a specific depth and returns the most favourable move to the computer.

**Concept:**



<p id="gdcalert1" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image1.png). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert2">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![gametree](images/gametree.png "image_tooltip")



            (image source: wikipedia)

The core concept of this algorithm can be explained using this game tree.

At each level the maximum/minimum value of the child nodes is chosen depending on whether the player is maximizing or minimizing. For example, at level 3, the first node is assigned 10 over infinity as it is the minimizing player’s move. At level 2 the first node is assigned 10 over 5 as it is the maximizing player’s move. In this fashion the algorithm assigns values to all nodes of the game tree upto a specific depth using depth first search and recursion. The value assigned to the root node represents the most favourable move the computer can make.

**Implementation:**



<p id="gdcalert2" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image2.png). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert3">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![minmaxcode](images/minmaxcode.png "image_tooltip")


The minimax algorithm in our game is implemented using the recursive minimax function which takes the depth, maximizing player and number of moves as parameters and it returns the most favourable column according to the highest score. In case the maximizing player has won, the function returns the maximum possible value infinity and returns negative infinity if the minimizing player has won. In case the game is a draw, zero is returned. In case the depth passed to the function is zero then the overall score calculated for the current board by the score_move function is returned. In all of these cases no column is returned since no further moves can be checked by the function. All these cases form the base cases of the function.

In case none of these conditions are satisfied, the function checks whether the player passed to it is the maximizing player or not and gets a list of all the valid columns where moves can be made using the valid_cols function. If the player is maximizing, the initial value is set to negative infinity. Then a loop is run considering all possible moves by dropping the token in each column one by one. The minimax function is then called on it’s child node and the score obtained is compared with the current value. The maximum of these two is set to be the value for the next iteration. The maximum value obtained after iterating through all columns, i.e, after going through all moves and the column which gave that value, i.e, the move which yielded that value is then returned. In case the player is minimizing the initial value is set to positive infinity and a similar loop is run considering all possible moves and the least value obtained after iterating through all columns and the respective column which yielded that value are returned.

The overall score is evaluated using the evaluate and score_move functions. The score_move function checks each row, column, positive and negative diagonals for the tokens present in them in windows of 4 slots each. Each window is passed to the evaluate function which returns the score of a particular window. The center column is also given priority in this function since it is easier to construct rows, columns and diagonals of four using tokens from the central column.The overall score of a particular move after considering all possible windows is then calculated and returned.



<p id="gdcalert3" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image3.png). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert4">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![score_move_code](images/score_move_code.png "image_tooltip")


The evaluate function assigns  scores for a window passed to it depending on how many maximizing and minimizing tokens along with empty slots are present in the window, i.e, how favourable it is for the given player, and returns the score of that particular window.



<p id="gdcalert4" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image4.png). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert5">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![evaluatecode](images/evaluatecode.png "image_tooltip")

