# [Segment Tree]()
<div style="text-align:center">
    <img src="https://he-s3.s3.amazonaws.com/media/uploads/a0c7f90.jpg" alt="drawing" width="500"/>
    <img src="https://he-s3.s3.amazonaws.com/media/uploads/aad673e.jpg" alt="drawing" width="350"/>
</div>


>>>
```c++
void build(int node, int start, int end)
{
    if(start == end)
    {
        // Leaf node will have a single element
        tree[node] = A[start];
    }
    else
    {
        int mid = (start + end) / 2;
        // Recurse on the left child
        build(2*node, start, mid);
        // Recurse on the right child
        build(2*node+1, mid+1, end);
        // Internal node will have the sum of both of its children
        tree[node] = tree[2*node] + tree[2*node+1];
    }
}
```
Complexity: O(N).<br/>
<br/>

```c++
void update(int node, int start, int end, int idx, int val)
{
    if(start == end)
    {
        // Leaf node
        A[idx] += val;
        tree[node] += val;
    }
    else
    {
        int mid = (start + end) / 2;
        if(start <= idx and idx <= mid)
        {
            // If idx is in the left child, recurse on the left child
            update(2*node, start, mid, idx, val);
        }
        else
        {
            // if idx is in the right child, recurse on the right child
            update(2*node+1, mid+1, end, idx, val);
        }
        // Internal node will have the sum of both of its children
        tree[node] = tree[2*node] + tree[2*node+1];
    }
}
```
Complexity: O(LogN).<br/>
<br/>

```c++
int query(int node, int start, int end, int l, int r)
{
    if(r < start or end < l)
    {
        // range represented by a node is completely outside the given range
        return 0;
    }
    if(l <= start and end <= r)
    {
        // range represented by a node is completely inside the given range
        return tree[node];
    }
    // range represented by a node is partially inside and partially outside the given range
    int mid = (start + end) / 2;
    int p1 = query(2*node, start, mid, l, r);
    int p2 = query(2*node+1, mid+1, end, l, r);
    return (p1 + p2);
}
```
Complexity: O(LogN).<br/>
<br/>

# [Segment tree with single element modifications](https://codeforces.com/blog/entry/18051)

<div style="text-align:center">
    <img src="https://codeforces.com/predownloaded/0f/52/0f52998b96c8a0f55d379fd5c990e5d2d66d1ab2.png" alt="drawing" width="500"/>
</div>

```c++
const int N = 1e5;  // limit for array size
int n;  // array size
int t[2 * N];

void build() {  // build the tree
  for (int i = n - 1; i > 0; --i) t[i] = t[i<<1] + t[i<<1|1];
}

void modify(int p, int value) {  // set value at position p
  for (t[p += n] = value; p > 1; p >>= 1) t[p>>1] = t[p] + t[p^1];
}

int query(int l, int r) {  // sum on interval [l, r)
  int res = 0;
  for (l += n, r += n; l < r; l >>= 1, r >>= 1) {
    if (l&1) res += t[l++];
    if (r&1) res += t[--r];
  }
  return res;
}

int main() {
  scanf("%d", &n);
  for (int i = 0; i < n; ++i) scanf("%d", t + n + i);
  build();
  modify(0, 1);
  printf("%d\n", query(3, 11));
  return 0;
}
```

## [Dynamic Segtree](https://codeforces.com/blog/entry/60837)
```c++
gp_hash_table<int, int, chash> seg;

int get(int x) { return (seg.find(x) == seg.end()) ? 0 : seg[x]; }
void modify(int p, int val) {
    for (seg[p += N] = val; p > 0; p >>= 1) {
        seg[p >> 1] = get(p) + get(p ^ 1);
    }
}

int query(int l, int r) {
    int res = 0;
    for (l += N, r += N; l < r; l >>= 1, r >>= 1) {
        if (l & 1)
            res += get(l++);
        if (r & 1)
            res += get(--r);
    }
    return res;
}
```

## [An efficient way to strengthen up your segment tree.](https://codeforces.com/blog/entry/13703)
## [Segment Tree and Lazy Propagation](https://www.hackerearth.com/practice/notes/segment-tree-and-lazy-propagation/)