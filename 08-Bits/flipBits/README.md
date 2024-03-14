### Question:

Given numbers n and k, toggle kth bit of number n. Rightmost bit is considered 0th bit and so on.

### Solution:

To flip a bit, use `xor` operation.

<table>
  <tr>
    <th>x1</th>
    <th>x2</th>
    <th>x1 XOR x2</th>
  </tr>
  <tr>
    <td>0</td>
    <td>0</td>
    <td>0</td>
  </tr>
  <tr>
    <td>0</td>
    <td>1</td>
    <td>1</td>
  </tr>
  <tr>
    <td>1</td>
    <td>0</td>
    <td>1</td>
  </tr>
  <tr>
    <td>1</td>
    <td>1</td>
    <td>0</td>
  </tr>
</table>


So, first create a mask and shift the i by k; do `xor` operation between `N` and created `mask`.
