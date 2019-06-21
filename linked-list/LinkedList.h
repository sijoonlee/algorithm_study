//
// Created by sijoonlee on 6/21/19.
//

#ifndef LINKED_LIST_LINKEDLIST_H
#define LINKED_LIST_LINKEDLIST_H


#include <iostream>

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
    void InsertBack(int value);
    void DeleteAt(int index);
    void DeleteBack();
    void Reverse();
    int Find(int value) const;
    int GetValue(int index) const;

    LinkedList operator+(const LinkedList &rhs) const; // concatenate

};

#endif //LINKED_LIST_LINKEDLIST_H
