<p>Slicing is used to get multiple characters (a substring) from a string. Its syntax is similar to that of indexing, but instead of just one index you use two indices (numbers) separated by a colon, e.g. <code>str[ind1:ind2]</code> .</p><h5>Example</h5><pre><code>
str[start:end] # items start through end-1
str[start:]    # items start through the rest of the array
str[:end]      # items from the beginning through end-1
str[:]         # a copy of the whole array
</code></pre>
<p>Use slicing to get <code>"Python"</code> from the <code>monty_python</code> variable.</p><div class="hint">You can leave one or both indices empty.</div>

