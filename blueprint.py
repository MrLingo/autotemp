
# The blueprint for the html and css files
if __name__ != '__main__':

    H1_TAG = '<h1>'
    UL_TAG = '<ul>'
    OL_TAG = '<ol>'
    P_TAG = '<p>'
    A_TAG = "<a href='#'>"
    DIV_TAG = '<div>'
    IMG_TAG = "<img src='#'>"
    
    # Hardcoded tags
    jquery_tag = '<script src="https://code.jquery.com/jquery-3.3.1.js" integrity="sha256-2Kok7MbOyxpgUVvAk/HJ2jigOSYS2auK4Pfzbm7uH60=" crossorigin="anonymous"></script>'

    bootstrap_tag = '''<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.0/css/bootstrap.min.css"integrity="sha384-9gVQ4dYFwwWSjIDZnLEWnxCjeSWFphJiwGPXr1jddIhOegiu1FwO5qRGvFXOdJZ4" crossorigin="anonymous">
                       <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.1.0/js/bootstrap.min.js"
                       integrity="sha384-uefMccjFJAIv6A+rW+L4AHf99KvxDjWSu1z9VI8SKNVmz4sk7buKt/6v9KI65qnm" crossorigin="anonymous"></script>
                    '''

    h1_tag = '<h1></h1>\n'
    ul_tag = '''
<ul>
  <li></li>\n
  <li></li>\n
  <li></li>\n
  <li></li>\n
</ul>\n
    '''

    ol_tag = '''
<ol>
  <li></li>\n
  <li></li>\n
  <li></li>\n
  <li></li>\n
</ol>\n
'''

    p_tag = '<p></p>\n'
    a_tag = "<a href='#'>\n"
    div_tag = '<div></div>\n'
    img_tag = "<img src='#'>\n"

    style_tag = '<style></style>\n'
    script_tag = '<script></script>\n'
    # html part
    # 12 tags to style total in each blueprint.

    h1_style = '''
    h1{

    }
    '''
    ul_style = '''
    ul{

    }
    '''
    ol_style = '''
    ol{

    }
    '''

    p_style = '''
    p{

    }
    '''

    a_style = '''
    a{

    }
    '''
    div_style = '''
    div{

    }
    '''

    img_style = '''
    img{

    }
    '''

    html_doc_indented_0 = '''
<!DOCTYPE html>
<html>
<head>
%s
%s
<meta charset='utf-8'>
<title>%s</title>
</head>
<body>
<header></header>
%s
%s
%s
%s
%s
%s
%s
<footer></footer>
</body>
%s
%s
</html>
'''

    html_doc_indented_2 = '''
  <!DOCTYPE html>
  <html>
  <head>
  %s
  %s
  <meta charset='utf-8'>
  <title>%s</title>
  </head>
  <body>
  <header></header>
  %s
  %s
  %s
  %s
  %s
  %s
  %s
  <footer></footer>
  </body>
  %s
  %s
  </html>
    '''

    html_doc_indented_4 = '''
    <!DOCTYPE html>
        <html>
            <head>
                %s
                %s
                <meta charset='utf-8'>
                <title>%s</title>
            </head>
            <body>
                <header></header>
                %s
                %s
                %s
                %s
                %s
                %s
                %s
                <footer></footer>
            </body>
            %s
            %s
        </html>
   '''
##################################################################

# Css part
# 7 tags to style total in each blueprint.
css_sheet_indented_0 = '''
html, body {

}

html {

}

body {

}

header {

}

%s
%s
%s
%s
%s
%s
%s

footer {

}
'''

css_sheet_indented_2 = '''
  html, body {

  }

  html {

  }

  body {

  }

  header {

  }

  %s
  %s
  %s
  %s
  %s
  %s
  %s

  footer {

  }
'''

css_sheet_indented_4 = '''
    html, body {

    }

    html {

        }

    body {

    }

    header {

    }

    %s
    %s
    %s
    %s
    %s
    %s
    %s

    footer {

    }
'''
