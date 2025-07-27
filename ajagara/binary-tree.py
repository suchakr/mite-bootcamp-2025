class TreeNode:
    """Simple BST node with value and left/right pointers"""
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BST:
    def __init__(self):
        self.root = None
    
    def insert(self, val):
        """Insert maintaining BST property: left < root < right"""
        self.root = self._insert_recursive(self.root, val)
    
    def _insert_recursive(self, node, val):
        if not node:
            return TreeNode(val)
        
        if val < node.val:
            node.left = self._insert_recursive(node.left, val)
        else:
            node.right = self._insert_recursive(node.right, val)
        
        return node

# ============================================================================
# TRAVERSAL METHODS - Each serves different purposes!
# ============================================================================

def inorder_traversal(root):
    """
    INORDER: Left → Root → Right
    🎯 USE CASE: Get sorted elements from BST
    📊 OUTPUT: Always sorted ascending order for BST
    ⏰ COMPLEXITY: O(n) time, O(h) space (h = height)
    """
    result = []
    
    def inorder_helper(node):
        if node:
            inorder_helper(node.left)    # Visit left subtree first
            result.append(node.val)      # Process current node
            inorder_helper(node.right)   # Visit right subtree last
    
    inorder_helper(root)
    return result

def preorder_traversal(root):
    """
    PREORDER: Root → Left → Right
    🎯 USE CASE: Create copy of tree, serialize tree structure
    📊 OUTPUT: Root comes first, then subtrees
    ⏰ COMPLEXITY: O(n) time, O(h) space
    💡 MEMORY: Good for reconstructing tree from traversal
    """
    result = []
    
    def preorder_helper(node):
        if node:
            result.append(node.val)      # Process current node FIRST
            preorder_helper(node.left)   # Then left subtree
            preorder_helper(node.right)  # Finally right subtree
    
    preorder_helper(root)
    return result

def postorder_traversal(root):
    """
    POSTORDER: Left → Right → Root
    🎯 USE CASE: Delete tree safely, calculate tree size/height
    📊 OUTPUT: Children processed before parent
    ⏰ COMPLEXITY: O(n) time, O(h) space
    💡 MEMORY: Safe for operations that need children done first
    """
    result = []
    
    def postorder_helper(node):
        if node:
            postorder_helper(node.left)   # Process left subtree first
            postorder_helper(node.right)  # Process right subtree second
            result.append(node.val)       # Process current node LAST
    
    postorder_helper(root)
    return result

def level_order_traversal(root):
    """
    LEVEL ORDER: Visit nodes level by level (BFS)
    🎯 USE CASE: Print tree by levels, find shortest path
    📊 OUTPUT: Level 0, then level 1, then level 2, etc.
    ⏰ COMPLEXITY: O(n) time, O(w) space (w = max width)
    💡 ITERATIVE: Uses queue instead of recursion
    """
    if not root:
        return []
    
    from collections import deque
    result = []
    queue = deque([root])
    
    while queue:
        node = queue.popleft()
        result.append(node.val)
        
        # Add children to queue for next level processing
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    
    return result

# ============================================================================
# PRACTICAL APPLICATIONS OF EACH TRAVERSAL
# ============================================================================

def validate_bst(root):
    """
    🔍 INORDER APPLICATION: Validate if tree is actually a BST
    Logic: Inorder of valid BST must be strictly ascending
    """
    inorder_vals = inorder_traversal(root)
    
    # Check if inorder sequence is sorted (BST property)
    for i in range(1, len(inorder_vals)):
        if inorder_vals[i] <= inorder_vals[i-1]:
            return False
    return True

def serialize_tree(root):
    """
    💾 PREORDER APPLICATION: Serialize tree to string
    Logic: Root first allows easy reconstruction
    """
    def serialize_helper(node):
        if not node:
            return "null"
        return f"{node.val},{serialize_helper(node.left)},{serialize_helper(node.right)}"
    
    return serialize_helper(root)

def calculate_tree_size(root):
    """
    📏 POSTORDER APPLICATION: Calculate total nodes
    Logic: Count children first, then add current node
    """
    def size_helper(node):
        if not node:
            return 0
        
        left_size = size_helper(node.left)    # Count left subtree
        right_size = size_helper(node.right)  # Count right subtree
        return left_size + right_size + 1     # Add current node
    
    return size_helper(root)

def print_tree_by_levels(root):
    """
    🎨 LEVEL ORDER APPLICATION: Pretty print tree structure
    Logic: Show tree level by level for better visualization
    """
    if not root:
        return
    
    from collections import deque
    queue = deque([(root, 0)])  # (node, level)
    current_level = 0
    level_nodes = []
    
    while queue:
        node, level = queue.popleft()
        
        if level != current_level:
            print(f"Level {current_level}: {level_nodes}")
            level_nodes = []
            current_level = level
        
        level_nodes.append(node.val)
        
        if node.left:
            queue.append((node.left, level + 1))
        if node.right:
            queue.append((node.right, level + 1))
    
    print(f"Level {current_level}: {level_nodes}")

# ============================================================================
# DEMONSTRATION WITH SAMPLE BST
# ============================================================================

def demo_traversals():
    """
    Demo all traversals with concrete example
    Tree structure:
         4
       /   \
      2     6
     / \   / \
    1   3 5   7
    """
    
    # Build sample BST
    bst = BST()
    values = [4, 2, 6, 1, 3, 5, 7]
    for val in values:
        bst.insert(val)
    
    print("🌳 Sample BST with values:", values)
    print("   Tree structure:")
    print("       4")
    print("     /   \\")
    print("    2     6")
    print("   / \\   / \\")
    print("  1   3 5   7")
    print()
    
    # Demonstrate each traversal
    print("📊 TRAVERSAL RESULTS:")
    print(f"Inorder   (L→R→R): {inorder_traversal(bst.root)}")     # [1,2,3,4,5,6,7] - SORTED!
    print(f"Preorder  (R→L→R): {preorder_traversal(bst.root)}")    # [4,2,1,3,6,5,7] - Root first
    print(f"Postorder (L→R→R): {postorder_traversal(bst.root)}")   # [1,3,2,5,7,6,4] - Root last
    print(f"Level order (BFS): {level_order_traversal(bst.root)}")  # [4,2,6,1,3,5,7] - By levels
    print()
    
    # Demonstrate practical applications
    print("🔧 PRACTICAL APPLICATIONS:")
    print(f"Is valid BST? {validate_bst(bst.root)}")
    print(f"Tree size: {calculate_tree_size(bst.root)} nodes")
    print(f"Serialized: {serialize_tree(bst.root)}")
    print()
    
    print("🎨 TREE BY LEVELS:")
    print_tree_by_levels(bst.root)

# ============================================================================
# QUICK REFERENCE - WHEN TO USE WHICH TRAVERSAL
# ============================================================================

"""
🎯 TRAVERSAL CHEAT SHEET:

INORDER (Left → Root → Right):
✅ Get sorted data from BST
✅ Validate BST property
✅ Find kth smallest element
✅ Convert BST to sorted array

PREORDER (Root → Left → Right):
✅ Create copy of tree
✅ Serialize/save tree structure
✅ Print tree with proper indentation
✅ Evaluate expression trees (prefix)

POSTORDER (Left → Right → Root):
✅ Delete/free tree memory safely  
✅ Calculate tree properties (size, height)
✅ Evaluate expression trees (postfix)
✅ Directory size calculations

LEVEL ORDER (Breadth-First):
✅ Print tree level by level
✅ Find shortest path in unweighted tree
✅ Check if tree is complete
✅ Serialize tree with level info
"""

if __name__ == "__main__":
    demo_traversals()