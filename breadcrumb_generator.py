'''
Codewars - Breadcrumb Generator

Last Updated: 2016-Dec-10
First Created: 2016-Dec-09
Python 3.5
Chris

https://www.codewars.com/kata/breadcrumb-generator/

Description:

As breadcrumb menùs are quite popular today, I won't digress much on explaining them, leaving the wiki link doing the dirty work in my place.

What might not be so trivial is to get a decent breadcrumb from your current url: for this kata your purpose is to create a function that takes a url,
strips the first part (labeling it always HOME) and then builds it making each element
but the last a <a> element linking to the relevant path; last has to be a <span> element getting the active class.

All elements need to be turned into uppercase and separated by a separator, given as the second parameter of the function;
the last element can terminate in some common extension like .html, .htm, .php or .asp;
if the name of the last element is index.something, you treat it as if it wasn't there, sending users automatically to the upper folder.

A few examples can be more helpful than thousands of explanations, so here you have them:

generate_bc("mysite.com/pictures/holidays.html", " : ") == '<a href="/">HOME</a> : <a href="/pictures/">PICTURES</a> : <span class="active">HOLIDAYS</span>'
generate_bc("www.codewars.com/users/GiacomoSorbi", " / ") == '<a href="/">HOME</a> / <a href="/users/">USERS</a> / <span class="active">GIACOMOSORBI</span>'
generate_bc("www.microsoft.com/docs/index.htm", " * ") == '<a href="/">HOME</a> * <span class="active">DOCS</span>'

Seems easy enough? Well, probably not, but we have now a last extra rule: if one element (other than the root/home) is longer than 30 characters,
you have to shorten it, acronymizing it (i.e.: taking just the initials of every word); url will be always given in the format
this-is-an-element-of-the-url and you should ignore words in this array while acronymizing:
["the","of","in","from","by","with","and", "or", "for", "to", "at", "a"]; url composed of more words
separated by -, but equal or less than 30 characters long, needs to be just uppercased with hyphens replaced by spaces.

Ignore anchors (www.url.com#lameAnchorExample) and parameters (www.url.com?codewars=rocks&pippi=rocksToo) when present.

Examples:

generate_bc("mysite.com/very-long-url-to-make-a-silly-yet-meaningful-example/example.htm", " > ") == '<a href="/">HOME</a> >
<a href="/very-long-url-to-make-a-silly-yet-meaningful-example/">VLUMSYME</a> > <span class="active">EXAMPLE</span>'

generate_bc("www.very-long-site_name-to-make-a-silly-yet-meaningful-example.com/users/giacomo-sorbi", " + ") ==
'<a href="/">HOME</a> + <a href="/users/">USERS</a> + <span class="active">GIACOMO SORBI</span>'

You will always be provided valid url to webpages in common formats, so you probably shouldn't bother validating them.
If you like to test yourself with actual work/interview related kata, please also consider this one about building a string filter for Angular.js

Special thanks to the colleague that, seeing my code and commenting that I worked on that as if it was I was on CodeWars, made me realize that it could be indeed a good idea for a kata :)

'''

def generate_bc(url, separator):
    '''
    See above description. Url and seperator are both strings.
    '''

    ignore_words = ["the","of","in","from","by","with","and", "or", "for", "to", "at", "a"]

    if '//' in url:
        url = url.split('//')
        ans = url[1].split('/')
    else:
        ans = url.split('/')

    # change last element to active (if not index)

    while 'index' in ans[-1]:
        ans.pop()

    # change first element to home (UPPER)
    if len(ans) > 1:
        ans[0] = '<a href="/">HOME</a>'
    else:
        return '<span class="active">HOME</span>'

    anchor_number = [idx for idx, character in enumerate(ans[-1]) if not character.isalnum() and character != '-']

    if anchor_number:
        ans[-1] = ans[-1][:anchor_number[0]]

    if len(ans[-1]) <= 30:
        ans[-1] = '<span class="active">' + ans[-1].upper().split('.')[0].replace('-', ' ') + '</span>'
    else:
        ans[-1] = '<span class="active">' + ''.join([word[0].upper() for word in ans[-1].split('-') if word not in ignore_words]) + '</span>'

    new_mid = []
    full_string = ''

    for section in ans[1:-1]:
        full_string += section.lower() + '/'
        print(section, len(section))
        if len(section) <= 30:
            new_mid.append('<a href="/%s">' %(full_string) + section.upper().replace('-', ' ') + '</a>')
        else:
            new_mid.append('<a href="/%s">' %(full_string) + ''.join([word[0].upper() for word in section.split('-') if word not in ignore_words]) + '</a>')

    if ans[-1] == '<span class="active"></span>':
        return '<span class="active">HOME</span>'

    ans = [ans[0]] + new_mid + [ans[-1]]

    sep_join = separator
    return sep_join.join(ans)

def generate_bc_re(url, separator):
    '''
    anter69's solution.
    '''
    from re import sub
    ignoreList = ["THE", "OF", "IN", "FROM", "BY", "WITH", "AND",  "OR",  "FOR",  "TO",  "AT",  "A"]

    # remove leading http(s):// and trailing /
    url = sub("https?://", "", url.strip("/"))

    # skip index files
    url = sub("/index\..+$", "", url)

    # split url for processing
    url = url.split("/")

    # remove file extensions, anchors and parameters
    url[-1] = sub("[\.#\?].*", "", url[-1])

    # first element is always "home"
    menu = ["HOME"]
    # generate breadcrumb items
    for item in url[1:]:
        # replace dashes and set to uppercase
        item = sub("-", " ", item.upper())
        # create acronym if too long
        if len(item) > 30:
            item = "".join([w[0] for w in item.split() if w not in ignoreList])
        menu.append(item)

    # generate paths
    path = ["/"]
    for i in range(len(url) - 1):
        path.append(path[i] + url[i+1] + "/")

    # generate html code
    html = []
    for i in range(len(url) - 1):
        html.append("<a href=\"" + path[i] + "\">" + menu[i] +"</a>")
    html.append("<span class=\"active\">" + menu[-1] +"</span>")

    return separator.join(html)


def testing():
    # my temp tests
    #print(generate_bc("mysite.com/very-long-url/example.htm", " > "))
    #print(generate_bc("mysite.com/very-long-url-to-make-a-silly-or-yet-meaningful-example/example.htm", " > "))
    #print(generate_bc("mysite.com/pictures/index.html", " : "), '<a href="/">HOME</a> : <a href="/pictures/">PICTURES</a> : <span class="active">HOLIDAYS</span>')

    print(generate_bc('https://hello/index.html',  '>' ))

    '''
    # their tests
    print('Test 1')
    print(generate_bc("mysite.com/pictures/holidays.html", " : "))
    print('<a href="/">HOME</a> : <a href="/pictures/">PICTURES</a> : <span class="active">HOLIDAYS</span>')
    print(generate_bc("mysite.com/pictures/holidays.html", " : ") == '<a href="/">HOME</a> : <a href="/pictures/">PICTURES</a> : <span class="active">HOLIDAYS</span>')

    print('Test 2')
    print(generate_bc("www.codewars.com/users/GiacomoSorbi?ref=CodeWars", " / "))
    print('<a href="/">HOME</a> / <a href="/users/">USERS</a> / <span class="active">GIACOMOSORBI</span>')
    print(generate_bc("www.codewars.com/users/GiacomoSorbi?ref=CodeWars", " / ") == '<a href="/">HOME</a> / <a href="/users/">USERS</a> / <span class="active">GIACOMOSORBI</span>')

    print('Test 3')
    print(generate_bc("www.microsoft.com/docs/index.htm#top", " * "))
    print('<a href="/">HOME</a> * <span class="active">DOCS</span>')
    print(generate_bc("www.microsoft.com/docs/index.htm#top", " * ") == '<a href="/">HOME</a> * <span class="active">DOCS</span>')

    print('Test 4')
    print(generate_bc("mysite.com/very-long-url-to-make-a-silly-yet-meaningful-example/example.asp", " > "))
    print('<a href="/">HOME</a> > <a href="/very-long-url-to-make-a-silly-yet-meaningful-example/">VLUMSYME</a> > <span class="active">EXAMPLE</span>')
    print(generate_bc("mysite.com/very-long-url-to-make-a-silly-yet-meaningful-example/example.asp", " > ") == '<a href="/">HOME</a> > <a href="/very-long-url-to-make-a-silly-yet-meaningful-example/">VLUMSYME</a> > <span class="active">EXAMPLE</span>')

    print('Test 5')
    print(generate_bc("www.very-long-site_name-to-make-a-silly-yet-meaningful-example.com/users/giacomo-sorbi", " + "))
    print('<a href="/">HOME</a> + <a href="/users/">USERS</a> + <span class="active">GIACOMO SORBI</span>')
    print(generate_bc("www.very-long-site_name-to-make-a-silly-yet-meaningful-example.com/users/giacomo-sorbi", " + ") == '<a href="/">HOME</a> + <a href="/users/">USERS</a> + <span class="active">GIACOMO SORBI</span>')
    '''

testing()
