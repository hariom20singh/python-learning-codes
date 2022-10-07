#include <iostream>
using namespace std;
void linearsearch(int arr[], int n, int key)
{
    for (int i = 0; i < n; i++)
    {
        if (arr[i] == key)
        {
            cout << "element found at " << i;
        }
    }
}

int main()
{
    int n;
    cout << "enter no. of array you want";
    cin >> n;
    int arr[n];
    cout << "enter the array :- ";
    for (int i = 0; i < n; i++)
    {

        cin >> arr[i];
    }

    int key;
    cout << "enter the key :-";
    cin >> key;
    linearsearch(arr, n, key);

    return 0;
}