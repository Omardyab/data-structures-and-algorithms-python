# Challenge Summary
<!-- Description of the challenge -->
Method for the Binary Tree class to find maximum value

## Whiteboard Process
<!-- Embedded whiteboard image -->
![Whiteboard Process](cc16.jpg)
## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->
time: O(n) space: O(1)

## Solution
<!-- Show how to run your code, and examples of it in action -->

    def max(self):
            if self.root is None:
                return None
            max_value = self.root.value
            tree_nodes = self.in_order()

            for i in tree_nodes:
                if i > max_value:
                    max_value = i
            return max_value
