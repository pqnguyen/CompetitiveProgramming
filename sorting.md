# Sorting

## Index

+ [Merge Sort](#Merge-sort)
+ [Quick Sort](#Quick-sort)
+ [Heap Sort](#Heap-sort)
+ [Patience Sort](#Patience-sort)

## Merge sort

```c++
void merge_sort(int a[], int length) {
    merge_sort(a, 0, length-1);
}

void merge_sort(int a[], int low, int high) {
    if (low >= high)                  //Base case: 1 value to sort->sorted
      return;                         //(0 possible only on initial call)
    else {
      int mid = (low + high)/2;       //Approximate midpoint*
      merge_sort(a, low, mid);        //Sort low to mid part of array
      merge_sort(a, mid+1, high);     //Sort mid+1 to high part of array
      merge(a, low, mid, mid+1,high); //Merge sorted subparts of array
    }
}

void merge(int a[], int left_low, int left_high, int right_low, int right_high) 
{ 
    int length = right_high-left_low+1;
    int temp[length];
    int left = left_low;
    int right = right_low;
    for (int i = 0; i < length; ++i) { 
        if (left > left_high)
            temp[i] = a[right++];
        else if (right > right_high)
            temp[i] = a[left++];
        else if (a[left] <= a[right])
            temp[i] = a[left++];
        else
            temp[i] = a[right++]; 
    }
    
    for (int i=0; i< length; ++i) 
        a[left_low++] = temp[i];
}
```

## Quick sort

```c++
int partition(int A[], int start, int end) {
    int wall = start;
    for (int i = start; i < end; i++) {
        if (A[i] < A[end]) {
            swap(A[i], A[end]);
            wall++;
        }
    }
    swap(A[wall], A[end]);
    return wall;
}

void quick_sort ( int A[ ] ,int start , int end ) {
   if( start < end ) {
        //stores the position of pivot element
         int piv_pos = partition (A,start , end ) ;     
         quick_sort (A,start , piv_pos -1);    //sorts the left side of pivot.
         quick_sort ( A,piv_pos +1 , end) ; //sorts the right side of pivot.
   }
}
```

```c++
Let’s see the randomized version of the partition function :
int rand_partition ( int A[ ] , int start , int end ) {
    //chooses position of pivot randomly by using rand() function .
     int random = start + rand( )%(end-start +1 ) ;

      swap ( A[random] , A[end]) ;        //swap pivot with last element.
     return partition(A,start ,end) ;       //call the above partition function
}
```

## Heap Sort

```c++
#include <iostream>
using namespace std;
  
// function to heapify the tree
void heapify(int arr[], int n, int root)
{
   int largest = root; // root is the largest element
   int l = 2*root + 1; // left = 2*root + 1
   int r = 2*root + 2; // right = 2*root + 2
  
   // If left child is larger than root
   if (l < n && arr[l] > arr[largest])
   largest = l;
  
   // If right child is larger than largest so far
   if (r < n && arr[r] > arr[largest])
   largest = r;
  
   // If largest is not root
   if (largest != root)
      {
      //swap root and largest
      swap(arr[root], arr[largest]);
  
      // Recursively heapify the sub-tree
      heapify(arr, n, largest);
      }
}
  
// implementing heap sort
void heapSort(int arr[], int n)
{
   // build heap
   for (int i = n / 2 - 1; i >= 0; i--)
   heapify(arr, n, i);
  
   // extracting elements from heap one by one
   for (int i=n-1; i>=0; i--)
   {
      // Move current root to end
      swap(arr[0], arr[i]);
  
      // again call max heapify on the reduced heap
      heapify(arr, i, 0);
   }
}
```

## Patience sort

+ [Theory](https://www.cs.princeton.edu/courses/archive/spring13/cos423/lectures/LongestIncreasingSubsequence.pdf)
+ [Implementation](https://rosettacode.org/wiki/Sorting_algorithms/Patience_sort#Go)