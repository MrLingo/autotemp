import controller as ctrl
import blueprint as bp


if __name__ == '__main__':
    print('''
    ####################################################################################################
    #                                                                                                  #
    #                                               AutoTemp                                           #
    #                                                                                                  #
    ####################################################################################################
     ''')

    indents = ctrl.choose_indents()
    print('\n    ---------------------------------------------- HTML ------------------------------------------------\n\n')
    amount_of_html_docs = ctrl.how_much_html_docs()

    ctrl.include_additional_tag('jquery', bp.jquery_tag)
    ctrl.include_additional_tag('bootstrap', bp.bootstrap_tag)

    ctrl.define_html_title()
    ctrl.include_tag(bp.H1_TAG, bp.h1_tag)
    ctrl.include_tag(bp.UL_TAG, bp.ul_tag)
    ctrl.include_tag(bp.OL_TAG, bp.ol_tag)
    ctrl.include_tag(bp.P_TAG, bp.p_tag)
    ctrl.include_tag(bp.A_TAG, bp.a_tag)
    ctrl.include_tag(bp.DIV_TAG, bp.div_tag)
    ctrl.include_tag(bp.IMG_TAG, bp.img_tag)

    ctrl.include_additional_tag('<style>', bp.style_tag)
    ctrl.include_additional_tag('<script>', bp.script_tag)

    ctrl.prepare_html(amount_of_html_docs, indents, ctrl.included_tags)

    print('\n    ---------------------------------------------- CSS -------------------------------------------------\n\n')

    ctrl.tags_to_style()
    ctrl.style(indents, ctrl.final_css_list)
    print(ctrl.final_css_list)

    print('\n ---------------------------------------------- JavaScript ---------------------------------------------\n\n')
    ctrl.amount_of_js_scripts()

    print('\n\nYou are all set! Thank you for using AutoTemp!')
