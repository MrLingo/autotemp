# This module takes care of all validations, checks and all the main logic.

import blueprint as bp
import generators as gen


invalid_input_message = '\nInvalid input!'

# Have a fixed length of 12 when filled.
included_tags = []

# Have a fixed length of 7 when filled.
styled_tags = []

final_css_list = []
css_blueprint_list = []


if __name__ != '_main_':

    # Final step before generating the html part
    def prepare_html(num_of_files, indent_option, tag_list):
        if indent_option == 4:
            gen.generate_html(bp.html_doc_indented_4, tag_list, num_of_files)
        elif indent_option == 2:
            gen.generate_html(bp.html_doc_indented_2, tag_list, num_of_files)
        elif indent_option == 0:
            gen.generate_html(bp.html_doc_indented_0, tag_list, num_of_files)


    def choose_indents():
        while True:
            print('\nHow much indents: 2, 4 or 0? For all documents(Html, CSS)\n')
            try:
                indent_input = int(input())
                if indent_input != 2 and indent_input != 4 and indent_input != 0:
                    print(invalid_input_message)
                else:
                    return indent_input
            except ValueError:
                print(invalid_input_message)


    def define_html_title():
        print('Choose title for your html doc/s\n')
        html_title = input()
        included_tags.append(html_title)


    def how_much_html_docs():
        while True:
            try:
                print('How much html documents to create?\n')
                num_of_html_input = int(input())
                if num_of_html_input < 1:
                    print('You have to create atleast one document!')
                else:
                    break
            except ValueError:
                print(invalid_input_message)
        return num_of_html_input


    def include_tag(tag, tag_blueprint):
        print('How many times should ' + str(tag) + ' tag be included?')
        try:
            tag_input = int(input())
            if tag_input > 0:
                generated_tag = gen.generate_tag(tag_blueprint, tag_input)
                included_tags.append(generated_tag)
                styled_tags.append(tag)
            else:
                included_tags.append("")
                styled_tags.append("")
        except ValueError:
            included_tags.append("")
            print(invalid_input_message)


    # <style>, <script>, bootstrap and jquery
    def include_additional_tag(tag, tag_blueprint):
        while True:
            print('\nInclude '+tag+' ?\n')
            try:
                print('Y/N?')
                additional_tag_input = input().upper()
                if additional_tag_input != 'Y' and additional_tag_input != 'N':
                    print('Please enter either Y or N!')
                elif additional_tag_input == 0:
                    included_tags.append("")
                    break
                else:
                    included_tags.append(tag_blueprint)
                    break
            except ValueError:
                print(invalid_input_message)


    # Out of the chosen tags, decide which ones to style
    def tags_to_style():
        print('Which tags to style?\n')
        for x in styled_tags:
            try:
                if x == "":
                    final_css_list.append("")
                else:
                    print('Should the ' + x + ' tag be styled?\n Y/N?')
                    css_input = input().upper()
                    if css_input == 'Y':
                        final_css_list.append(x)
                    elif css_input == 'N':
                        final_css_list.append("")
                    else:
                        print(invalid_input_message)
            except ValueError:
                print(invalid_input_message)


    # Check which blueprint to add in the sheet
    def style(indent, css_list):
        for c in css_list:
            if c == '<h1>':
                css_blueprint_list.append(bp.h1_style)
            elif c == '<ul>':
                css_blueprint_list.append(bp.ul_style)
            elif c == '<ol>':
                css_blueprint_list.append(bp.ol_style)
            elif c == '<p>':
                css_blueprint_list.append(bp.p_style)
            elif c == '<a href="#">':
                css_blueprint_list.append(bp.a_style)
            elif c == '<div>':
                css_blueprint_list.append(bp.div_style)
            elif c == '<img src="#">':
                css_blueprint_list.append(bp.img_style)
            else:
                css_blueprint_list.append('')

        if indent == 0:
            sheet_blueprint = bp.css_sheet_indented_0
        elif indent == 2:
            sheet_blueprint = bp.css_sheet_indented_2
        else:
            sheet_blueprint = bp.css_sheet_indented_4
        gen.generate_css(sheet_blueprint, css_blueprint_list)


    def amount_of_js_scripts():
        print('How many javascript files you want to create?')
        try:
            js_input = int(input())
            if js_input < 0:
                print(invalid_input_message)
            elif js_input == 0:
                return
            else:
                gen.generate_js(js_input)
        except ValueError:
            print(invalid_input_message)










