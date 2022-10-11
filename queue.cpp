#include<iostream>
#include<queue>
using namespace std;

void print(queue<char>que)
{
    queue<char>c=que;
    while(!c.empty())
    {
        cout<<c.front()<<" ";
        c.pop();
    }
    cout<<endl;
}
int main(){
    queue<char>q;
    q.push('a');
    q.push('b');
    q.push('c');
    print(q);

    cout<<q.back()<<endl;
    q.pop();
    print(q);
    return 0;
}