class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        avail_keys=set()

        def key_add(keys):
            for k in keys:
                avail_keys.add(k)
 
        key_add(rooms[0])
        visited = {0}
        while avail_keys:
            i = avail_keys.pop()
            if i not in visited:
                key_add(rooms[i])
                visited.add(i)

        return len(visited) == len(rooms)
            


        