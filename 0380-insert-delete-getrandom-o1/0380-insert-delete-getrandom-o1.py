
import random
class RandomizedSet:

    def __init__(self):
        self.vals = [] # list to store values
        self.idx= {} #  Dictionary to store the value to index mapping

    def insert(self, val: int) -> bool:

        if val in self.idx:
            return False
        # Append the value to the list and update the dictionary with its index
        self.vals.append(val)
        self.idx[val] = len(self.vals)-1
        return True 
        

    def remove(self, val: int) -> bool:
        #Check if val does not exist in the set

        if val not in self.idx:
            return False

        #Move the last value to the place idx of the value to delete

        last = self.vals[-1]
        idx_to_remove  = self.idx[val] #the index to remove

        #Move the last element to the place of the value to be removed:
        # take last element into the palce where the value will be deleted
        self.vals[idx_to_remove] = last

        #update the last element in the dictionary
        self.idx[last] = idx_to_remove

        #Remove the last value and delete the value from the dictionary:
        self.vals.pop()
        #deletes the key 5 from the dictionary. 
        del self.idx[val]

        return True



        

    def getRandom(self) -> int:
                # Fetch a random value from the list
        return random.choice(self.vals)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()

'''
Data Structures:

self.idx: Dictionary for quick value-to-index mapping.
self.vals: List storing all values.
Steps:

Existence Check:

Check if the value exists in self.idx. If not, return False.
Get Last Element & Target Index:

Fetch the last element in self.vals.
Determine the index of the value we want to remove using self.idx.
Swap & Update:

Replace the target value in self.vals with the last element.
Update the index of this last element in self.idx to the previous index of the target value.
Clean Up:

Remove the last element from self.vals (which is now a duplicate due to the swap).
Delete the target value's entry from self.idx.
'''