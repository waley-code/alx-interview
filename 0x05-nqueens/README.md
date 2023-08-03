# N Queens
## Algorithm   Python

The backtracking algorithm is a technique used to find solutions for problems that involve making a series of decisions. It systematically explores all possible solutions while discarding the ones that do not satisfy the problem's constraints. The algorithm follows a trial and error approach, and it "backs" or "backtracks" to explore alternative choices whenever a partial solution cannot be completed.

Here's how the backtracking algorithm works:

1. Start at the initial state or configuration: The algorithm begins by considering the initial state of the problem, which may represent an empty solution or a partial solution with some decisions made.

2. Make a decision: The algorithm makes a decision to extend the current state. This decision can be selecting a value, a position, or any other action based on the problem's constraints and requirements.

3. Check if the decision is valid: After making a decision, the algorithm checks if the current state is valid or if it satisfies the problem's constraints. If the state is not valid, the algorithm backtracks to the previous state and undoes the last decision.

4. Explore other choices: If the current state is valid, the algorithm proceeds to the next step or decision and repeats the process of making a decision, checking its validity, and backtracking if needed.

5. Reach the base case or solution: The algorithm continues this process of making decisions and backtracking until it reaches a base case or finds a complete solution. In the context of backtracking, the base case represents a valid complete solution to the problem.

6. If a solution is found, store or output it: If the algorithm reaches a valid solution, it stores or outputs the solution based on the problem's requirements.

7. Backtrack and explore alternative choices: After storing or outputting the solution, the algorithm backtracks to the previous state to explore alternative choices and find more solutions. The backtracking process continues until all possible solutions have been explored.

The backtracking algorithm is used in various problems like the N Queens puzzle, Sudoku, graph traversal, and many more. It is an efficient way to search through a large search space and find valid solutions while avoiding unnecessary computations by backtracking when needed. The algorithm typically has a time complexity of O(b^d), where b is the branching factor (number of choices at each step) and d is the depth of the search space (maximum decision depth).