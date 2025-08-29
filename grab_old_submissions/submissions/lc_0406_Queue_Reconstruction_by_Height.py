class OccupationNode:
    def __init__(self,L,R):
        self.L=L
        self.R=R
        if L == R:
            self.right = None
            self.left = None
            self.value = 1 #This is unoccupied
            return
        middle = (L+R)//2
        self.left = OccupationNode(L,middle)
        self.right = OccupationNode(middle+1,R)
        self.value = self.left.value+self.right.value
    
    def mark_occupied(self,index):
        if self.L == self.R:
            if self.L == index:
                self.value = 0
                return
            else:
                print("Shouldn't be possible to be here.")
        middle = (self.L + self.R)//2
        if index <= middle:
            self.left.mark_occupied(index)
        if index >middle:
            self.right.mark_occupied(index)
        self.value = self.left.value + self.right.value
    
    def find_nth_open(self,index):
        if self.L == self.R:
            return self.L # We found a leaf!
        discriminator = index - self.left.value
        if discriminator >= 0:
            return self.right.find_nth_open(discriminator)
        else:
            return self.left.find_nth_open(index)
        #Flow: find nth open -> get an index -> move the person to that index in the output
        # -> mark it as occupied -> continue to next person
        # people are sorted from short to tall, then from high to low by # in front

class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        """General idea (had to quit and watch a pretty serious soln): This is a kind of sort, so our absolute
        minimum is O(nlog(n)) TC. Per the hint, the index of the shortest person with the smallest number of taller
        people in front is exactly the # of as-tall-or-taller people in front of them, and this is true for anybody 
        of the same height with more as-tall-or-taller ppl in front of them. What we *could* do is complicated 
        inserts from tall to short, but this will take lots and lots of comparisons. Instead, we'll place ppl 
        at their appropriate index right away by keeping track of which spots are occupied and searching down a tree
        to determine where the "height-adjusted index" (# of people) maps to in the occupied spots in the queue. 
        
        We can do this using Segment Trees."""
        height_to_people = defaultdict(list)
        for person in people:
            height_to_people[person[0]].append(person)
        sorted_heights = list(height_to_people.keys())
        sorted_heights.sort() #Shortest-to-tallest
        # Let's arrange each set of values by ppl in front
        for heighted_key in sorted_heights:
            people_list = height_to_people[heighted_key]
            for person in people_list:
                person.reverse()
            people_list.sort()
            people_list.reverse() # high-to-low
            for person in people_list:
                person.reverse() # back to original orientation, but sorted high-to-low by visibility
            height_to_people[heighted_key] = people_list # May not be necessary but JIC
        # Finally ready to construct the result
        result = [[]]*len(people)
        head = OccupationNode(0,len(people)-1)
        for heighted_key in sorted_heights:
            people_list = height_to_people[heighted_key]
            for person in people_list:
                result_index = head.find_nth_open(person[1])
                result[result_index] = person
                head.mark_occupied(result_index)
        return result