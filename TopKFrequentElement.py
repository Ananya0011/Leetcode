class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        dis=list(set(nums))
        dict1={}
        for i in range(len(dis)):
            dict1[dis[i]]=0
        #now frequency
        for x in nums:
            dict1[x]+=1
        #now figuring out the top 2
        
        heap=[]
        for num,freq in dict1.items():
            heap.append((freq,num))
            i=len(heap)-1
            while i>0:
                parent=(i-1)//2
                if heap[i]<heap[parent]:
                    heap[i],heap[parent]=heap[parent],heap[i]
                    i=parent
                else:
                    break
            if len(heap)>k:
                heap[0],heap[-1]=heap[-1],heap[0]
                heap.pop()
                i=0
                while True:
                    left=2*i+1
                    right=2*i+2
                    smallest=i
                    if left<len(heap) and heap[left]<heap[smallest]:
                        smallest=left
                    if right<len(heap) and heap[right]<heap[smallest]:
                        smallest=right
                    if smallest!=i:
                        heap[i],heap[smallest]=heap[smallest],heap[i]
                        i=smallest
                    else:
                        break
                
        return [x[1] for x in heap]
                        
            
                
                       
        





            
