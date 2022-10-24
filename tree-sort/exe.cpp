#include<bits/stdc++.h>

//difference between struct and class
/*
    the only difference between a struct and class in C++ is the default accessibility of member 
    variables and methods.  In a struct they are public; in a class they are private. 
*/
using namespace std;

// construct a node strcutue using sturc


struct Node {
    int key;
    struct Node *left, *right;  //if we want node to have left, right properties? pointers to struct node
};


struct Node *newNode(int item)  // a special constructor for insert
{
    struct Node *temp = new Node;
    temp->key = item;
    temp->left = temp->right = NULL;
    return temp;

}


Node* insert(Node* node, int key)
{
    if (node==NULL) return newNode(key);

    if (key < node->key)
        node->left = insert(node->left, key);
    else if (key > node->key)
        node->right = insert(node->right, key);

    
    return node;
}

void inorder(Node* root, int arr[], int &i)  // i pass by reference, arr to store 
{
    if (root != NULL)
    {
        inorder(root->left, arr, i);
        arr[i++] = root->key;
        inorder(root->right, arr, i);
    }
}

void treeSort(int arr[], int n) // n: length of array
{
    struct Node *root = NULL;
    root = insert(root, arr[0]);

    for (int i=1; i<n; i++)
        root = insert(root, arr[i]);

    // store in array
    int i = 0;
    inorder(root, arr, i);
}

int main(){
    //create in put array
    int arr[] = {5,5,7,8,9, 19};
    int n = sizeof(arr)/sizeof(arr[0]);
    treeSort(arr, n);

    for (int i=0; i<n; i++)
        cout << arr[i] << " ";
    
    return 0;

}