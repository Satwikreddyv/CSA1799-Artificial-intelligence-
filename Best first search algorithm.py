% Facts representing directed edges between nodes.
edge(a, b, 2).
edge(a, c, 5).
edge(b, d, 4).
edge(c, d, 1).
edge(d, goal, 3).

% Heuristic predicate estimating the cost from a node to the goal.
heuristic(Node, Cost) :-
    goal(goal),
    edge(Node, goal, Cost).

% Best First Search algorithm.
best_first_search(Node, Path, Cost) :-
    best_first_search_helper(Node, [Node], 0, Path, Cost).

best_first_search_helper(Node, Path, AccumulatedCost, Path, AccumulatedCost) :-
    goal(Node).

best_first_search_helper(Node, Path, AccumulatedCost, FinalPath, FinalCost) :-
    findall(NextNode, (edge(Node, NextNode, _), not(member(NextNode, Path))), NextNodes),
    best_next_node(NextNodes, Node, AccumulatedCost, NextNode),
    edge(Node, NextNode, EdgeCost),
    NewAccumulatedCost is AccumulatedCost + EdgeCost,
    best_first_search_helper(NextNode, [NextNode | Path], NewAccumulatedCost, FinalPath, FinalCost).

% Helper predicate to find the best next node based on heuristic.
best_next_node([Node], _, _, Node).

best_next_node([Node1, Node2 | Rest], CurrentNode, AccumulatedCost, BestNode) :-
    heuristic(Node1, Cost1),
    heuristic(Node2, Cost2),
    BestCost is min(Cost1, Cost2),
    (Cost1 = BestCost, best_next_node([Node1 | Rest], CurrentNode, AccumulatedCost, BestNode);
     Cost2 = BestCost, best_next_node([Node2 | Rest], CurrentNode, AccumulatedCost, BestNode)).

% Example usage:
% To find a path from 'a' to 'goal', use: best_first_search(a, Path, Cost).
