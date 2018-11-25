
class ListNode:

    def __init__(self, x, prev=None, next=None):
        """
        list node
        :param x: the satellite data
        :param prev: points to its predecessor
        :param next: points to its successor in the linked list
        """
        self.value = x
        self.next = next
        self.prev = prev


class list_:
    def __init__(self):
        self.nil = ListNode(None)

    def search(self, value):
        """
        searching in a linked list
        the cost time is O(n)
        :param value: the satellite value equals to
        :return: the node if not find return None
        """
        node = self.nil.next  # set the start node
        while node and node.value != value:  # the loop condition
            node = node.next
        # if not find the node, the list have gone to the tail of list
        # and the tail's next is None, so the node is None
        return node

    def insert(self, value):
        """
        insert the value into the list
        the cost time is O(n)
        :param value: the value to be inserted
        :return: the node have inserted
        """
        current = self.nil.next
        while current.next:  # to find the tail of the list
            current = current.next
        node = ListNode(value, current, None)  # create new node with prev node
        current.next = node  # change the tail node
        node.next = self.nil.next
        return node

    def delete(self, node):
        """
        delete the given node
        :param node: the node to delete
        :return: the deleted node
        """
        if node.prev:  # if the node's prev is not None, change its predecessor's prev
            node.prev.next = node.next
        if node.next:  # if the node'next is not None, change its successor's next
            node.next.prev = node.prev
        return node

    def delete(self, value):

        node = self.search(value)
        if node:
            return self.delete(node)
        else:return None

