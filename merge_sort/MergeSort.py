class MergeSort:
    @classmethod
    def _merge(cls, left, right, merged):
        i, j = 0, 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                j += 1

        if i < len(left):
            merged.extend(left[i:])
        elif j < len(right):
            merged.extend(right[j:])

        return merged
    
    @classmethod
    def sort(cls, unsorted):
        if len(unsorted) <= 1:
            return unsorted
        else:
            pivot = len(unsorted) // 2
            left = cls.sort(unsorted[:pivot])
            right = cls.sort(unsorted[pivot:])

            return cls._merge(cls.sort(left), cls.sort(right), [])