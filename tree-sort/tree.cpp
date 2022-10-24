#include<bits/stdc++.h>

//difference between struct and class
/*
    the only difference between a struct and class in C++ is the default accessibility of member 
    variables and methods.  In a struct they are public; in a class they are private. 
*/
using namespace std;


struct Node
{
    int key;
    struct Node *left, *right;
};

//a utility function to create a new BST Node
struct Node *newNode(int item)
{
    struct Node *temp = new Node;
    temp->key = item;
    temp->left = temp->right = NULL;
    return temp;
}

//stores inorder traversal of BST
//in arr[]
void storeSorted(Node *root, int arr[], int &i)
{
    if (root != NULL)
    {
        storeSorted(root->left, arr, i);
        arr[i++] = root->key;
        storeSorted(root->right, arr, i);
    }
}


// a utility function to insert a new node with
// a given key in BST

Node* insert(Node* node, int key)
{
    if (node == NULL) return newNode(key);
    
    if (key < node->key)
        node->left = insert(node->left, key);
    else if (key > node->key)
        node->right = insert(node->right, key);

    //return the unchanged node pointer
    return node;
}

//this function sorts arr[0..n-1]using tree sort
void treeSort(int arr[], int n)
{
    struct Node *root = NULL;

    //construct the BST
    root = insert(root, arr[0]);
    for (int i=1; i<n; i++)
        root = insert(root, arr[i]);

    //store inoder traversal of the BST
    int i =0;
    storeSorted(root, arr, i);
}


// Driver Program to test above functions
int main()
{
    //create input array
    int arr[] = {5, 4, 7, 2, 11};
    int n = sizeof(arr)/sizeof(arr[0]);
 
    treeSort(arr, n);
 
    for (int i=0; i<n; i++)
       cout << arr[i] << " ";
 
    return 0;
}