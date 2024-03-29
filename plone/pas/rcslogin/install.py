from AccessControl.Permissions import manage_users
from Products.PageTemplates.PageTemplateFile import PageTemplateFile
from Products.PluggableAuthService import registerMultiPlugin

import plugin

manage_add_rcslogin_form = PageTemplateFile('browser/add_plugin',
                            globals(), __name__='manage_add_rcslogin_form' )


def manage_add_rcslogin_helper( dispatcher, id, title=None, REQUEST=None ):
    """Add an rcslogin Helper to the PluggableAuthentication Service."""

    sp = plugin.RcsloginHelper( id, title )
    dispatcher._setObject( sp.getId(), sp )

    if REQUEST is not None:
        REQUEST['RESPONSE'].redirect( '%s/manage_workspace'
                                      '?manage_tabs_message='
                                      'rcsloginHelper+added.'
                                      % dispatcher.absolute_url() )


def register_rcslogin_plugin():
    try:
        registerMultiPlugin(plugin.RcsloginHelper.meta_type)
    except RuntimeError:
        # make refresh users happy
        pass


def register_rcslogin_plugin_class(context):
    context.registerClass(plugin.RcsloginHelper,
                          permission = manage_users,
                          constructors = (manage_add_rcslogin_form,
                                          manage_add_rcslogin_helper),
                          visibility = None,
                          icon='browser/icon.gif'
                         )
