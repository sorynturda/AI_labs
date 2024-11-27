def depthFirstSearch(problem: SearchProblem) -> List[Directions]:
	"""
	Cautare in adancime
	"""
	stack = Stack()
    node = problem.getStartState()
    visited = set()
    stack.push((node, []))
    while not stack.isEmpty():
        position, path = stack.pop()
        if position not in visited:
            visited.add(position)
            if problem.isGoalState(positoin):
                return path
            for successor, action, cost in problem.getSuccessors(position):
                if successor not in visited:
                    stack.push((successor, path + [action]))
    return []