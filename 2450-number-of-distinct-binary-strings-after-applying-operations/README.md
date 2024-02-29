<h2><a href="https://leetcode.com/problems/number-of-distinct-binary-strings-after-applying-operations/">2450. Number of Distinct Binary Strings After Applying Operations</a></h2><h3>Medium</h3><hr><div><p>You are given a <strong>binary</strong> string <code>s</code> and a positive integer <code>k</code>.</p>

<p>You can apply the following operation on the string <strong>any</strong> number of times:</p>

<ul>
	<li>Choose any substring of size <code>k</code> from <code>s</code> and <strong>flip</strong> all its characters, that is, turn all <code>1</code>'s into <code>0</code>'s, and all <code>0</code>'s into <code>1</code>'s.</li>
</ul>

<p>Return <em>the number of <strong>distinct</strong> strings you can obtain</em>. Since the answer may be too large, return it <strong>modulo</strong> <code>10<sup>9</sup> + 7</code>.</p>

<p><strong>Note</strong> that:</p>

<ul>
	<li>A binary string is a string that consists <strong>only</strong> of the characters <code>0</code> and <code>1</code>.</li>
	<li>A substring is a contiguous part of a string.</li>
</ul>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre><strong>Input:</strong> s = "1001", k = 3
<strong>Output:</strong> 4
<strong>Explanation:</strong> We can obtain the following strings:
- Applying no operation on the string gives s = "1001".
- Applying one operation on the substring starting at index 0 gives s = "<u><strong>011</strong></u>1".
- Applying one operation on the substring starting at index 1 gives s = "1<u><strong>110</strong></u>".
- Applying one operation on both the substrings starting at indices 0 and 1 gives s = "<u><strong>0000</strong></u>".
It can be shown that we cannot obtain any other string, so the answer is 4.</pre>

<p><strong class="example">Example 2:</strong></p>

<pre><strong>Input:</strong> s = "10110", k = 5
<strong>Output:</strong> 2
<strong>Explanation:</strong> We can obtain the following strings:
- Applying no operation on the string gives s = "10110".
- Applying one operation on the whole string gives s = "01001".
It can be shown that we cannot obtain any other string, so the answer is 2.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= k &lt;= s.length &lt;= 10<sup>5</sup></code></li>
	<li><code>s[i]</code> is either <code>0</code> or <code>1</code>.</li>
</ul>
</div>