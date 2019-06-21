## Linked List Class

**LiknkedList.h**
```
struct Node{
    int data;
    struct Node* next;
};


class LinkedList{
private:
    Node *first;
    int listLength;
    void RecursiveReverse(Node * cursor, Node * next);

public:
    LinkedList();
    LinkedList(int array[], int length);
    ~LinkedList();

    void Print() const;
    int GetLength() const;
    void InsertBefore(int index, int value);
        // Insert a node before a given index
    void InsertBack(int value);
        // Insert a node to the back
    void DeleteAt(int index);
        // Delete a node at a given index
    void DeleteBack();
        // Delete the last node
    void Reverse();
        // Reverse list
    int Find(int value) const;
        // Find a node that has the given value
        // If not found, return -1
    int GetValue(int index) const;
        // Get a value of a node with the given index

    LinkedList operator+(const LinkedList &rhs) const;
        // concatenate two LinkedList objects
        // return new LinkedList
};
```

