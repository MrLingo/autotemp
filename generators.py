import os
import blueprint as bp
import os


if __name__ != '__main__':
    html_path = r'C:\AutoTemp Generated Files\HTML'
    css_path = r'C:\AutoTemp Generated Files\CSS'
    js_path = r'C:\AutoTemp Generated Files\JS'

    def generate_html(doc_blueprint, tag_list, num_of_files):
        for i in range(len(tag_list)):
            final_result = doc_blueprint % (tag_list[0], tag_list[1], tag_list[2],
                                            tag_list[3], tag_list[4], tag_list[5],
                                            tag_list[6], tag_list[7], tag_list[8],
                                            tag_list[9], tag_list[10], tag_list[11])
        if not os.path.exists(html_path):
            os.makedirs(html_path)
        os.chdir(html_path)
        for x in range(num_of_files):
            html_doc = open('generated_html_doc_' + str(x) + '.html', 'w')
            html_doc.write(final_result)
            html_doc.close()


    def generate_tag(tag, num_of_tags):
        generated_tags = ''
        for x in range(num_of_tags):
            generated_tags += str(tag)
        return generated_tags

    # css_blueprint_list - every tag's styled
    def generate_css(sheet_blueprint, css_blueprint_list):
        for s in range(len(css_blueprint_list)):
            final_result = sheet_blueprint % (css_blueprint_list[0], css_blueprint_list[1],
                                              css_blueprint_list[2], css_blueprint_list[3],
                                              css_blueprint_list[4], css_blueprint_list[5],
                                              css_blueprint_list[6])
        if not os.path.exists(css_path):
            os.makedirs(css_path)
        os.chdir(css_path)
        css_doc = open('generated_css_sheet.css', 'w')
        css_doc.write(final_result)
        css_doc.close()


    def generate_js(num_of_files):
        if not os.path.exists(js_path):
            os.makedirs(js_path)
        os.chdir(js_path)
        for j in range(num_of_files):
            js_script = open('generated_js_script_' + str(j) + '.js', 'w')
            js_script.write("//Generated blank JS file.")
            js_script.close()
