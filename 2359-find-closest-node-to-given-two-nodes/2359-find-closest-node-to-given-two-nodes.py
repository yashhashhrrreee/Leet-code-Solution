class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        if node1 == node2: return node1

        p1, p2 = node1, node2
        p1_path_set = set([p1])
        p2_path_set = set([p2])

        while True:
            next_p1 = edges[p1]            
            next_p2 = edges[p2]
            
            next_p1 = p1 if next_p1 == -1 else next_p1
            next_p2 = p2 if next_p2 == -1 else next_p2

            hit_list = []
            
            if next_p1 in p2_path_set:
                hit_list.append(next_p1)
            if next_p2 in p1_path_set:
                hit_list.append(next_p2)
            
            if hit_list:
                return min(hit_list)
            elif next_p1 == next_p2:
                return next_p1

            if all([
                next_p1 in p1_path_set,
                next_p2 in p2_path_set]):
                return -1

            p1_path_set.add(next_p1)
            p2_path_set.add(next_p2)
            p1, p2 = next_p1, next_p2