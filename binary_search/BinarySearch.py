class BinarySearch:
    
    @classmethod
    def search(cls, ls, item, min=0, max=None):
        '''
        Return index list of all occurences.
        Should be called only with list and item to search,
        but it is possible to call this method with key arguments min and max
        to search in list slice.

        Params:
            - list of integers
            - integer
            - min: integer
            - max: integer
        
        Return:
            - list of integers
        '''

        # of no max is specified, use full length of list
        if max == None:
            max = len(ls) - 1

        # set index of item nearest to median
        half = (max+min) // 2

        # if no difference between min and half or max and half, no solution exists
        if min == half or max == half:
            return []
        
        # return index when match is found
        # --- NEED TO SCAN AROUND FOR DUPLICATES ---
        if ls[half] == item:
            # save solution
            solution = [half]

            lesser_neighbor_index = half - 1
            bigger_neightbor_index = half + 1

            # search in lesser neighbors
            while lesser_neighbor_index >= 0 and ls[lesser_neighbor_index] == ls[half]:
                solution.append(lesser_neighbor_index)
                lesser_neighbor_index -= 1
            
            # seach in bigger neighbors
            while bigger_neightbor_index < len(ls) and ls[bigger_neightbor_index] == ls[half]:
                solution.append(bigger_neightbor_index)
                bigger_neightbor_index += 1
            
            return solution


        # search in lesser half
        elif ls[half] > item:
            return cls.search(ls, item, min=min, max=half)
        # search in bigger half
        else:
            return cls.search(ls, item, min=half, max=max)