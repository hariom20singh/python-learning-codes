#include<bits/stdc++.h>
using namespace std;
class Node{
  public:
  int data;
  Node* next;
  Node* prev;
  Node(int data)
  {
    this->data=data;
    this->next=NULL;
    this->prev=NULL;
  }

  ~Node()
  {
    int value=this->data;
    if(this->next!=NULL)
    {
        delete next;
        // this->next=NULL;
    }
    cout<<"Memory is free for : "<<value<<endl;
  }
};
void insertAtHead(Node* &tail,Node* &head,int d)
{   if(head==NULL)
    {
        Node* temp=new Node(d);
        head=temp;
        tail=temp;
    }
    else{
    Node* temp=new Node(d);
    head->prev=temp;
    temp->next=head;
    head=temp;
    }
}
void insertAtTail(Node* &tail,Node* &head,int d)
{   
    if(tail==NULL)
    {
        Node* temp=new Node(d);
        tail=temp;
        head=temp;
    }
    else{
    Node* temp=new Node(d);
    tail->next=temp;
    temp->prev=tail;
    tail=temp;
    }
}
void insertAtPosition(Node* & tail,Node* &head,int position,int d)
{
    if(position==1)
    {
        insertAtHead(tail,head,d);
        return;
    }
    int cnt=1;
    Node* temp=head;
    while(cnt<position-1)
    {
        temp=temp->next;
        cnt++;
    }
    if(temp->next==NULL)
    {
        insertAtTail(tail,head,d);
        return;
    }
    Node* nodeToInsert=new Node(d);
    nodeToInsert->next=temp->next;
    temp->next->prev=nodeToInsert;
    temp->next=nodeToInsert;
    nodeToInsert->prev=temp;
}
void deleteAtPosition(Node*& head,int position)
{
    if(position==1)
    {
        Node* temp=head;
        temp->next->prev=NULL;
        head=head->next;
        temp->next=NULL;
        delete temp;  
    }
    else{
        Node* previous=NULL;
        Node* curr=head;
        int cnt=1;
        while(cnt<position)
        {
            previous=curr;
            curr=curr->next;
            cnt++;
        }
        curr->prev=NULL;
        previous->next=curr->next;
        curr->next=NULL;
        delete curr;
    }
}
void print(Node* &head)
{
    Node*temp=head;
    while(temp!=NULL)
    {
        cout<<temp->data<<" ";
        temp=temp->next;
    }
    cout<<endl;
}
int main(){
    
    Node* head=NULL;
    Node* tail=NULL;
    
    insertAtHead(tail,head,3);
    print(head);
    insertAtTail(tail,head,7);
    print(head);
    insertAtTail(tail,head,9);
    print(head);
    insertAtPosition(tail,head,1,1);
    print(head);
    insertAtPosition(tail,head,5,11);
    print(head);
    insertAtPosition(tail,head,4,15);
    print(head);
    deleteAtPosition(head,2);
    print(head);
    return 0;
}