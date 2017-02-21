class QUEUE:
    def __init__(self):
        self.holder = []

    def enqueue(self, val):
        self.holder.append(val)

    def dequeue(self):
        val = None
        try:
            val = self.holder[0]
            if len(self.holder) == 1:
                self.holder = []
            else:
                self.holder = self.holder[1:]
        except:
            pass

        return val

    def IsEmpty(self):
        result = False
        if len(self.holder) == 0:
            result = True
        return result


def get_all_routes(graph, start, end):
    temp_path = [start]

    q = QUEUE()
    q.enqueue(temp_path)

    valid_routes = []

    while not q.IsEmpty():
        tmp_path = q.dequeue()
        last_node = tmp_path[len(tmp_path) - 1]
        if last_node == end:
             valid_routes.append(tmp_path)
        for link_node in graph[last_node]:
            if link_node not in tmp_path:
                new_path = []
                new_path = tmp_path + [link_node]
                q.enqueue(new_path)
    return valid_routes


def get_longest_route(graph, start, end):
    valid_routes = get_all_routes(graph, start, end)
    if len(valid_routes) == 0:
        return None
    longest = None
    for route in valid_routes:
        if longest is None or (len(route) > len(longest)):
            longest = route
    return longest


def get_shortest_route(graph, start, end):
    valid_routes = get_all_routes(graph, start, end)
    if len(valid_routes) == 0:
        return None
    shortest = None
    for route in valid_routes:
        if shortest is None or (len(route) < len(shortest)):
            shortest = route
    return shortest

if __name__ == "__main__":
    graph = {'A': ['B', 'C', 'E'],
             'B': ['A', 'C', 'D'],
             'C': ['D'],
             'D': ['C'],
             'E': ['F', 'D'],
             'F': ['C']}

    i = get_all_routes(graph, "A", "D")
    for item in i:
        print(item)
    print("")
    i = get_shortest_route(graph, "A", "D")
    print(i)
