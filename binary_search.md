# Binary Search

## Index

+ [Binary Search Template](#Binary-Search-Template)
+ [Kth largest element in an array](#Kth-largest-element-in-an-array)
+ [Kth Smallest Element in a Sorted Matrix](#)
+ [K Closest Points to Origin](#)

## Binary Search Template

+ Template #1

Classic binary search

```c++
int binarySearch(vector<int>& nums, int target){
  if(nums.size() == 0)
    return -1;

  int left = 0, right = nums.size() - 1;
  while(left <= right){
    // Prevent (left + right) overflow
    int mid = left + (right - left) / 2;
    if(nums[mid] == target){ return mid; }
    else if(nums[mid] < target) { left = mid + 1; }
    else { right = mid - 1; }
  }

  // End Condition: left > right
  return -1;
}
```

Search range by finding first and last occurrence 
```c++
vector<int> searchRange(int A[], int n, int target) {
    int i = 0, j = n - 1;
    vector<int> ret(2, -1);
    // Search for the left one
    while (i < j)
    {
        int mid = (i + j) /2;
        if (A[mid] < target) i = mid + 1;
        else j = mid;
    }
    if (A[i]!=target) return ret;
    else ret[0] = i;

    // Search for the right one
    j = n-1;  // We don't have to set i to 0 the second time.
    while (i < j)
    {
        int mid = (i + j) /2 + 1;	// Make mid biased to the right
        if (A[mid] > target) j = mid - 1;
        else i = mid;				// So that this won't make the search range stuck.
    }
    ret[1] = j;
    return ret;
}
```

+ Key Attributes:
    + Most basic and elementary form of Binary Search
    + Search Condition can be determined without comparing to the element's neighbors (or use specific elements around
      it)
    + No post-processing required because at each step, you are checking to see if the element has been found. If you
      reach the end, then you know the element is not found

+ Distinguishing Syntax:
    + Initial Condition: left = 0, right = length-1
    + Termination: left > right
    + Searching Left: right = mid-1
    + Searching Right: left = mid+1

+ Template 2

Advanced form of Binary Search. It is used to search for an element or condition which requires accessing the current
index and its immediate right neighbor's index in the array

```c++
int binarySearch(vector<int>& nums, int target){
  if(nums.size() == 0)
    return -1;

  int left = 0, right = nums.size();
  while(left < right){
    // Prevent (left + right) overflow
    int mid = left + (right - left) / 2;
    if(nums[mid] == target){ return mid; }
    else if(nums[mid] < target) { left = mid + 1; }
    else { right = mid; }
  }

  // Post-processing:
  // End Condition: left == right
  if(left != nums.size() && nums[left] == target) return left;
  return -1;
}
```

+ Key Attributes:
    + An advanced way to implement Binary Search.
    + Search Condition needs to access element's immediate right neighbor
    + Use element's right neighbor to determine if condition is met and decide whether to go left or right
    + Gurantees Search Space is at least 2 in size at each step
    + Post-processing required. Loop/Recursion ends when you have 1 element left. Need to assess if the remaining
      element meets the condition.

+ Distinguishing Syntax:
    + Initial Condition: left = 0, right = length
    + Termination: left == right
    + Searching Left: right = mid
    + Searching Right: left = mid+1

+ Template 3

Another unique form of Binary Search. It is used to search for an element or condition which requires accessing the
current index and its immediate left and right neighbor's index in the array.

```c++
int binarySearch(vector<int>& nums, int target){
    if (nums.size() == 0)
        return -1;

    int left = 0, right = nums.size() - 1;
    while (left + 1 < right){
        // Prevent (left + right) overflow
        int mid = left + (right - left) / 2;
        if (nums[mid] == target) {
            return mid;
        } else if (nums[mid] < target) {
            left = mid;
        } else {
            right = mid;
        }
    }

    // Post-processing:
    // End Condition: left + 1 == right
    if(nums[left] == target) return left;
    if(nums[right] == target) return right;
    return -1;
}
```

+ Key Attributes:
  + An alternative way to implement Binary Search
  + Search Condition needs to access element's immediate left and right neighbors
  + Use element's neighbors to determine if condition is met and decide whether to go left or right
  + Gurantees Search Space is at least 3 in size at each step
  + Post-processing required. Loop/Recursion ends when you have 2 elements left. Need to assess if the remaining elements meet the condition.

+ Distinguishing Syntax:
  + Initial Condition: left = 0, right = length-1
  + Termination: left + 1 == right
  + Searching Left: right = mid
  + Searching Right: left = mid

## Kth largest element in an array

```c++
    public int findKthLargest(int[] nums, int k) {
        k = nums.length - k;
        int lo = 0;
        int hi = nums.length - 1;
        while (lo < hi) {
            final int j = partition(nums, lo, hi);
            if(j < k) {
                lo = j + 1;
            } else if (j > k) {
                hi = j - 1;
            } else {
                break;
            }
        }
        return nums[k];
    }

    private int partition(int[] nums, int lo, int hi) {
        int pivot = nums[hi];
        int i = lo;
        for (int j = lo; j < hi; j++) {
            if (nums[j] <= pivot) {
                swap(nums, i, j);
                i++;
            }
        }
        swap(nums, i, hi);
        return i;
    }
```

## Kth Smallest Element in a Sorted Matrix

-

Leetcode: [Solution](https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/discuss/85173/Share-my-thoughts-and-Clean-Java-Code)

- Approach 1:

```java
public class Solution {
    public int kthSmallest(int[][] matrix, int k) {
        int n = matrix.length;
        PriorityQueue<Tuple> pq = new PriorityQueue<Tuple>();
        for(int j = 0; j <= n-1; j++) pq.offer(new Tuple(0, j, matrix[0][j]));
        for(int i = 0; i < k-1; i++) {
            Tuple t = pq.poll();
            if(t.x == n-1) continue;
            pq.offer(new Tuple(t.x+1, t.y, matrix[t.x+1][t.y]));
        }
        return pq.poll().val;
    }
}

class Tuple implements Comparable<Tuple> {
    int x, y, val;
    public Tuple (int x, int y, int val) {
        this.x = x;
        this.y = y;
        this.val = val;
    }
    
    @Override
    public int compareTo (Tuple that) {
        return this.val - that.val;
    }
}
```

- Approach 2:

```java
public class Solution {
    public int kthSmallest(int[][] matrix, int k) {
        int lo = matrix[0][0], hi = matrix[matrix.length - 1][matrix[0].length - 1] + 1;//[lo, hi)
        while(lo < hi) {
            int mid = lo + (hi - lo) / 2;
            int count = 0,  j = matrix[0].length - 1;
            for(int i = 0; i < matrix.length; i++) {
                while(j >= 0 && matrix[i][j] > mid) j--;
                count += (j + 1);
            }
            if(count < k) lo = mid + 1;
            else hi = mid;
        }
        return lo;
    }
}
```

## [K Closest Points to Origin](https://leetcode.com/problems/k-closest-points-to-origin/)

+ [[Java] Three solutions to this classical K-th problem.](https://leetcode.com/problems/k-closest-points-to-origin/discuss/220235/Java-Three-solutions-to-this-classical-K-th-problem.)