---
layout: post
title:  "IceCTF writeup - Contract"
date:   2016-08-19 18:13:49 +0200
categories: writeup
---
The challenge started out very easy. But this was not to be so. Soon enough it became quite apparent.

{% highlight ruby %}
def print_hi(name)
  puts "Hi, #{name}"
end
print_hi('Tom')
#=> prints 'Hi, Tom' to STDOUT.
{% endhighlight %}

Somewhere deep inside there was something. I could feel it. I decided to leave it for later and turned to the next system.