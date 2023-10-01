LEFT = 0
HEIGHT = 1
RIGHT = 2

N = int(input())
building_list = [[int(i) for i in input().split(' ')] for _ in range(N)]
#print(building_list)

def min(p, q):
    if(p > q):
        return q
    else :
        return p

def max(p, q):
    if(p>q):
        return p
    else : 
        return q

class Range_node:

    node_L = None
    node_R = None

    def __init__(self, left, height, right):
        self.left = left
        self.right = right
        self.height = height
    
    def set_node_L(self, node):
        if(self.height == node.height and self.left == node.right):
            self.left = node.left
            return
        else :
            self.node_L = node
    
    def set_node_R(self, node):
        if(self.height == node.height and self.right == node.left):
            self.right = node.right
            return
        else :
            self.node_R = node
    
    def print_all_node(self):

        if(self.node_L != None):
            self.node_L.print_all_node()
        print((self.left, self.height, self.right))
        if(self.node_R != None):
            self.node_R.print_all_node()

    def append_all_node(self):
        temp_list = []
        if(self.node_L != None):
            temp_list.extend(self.node_L.append_all_node())
        temp_list.append([self.left, self.height, self.right])
        if(self.node_R != None):
            temp_list.extend(self.node_R.append_all_node())
        
        return temp_list

    def get_min(self):
        if(self.node_L == None):
            return self
        return self.node_L

    def get_max(self):
        if(self.node_R == None):
            return self
        return self.node_R
    
    def delete_max(self):
        if(self.node_R == None):
            return self

        if(self.node_R.node_R == None):
            max_node = self.node_R
            self.node_R = self.node_R.node_L
            print(max_node.left, max_node.height, max_node.right)
            return max_node
        else :
            return self.node_R.delete_max()

    def delete_min(self):
        if(self.node_L == None):
            return self

        if(self.node_L.node_L == None):
            min_node = self.node_L
            self.node_L = self.node_L.node_R
            print(min_node.left, min_node.height, min_node.right)
            return min_node
        else :
            return self.node_L.delete_min()

    def pop_nearby_min(self):
        if(self.node_L == None):
            return None
        else :
            return self.node_L.delete_max()
    
    def pop_nearby_max(self):
        if(self.node_R == None):
            return None
        else :
            return self.node_R.delete_min()
    
    def merge_nearby_max(self):
        nearby_max_node = self.get_nearby_max()

        if(nearby_max_node == None):
            return

        if(self.height == nearby_max_node.height
           and self.right == nearby_max_node.left):
            self.right = nearby_max_node.right
            self.pop_nearby_max()

    def merge_nearby_min(self):
        nearby_min_node = self.get_nearby_min()

        if(nearby_min_node == None):
            return

        if(self.height == nearby_min_node.height
           and self.left == nearby_min_node.right):
            self.left = nearby_min_node.left
            self.pop_nearby_min()

    def get_nearby_min(self):
        if(self.node_L == None):
            return None
        else :
            return self.node_L.get_max()

    def get_nearby_max(self):
        if(self.node_R == None):
            return None
        else :
            return self.node_R.get_min()
    
    def add(self, left, height, right):

        if(left == right):
            return
        
        if(left > right):
            return
        

        if(self.right <= left):
            
            if(self.node_R == None):
                self.set_node_R(Range_node(left, height, right))
                return
            
            self.node_R.add(left, height, right)
            return

        if(self.left >= right):

            if(self.node_L == None):
                self.set_node_L(Range_node(left, height, right))

            self.node_L.add(left, height, right)
            return
        
        self_left_final = max(self.left, left)
        self_right_final = min(self.right, right)
        self_height_final = max(self.height, height)



        if(self.node_L == None):
            if(self.left != left):
                
                self.set_node_L(Range_node(min(self.left, left), 
                        self.height if min(self.left, left) == self.left else height,
                        max(self.left, left)))
        else :
            
            self.node_L.add(min(self.left, left), 
                        self.height if min(self.left, left) == self.left else height,
                        max(self.left, left))
        
        if(self.node_R == None):
            if(min(self.right, right) != max(self.right, right)):
                
                self.set_node_R(Range_node(min(self.right, right), 
                        self.height if max(self.right, right) == self.right else height,
                        max(self.right, right)))
        else :

            self.node_R.add(min(self.right, right), 
                        self.height if max(self.right, right) == self.right else height,
                        max(self.right, right))
        
        self.left = self_left_final
        self.right = self_right_final
        self.height = self_height_final

        self.merge_nearby_max()
        self.merge_nearby_min()
        
    
    def add_node(self, left, height, right):
        self.add(left, height, right)
        #self.merge()
    
    def merge(self):
        return



if(len(building_list) > 0):
    root = Range_node(building_list[0][LEFT], building_list[0][HEIGHT], building_list[0][RIGHT])

    for i in range(len(building_list)):
        if(i == 0):
            continue
        root.add_node(building_list[i][LEFT], building_list[i][HEIGHT], building_list[i][RIGHT])

root_all_node_list = root.append_all_node()
print(root_all_node_list)
# text = ""/

# for i in range(len(root_all_node_list)):
#     if(i == 0):
#         text += str(root_all_node_list[0][LEFT]) + " " + str(root_all_node_list[0][HEIGHT]) + " "
#         continue
#     if(i == len(root_all_node_list) -1):
#         text += str(root_all_node_list[i][RIGHT]) + " " + "0 "
#         continue
#     if(root_all_node_list[i-1][RIGHT] == root_all_node_list[i][LEFT] and 
#        root_all_node_list[i-1][HEIGHT] == root_all_node_list[i][HEIGHT]):
#         continue
#     if(root_all_node_list[i-1][RIGHT] != root_all_node_list[i][LEFT]):
#         text += str(root_all_node_list[i-1][RIGHT]) + " " + "0 "
        
#     text += str(root_all_node_list[i][LEFT]) + " " + str(root_all_node_list[i][HEIGHT]) + " "

# print(text)
#[[1, 11, 2], [2, 11, 3], [3, 13, 5], [5, 13, 7], [7, 13, 9], [12, 7, 14], [14, 7, 16], [16, 3, 19], [19, 18, 22], [22, 3, 23], [23, 13, 24], [24, 13, 25], [25, 13, 28], [28, 13, 29]]
#[[1, 11, 3], [3, 13, 5], [5, 13, 7], [7, 13, 9], [12, 7, 14], [14, 7, 16], [16, 3, 19], [19, 18, 22], [22, 3, 23], [23, 13, 24], [24, 13, 25], [25, 13, 28], [28, 13, 29]]