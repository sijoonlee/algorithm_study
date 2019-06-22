#include <iostream>
#include "doublyLinkedList.h"

int main() {

    List<int> myList;
    myList.PushFront(2);
    myList.PushBack(3);
    myList.PushFront(1);
    myList.PushFront(0);
    myList.Print();
    std::cout << myList.PopFront() <<"\n";
    std::cout << myList.PopBack()<<"\n";
    myList.Print();
    //std::cout << myList.Size()<<"\n";
    std::cout << "----------" << "\n";
    List<int> myListB;
    myListB.PushFront(0);
    myListB.PushBack(4);
    myListB.PushBack(5);
    myListB.Print();

    return 0;
}