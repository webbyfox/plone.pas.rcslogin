Tests for plone.pas.rcslogin

test setup
----------

    >>> from Testing.ZopeTestCase import user_password
    >>> from Products.Five.testbrowser import Browser
    >>> browser = Browser()

Plugin setup
------------

    >>> acl_users_url = "%s/acl_users" % self.portal.absolute_url()
    >>> browser.addHeader('Authorization', 'Basic %s:%s' % ('portal_owner', user_password))
    >>> browser.open("%s/manage_main" % acl_users_url)
    >>> browser.url
    'http://nohost/plone/acl_users/manage_main'
    >>> form = browser.getForm(index=0)
    >>> select = form.getControl(name=':action')

plone.pas.rcslogin should be in the list of installable plugins:

    >>> 'Rcslogin Helper' in select.displayOptions
    True

and we can select it:

    >>> select.getControl('Rcslogin Helper').click()
    >>> select.displayValue
    ['Rcslogin Helper']
    >>> select.value
    ['manage_addProduct/plone.pas.rcslogin/manage_add_rcslogin_helper_form']

we add 'Rcslogin Helper' to acl_users:

    >>> from plone.pas.rcslogin.plugin import RcsloginHelper
    >>> myhelper = RcsloginHelper('myplugin', 'Rcslogin Helper')
    >>> self.portal.acl_users['myplugin'] = myhelper

and so on. Continue your tests here

    >>> 'ALL OK'
    'ALL OK'

