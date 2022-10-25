#include<iostream>
using namespace std;
int main()
{
    int i,n;
    cin>>n;
    int sum=0;
    for(i=1;i<=n;i++)
    {
        if(n%i==0)
        {
            sum+=i;
        }
    }
    if(sum==2*n)
    
        cout<<"perfect number";
    
    else 
    cout<<"not perfect";
    return 0;
}