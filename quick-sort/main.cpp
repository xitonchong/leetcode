#include<bits/stdc++.h>

using namespace std;

void swap(int* a, int* b)
{
    int t = *a;
    *a = *b; 
    *b = t;
}

int partition(int start, int end, int arr[])
{
    int pivot = arr[end];
    int i = (start-1);
    for (int j=start; j<=end; j++)
    {
        if (arr[j] < pivot)
        {
            i++;
            swap(&arr[i], &arr[j]);
        }
    }
    swap(&arr[i+1], &arr[end]);
    return (i+1);
}


void quickSort(int arr[], int start, int end)
{
    if (start < end)
    {
        int p = partition(start, end, arr);

        quickSort(arr, start, p-1);
        quickSort(arr, p+1, end);
    }
}

void printArray(int arr[], int size)
{
    for (int i=0; i<size; i++)
        cout << arr[i] << " " ;
    cout << endl;
}

int main()
{
    int arr[] = {10, 8, 8,9,1,5, 12, 18};
    int n=sizeof(arr)/sizeof(arr[0]);

    quickSort(arr, 0, n-1);

    printArray(arr, n);
}




