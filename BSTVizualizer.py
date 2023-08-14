import matplotlib.pyplot as plt

radius = 0.30
class TreeVisualizer:
    def __init__(self, bst):
        self.bst = bst

    def plot_tree(self, root=None, save_path=None):
        if root is None:
            root = self.bst.root
        fig, ax = plt.subplots(figsize=(8, 6))
        ax.plot([0, 0], [3 - radius, 0], 'k-')
        self._plot_tree(root, 0, 3, 2, ax)
        ax.axis('off')
        
        if save_path:
            plt.savefig(save_path, bbox_inches='tight', pad_inches=0)
        else:
            plt.show()

    def _plot_tree(self, node, x, y, y_diff, ax):
        if node is not None:
            ax.add_patch(plt.Circle((x, y), radius=radius, color='lightblue', ec='black'))
            ax.text(x, y, str(node.key), ha='center', va='center', fontsize=10, fontweight='bold')
            if node.left is not None:
                ax.plot([x, x - y_diff], [y + radius, y + y_diff - radius], 'k-')
                self._plot_tree(node.left, x - y_diff, y + y_diff, y_diff / 2, ax)
            if node.right is not None:
                ax.plot([x, x + y_diff], [y + radius, y + y_diff - radius], 'k-')
                self._plot_tree(node.right, x + y_diff, y + y_diff, y_diff / 2, ax)

    def main(self):
        save_path = 'tree.png'
        self.plot_tree(save_path=save_path)


