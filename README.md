<h1>formatflick</h1>
<p>
    This Python module provides a convenient way to convert between different file formats.
</p>
<h2>Installation</h2>
<p>
    Right now the module cannot be installed regular 
<code>pip install</code>. instead, use the following command in your terminal(for linux & mac users)/ cmd(windows users)
<br/><code>pip install -i https://test.pypi.org/simple/ formatflick</code>
<br/>
To install a specific version type:<br/>
<code>pip install -i https://test.pypi.org/simple/ formatflick==version_no</code>
<br/>
For information you can visit the <a href="https://test.pypi.org/project/formatflick/">TestPyPI link</a>. There are certain dependencies for this module such as
<ol>
<li>Pandas</li>
<li>lxml</li>
</ol>
Both can be downloaded as separate pip module.
<h2>Usage</h2>
Using this module is easy in your python code. Below is an example which shows how you can use the module
<pre>
from formatflick import formatflick

file_path = "samplecsv.csv" # file path

obj = formatflick.Formatflick(test_path, destination_extension=".json") #initialize the module

obj.convert() # convert function to convert to specified file extension
</pre>