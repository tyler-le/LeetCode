class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:

        meetings.sort(key = lambda x : x[0])

        # keep track of lowest available meeting room
        available_rooms = [room for room in range(n)]

        # keep track of the occupied rooms that end first
        occupied_rooms = [] # (end, room)

        # count the number of meetings within a room
        cnt = defaultdict(int)

        # go thru each meeting and assign it to the room that ends first
        for start, end in meetings:

            # de-occupy rooms
            while occupied_rooms and occupied_rooms[0][0] <= start:
                occupy_end, occupy_room = heappop(occupied_rooms)
                heappush(available_rooms, occupy_room)

            # if there are available rooms, occupy them
            if available_rooms:
                room = heappop(available_rooms)
                print(f"room {room} is taking {[start, end]}")
                cnt[room]+=1
                heappush(occupied_rooms, (end, room))

            # if there are no available rooms
            # give it to the earliest-finishing room
            else:
                prev_end, room = heappop(occupied_rooms)
                print(f"room {room} is taking {[start, end]}")
                cnt[room]+=1
                heappush(occupied_rooms, (prev_end + end - start, room))

        mx = max(cnt.values())
        for i in range(n):
            if cnt[i] == mx: return i


