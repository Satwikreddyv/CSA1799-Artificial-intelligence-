% Facts representing fruits and their colors.
fruit_color(apple, red).
fruit_color(banana, yellow).
fruit_color(grape, purple).
fruit_color(orange, orange).
fruit_color(watermelon, green).

% Predicate to find the color of a fruit using backtracking.
find_fruit_color(Fruit, Color) :-
    fruit_color(Fruit, Color).

% Predicate to find fruits of a specific color using backtracking.
find_color_fruit(Color, Fruit) :-
    fruit_color(Fruit, Color).

% Example queries:
% To find the color of an apple, use: find_fruit_color(apple, Color).
% To find a fruit that is red, use: find_color_fruit(red, Fruit).
% To find all fruits and their colors, use: find_fruit_color(Fruit, Color).
% To find all fruits that are red, use: find_color_fruit(red, Fruit).
