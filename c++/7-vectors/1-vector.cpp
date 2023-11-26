#include<iostream>
#include<vector>
using namespace std;
  
int main()
{
    vector<int> vect{ 10, 20, 30 };
    int arr[4] = {20, 24, 28, 32}; 
    vector<int> vect1(vect.begin(), vect.end());
    for(int i= 0; i<vect1.size(); i++){
        cout << vect1[i] << endl;
    }
    cout << vect1[7] << endl;
    for (int x : vect1)
        cout << x << " ";
  
    return 0;
}