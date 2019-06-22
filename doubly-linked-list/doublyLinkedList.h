//
// Created by sijoonlee on 6/21/19.
//
#pragma once
#include <iostream>


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

template <typename T>
List<T>::List(){
    head = nullptr;
    tail = nullptr;
}

template <typename T>
List<T>::~List() {
    // release memory of each node
    while(head){
        Node *temp(head);
        head = head->next;
        delete temp;
    }
}

template <typename T>
void List<T>::PushFront(T value){
    if(head == nullptr){
        head = new Node(value);
        head->prev = nullptr;
        head->next = nullptr;
        tail = head;
    } else {
        Node * temp = new Node(value);
        temp->next = head;
        head->prev = temp;
        head = temp;
    }

}
template <typename T>
void List<T>::PushBack(T value){

    if(head == nullptr){
        head = new Node(value);
        head->prev = nullptr;
        head->next = nullptr;
        tail = head;
    } else {
        Node * temp = new Node(value);
        tail->next = temp;
        temp->prev = tail;
        tail = temp;
    }

}
template <typename T>
T List<T>::PopFront(){
    if (head== nullptr) {
        throw("Empty");
    }
    Node * temp(head);
    T value = head->data;
    head = head->next;
    if(head)
        head->prev = nullptr;
    else
        tail = nullptr;

    delete temp;
    return value;
}
template <typename T>
T List<T>::PopBack(){
    if (head== nullptr) {
        throw("Empty");
    }
    Node * temp(tail);
    tail = tail->prev;
    if(tail)
        tail->next = nullptr;
    else
        head = nullptr;

    T value = temp->data;
    delete temp;
    return value;

}
template <typename T>
int List<T>::Size() const{
    if(head == nullptr){
        return 0;
    }

    Node * node = head;
    int length = 1;
    while(node->next){
        length ++;
        node = node->next;
    }

  return length;
}
template <typename T>
void List<T>::Print() const{
    Node * node = head;
    int counter = 0;
    while(node){
        std::cout << "index " << counter << ": " << node->data << "\n";
        counter++;
        node = node->next;
    }
}


