#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:

    void swapItems(vector<char>& s, int a, int b){
        if(a < b){
        char temp;
        temp = s.at(a);
        s.at(a) = s.at(b);
        s.at(b) = temp;
        swapItems(s, a+1, b-1);
        }
    }
    void reverseString(vector<char>& s) {
        if(s.size()>1)
            swapItems(s, 0 , s.size() - 1);
    }
    Solution(vector <char>& s){
        reverseString(s);
        for(char c:s)
            cout << c;
    }
};

int main(){
    vector<char> s = {'a', 'b', 'c', 'd', 'e'};
    Solution sol = Solution(s);
    
    return 0;
}