#Question215
class Solution(object):
    def heappush(heap, val):
        heap.append(val)
        i = len(heap) - 1

        # heapify-up
        while i > 0:
            parent = (i - 1) // 2
            if heap[i] < heap[parent]:
                heap[i], heap[parent] = heap[parent], heap[i]
                i = parent
            else:
                break


    def heappop(heap):
        if len(heap) == 1:
            return heap.pop()

        root = heap[0]
        heap[0] = heap.pop()
        i = 0

        # heapify-down
        while True:
            left = 2 * i + 1
            right = 2 * i + 2
            smallest = i

            if left < len(heap) and heap[left] < heap[smallest]:
                smallest = left

            if right < len(heap) and heap[right] < heap[smallest]:
                smallest = right

            if smallest != i:
                heap[i], heap[smallest] = heap[smallest], heap[i]
                i = smallest
            else:
                break

        return root
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        heap = []

        for x in nums:
            if len(heap) < k:
                heappush(heap, x)
            else:
                if x > heap[0]:
                    heappop(heap)
                    heappush(heap, x)

        return heap[0]
