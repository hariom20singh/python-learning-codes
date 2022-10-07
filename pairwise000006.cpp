#include <bits/stdc++.h>
using namespace std;


void maxProduct(int arr[], int n)
{
    if (n < 2)
    {
        cout << "No pairs exists\n";
        return;
    }

 
    int a = arr[0], b = arr[1];

    
    
    for (int i = 0; i < n; i++)
        for (int j = i + 1; j < n; j++)
            if (arr[i] * arr[j] > a * b)
                a = arr[i], b = arr[j];

    cout << "Max product pair is {" << a << ", "
         << b << "}";
}

int main()
{
    int arr[] = {1, 4, 3, 6, 7, 0};
    int n = sizeof(arr) / sizeof(arr[0]);
    maxProduct(arr, n);
    return 0;
}
