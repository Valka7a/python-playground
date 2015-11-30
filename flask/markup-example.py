from flask import Markup

Markup('<strong>Hello %s!</strong>') % '<blink>hacker</blink>'
# will produce
Markup(u'<strong>Hello &lt;blink&gt;hacker&lt;/blink&gt;!</strong>')

Markup.escape('<blink>hacker</blink>')
# will retrun
Markup(u'&lt;blink&gt;hacker&lt;/blink&gt;')

Markup('<em>Marked up</em> &raquo; HTML').striptags()
u'Marked up \xbb HTML'
