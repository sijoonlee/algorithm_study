#include <iostream>
#include "LinkedList.h"

int main(){

    int array[] = {1,2,3};
    LinkedList exampleA = LinkedList(array, 3);
    std::cout << exampleA.GetLength() << "\n";
    exampleA.Print();

    exampleA.InsertBack(4);
    std::cout << exampleA.GetLength() << "\n";
    exampleA.Print();

    exampleA.InsertBefore(0, 0);
    std::cout << exampleA.GetLength() << "\n";
    exampleA.Print();

    exampleA.DeleteBack();
    std::cout << exampleA.GetLength() << "\n";
    exampleA.Print();

    exampleA.DeleteAt(0);
    std::cout << exampleA.GetLength() << "\n";
    exampleA.Print();

    exampleA.Reverse();
    std::cout << exampleA.GetLength() << "\n";
    exampleA.Print();

    int indexToFind;
    indexToFind = exampleA.Find(2);
    if(indexToFind == -1)
        std::cout << "Not Found" << "\n";
    else
        std::cout << "Its index is " << indexToFind << "\n";

    std::cout << exampleA.GetValue(0) << "\n";
    std::cout << exampleA.GetValue(1) << "\n";
    std::cout << exampleA.GetValue(2) << "\n";

    LinkedList exampleB = LinkedList();
    exampleB.InsertBack(6);
    exampleB.InsertBack(5);
    exampleB.InsertBack(4);
    exampleB.Print();

    LinkedList exampleC = exampleB + exampleA;
    exampleC.Print();

}

