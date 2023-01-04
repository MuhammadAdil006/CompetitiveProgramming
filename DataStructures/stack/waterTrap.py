#this question can be solved by two ways
#dp solution
from collections import deque
# def trap(height):
        # ans=0
        # left_max=[0 for i in range(len(height))]
        # right_max=[0 for i in range(len(height))]

        # left_max[0]=(height[0])
        # for i in range(1,len(height)):
        #     left_max[i]=max(height[i],left_max[i-1])
        # right_max[len(height)-1]=height[-1]
        # for i in range(len(height)-2,-1,-1):
        #     right_max[i]=max(height[i],right_max[i+1])
        # for i in range(len(height)):
        #     ans+=min(left_max[i],right_max[i])-height[i]
        # return ans

#stack solution

def trap(height):
    ans,current=0,0
    st=deque()
    while (current < len(height)):
        while ( not len(st)==0 and height[current] > height[st[-1]]):
            top =st[-1]
            st.pop()
            if (len(st)==0):
                break
            distance = current - st[-1] - 1
            bounded_height = min(height[current], height[st[-1]]) - height[top]
            ans += distance * bounded_height
        
        st.append(current)
        current+=1
    return ans
