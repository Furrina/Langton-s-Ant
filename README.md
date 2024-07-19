# Langton's Ant
This is my implementation of multiple-color extension of Langton's ant (cellular automaton) using python. The visualization is done using the pygame module.

## About
*Langton's ant is a two-dimensional Turing machine with a very simple set of rules but complex emergent behavior.*

## Rules
Squares on a plane are colored variously either black or white. We arbitrarily identify one square as the "ant". The ant can travel in any of the four cardinal directions at each step it takes. The "ant" moves according to the rules below:

- At a white square, turn 90° clockwise, flip the color of the square, move forward one unit
- At a black square, turn 90° counter-clockwise, flip the color of the square, move forward one unit
