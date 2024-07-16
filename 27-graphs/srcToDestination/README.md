## Source to Destination

Given a source node and destination node, check if the destination node is reachable from the source node.

## Approach

Do the <a href="../breadthFirst/README.md">BFS</a> and check if still the visited node is False,
If the visited node has False value, it means we could not reach to that node, thus it is not reachable.
Otherwise, it is reachable.
