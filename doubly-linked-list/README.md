## Doubly Linked List Class
- written in C++
- Push & Pop Methods
- Template applied


**doublyLiknkedList.h**
```
template <typename T>
class List {

private:
    struct Node{
        T data;
        Node* prev;
        Node* next;
        Node(){}
        Node(T value)
                :data(value){}
    };
    Node *head;
    Node *tail;

public:
    List<T>();
    ~List<T>();

    void PushFront(T value);
    void PushBack(T value);
    T PopFront();
    T PopBack();
    int Size() const;
    void Print() const;

};
```

