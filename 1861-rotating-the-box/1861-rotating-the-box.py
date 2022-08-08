class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        STONE, OBSTACLE, EMPTY = '#', '*', '.'
        rotated = []
        rows, cols = len(box), len(box[0])
        
        # first, move all stones to the RIGHT
        # why? because when we rotate, the 'right' will turn into the bottom
        for row in box:
            move_position = len(row)-1
            for i in range(len(row)-1, -1, -1):
                if row[i] == OBSTACLE:
                    move_position = i-1
                
                if row[i] == STONE:
                    row[i], row[move_position] = row[move_position], row[i]
                    move_position-=1
                    
        # then rotate the box clockwise
        for i in range(cols):
            rotated.append([])
            for j in range(rows-1, -1, -1):
                rotated[i].append(box[j][i])
            
                
        return rotated
            
                
                
                    
                
                
        