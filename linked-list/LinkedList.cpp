//
// Created by sijoonlee on 6/21/19.
//

#include "LinkedList.h"


LinkedList::LinkedList(){
    first = NULL;
    listLength = 0;
}

LinkedList::LinkedList(int array[], int length){

    // The first node
    first = new Node;
    first->data = array[0];
    first->next = NULL;
    listLength = length;

    Node *last = first;

    // Fill the temp with the array element's value
    // and propagate the list with temp
    Node *temp;
    int index;
    for(index = 1; index < length ; index ++ ){
        temp = new Node;
        temp->data = array[index];
        temp->next = NULL;
        last->next = temp;
        last = temp;
    }
}

LinkedList::~LinkedList() {
    // release memory of each node
    while(first){
        Node *temp = first;
        first = first->next;
        delete [] temp;
    }
}

void LinkedList::Print() const{
    Node * node = first;
    int counter = 0;
    while(node){
        std::cout << "index " << counter << ": " << node->data << "\n";
        counter++;
        node = node->next;
    }

}

int LinkedList::GetLength() const {
//    Node * node = first;
//    int length = 0;
//    while(node){
//        length ++;
//        node = node->next;
//    }
//  return length;
    return listLength;
}

void LinkedList::InsertBack(int value){

    if(first == NULL){
        first = new Node;
        first->data = value;
        first->next = NULL;

    } else {
        Node * last = new Node;
        last->data = value;

        Node * node = first;

        while(node->next){
            node = node->next;
        }
        node->next = last;
    }

    listLength++;
}

void LinkedList::InsertBefore(int index, int value){

    if (index < 0 || index > listLength){
        std::cout << "Index is out of range, You can use 0 ~ " << listLength << "\n";
        return;
    }
    if(first==NULL){
        std::cout << "use InsertBack(value) method instead, please" << "\n";
        return;
    }

    Node * node = first;
    Node * temp = new Node;
    temp->data = value;

    if ( index > 0){
        for(int i = 0; i <  index-1 ; i++ )
            node = node->next; // stop at the node right before the index

        temp->next = node->next;
        node->next = temp;

    }
    else { // index == 0
        temp->next = first;
        first = temp;
    }

    listLength++;

}

void LinkedList::DeleteBack() {

    if ( listLength < 0 ){
        std::cout << "listLength is less than 0, you need to debug" << "\n";
        return;
    }
    if(first==NULL){
        std::cout << "Nothing to delete" << "\n";
        return;
    }
    Node * node = first;
    int deletedValue;

    if(listLength == 1) {
        deletedValue = node->data;
        delete [] node;

    } else if ( listLength > 1 ){

        for(int i = 0; i <  listLength-2 ; i++ )
            node = node->next; // stop at the node right before the last one

        Node * temp = node->next;
        node->next = NULL;
        deletedValue = temp->data;
        delete [] temp;
    }
    std::cout << "Value " << deletedValue << " is deleted" << "\n";
    listLength--;

}

void LinkedList::DeleteAt(int index){
    if (index < 0 || index > listLength){
        std::cout << "Index is out of range, You can use 0 ~ " << listLength << "\n";
        return;
    }

    if ( listLength < 0 ){
        std::cout << "listLength is less than 0, you need to debug" << "\n";
        return;
    }
    if(first==NULL){
        std::cout << "Nothing to delete" << "\n";
        return;
    }

    int deletedValue;

    if ( index == 0 ){
        Node * temp = first;
        deletedValue = first->data;
        first = first->next;
        delete [] temp;

    } else {
        Node * beforeIndex = first;
        Node * atIndex = beforeIndex->next;
        for(int i = 1; i <  index-1 ; i++ ){
            beforeIndex = atIndex;
            atIndex = atIndex->next;
        }
        beforeIndex->next = atIndex->next;
        deletedValue = atIndex->data;
        delete [] atIndex;
    }
    listLength--;
}

void LinkedList::RecursiveReverse(Node *cursor, Node *next) {
    if(next){
        RecursiveReverse(next, next->next);
        next->next = cursor;
    } else {
        first->next = NULL; // current first will become the end
        first = cursor; // the end is now the first
    }
}

void LinkedList::Reverse(){
    RecursiveReverse(first, first->next);
}

int LinkedList::Find(int value) const{
    Node * cursor = first;
    int index;
    for(index = 0; index < listLength; index++){
        if( value == cursor->data )
            break;
        cursor = cursor->next;
    }

    if(index == listLength)
        index = -1;

    return index;
}

int LinkedList::GetValue(int index) const{
    Node * cursor = first;
    for (int i = 0; i < index; i++){
        cursor = cursor->next;
    }
    return cursor->data;
}

LinkedList LinkedList::operator+(const LinkedList &rhs) const {

    LinkedList concat = LinkedList();

    Node * node = first;
    while(node){
        concat.InsertBack(node->data);
        node = node->next;
    }

    for (int index = 0; index < rhs.GetLength(); index++)
        concat.InsertBack(rhs.GetValue(index));

    return concat;
}

