class Solution:
    def finalPrices(self, prices: list[int]) -> list[int]:
        answer = list(prices)
        stack = []  # Stores indices of items waiting for a discount
        
        for i, current_price in enumerate(prices):
            # Apply current_price as a discount to all previous items that are >= current_price
            while stack and prices[stack[-1]] >= current_price:
                prev_index = stack.pop()
                answer[prev_index] -= current_price
            
            stack.append(i)
            
        return answer