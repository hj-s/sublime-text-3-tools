#!/usr/bin/env python\n
# -*- coding: utf-8 -*-

import os
import sublime

PM = 'Mediawiker'
PML = 'mediawiker'
PROJECT_SETTINGS_PREFIX = 'mediawiker'


def from_package(*path, **kwargs):

    def posixer(line):
        return line.replace('\\', '/') if posix else line

    name = kwargs.get('name', PM)
    posix = kwargs.get('posix', True)
    is_abs = kwargs.get('is_abs', False)
    root = sublime.packages_path() if is_abs else 'Packages'
    return posixer(os.path.join(root, name, *path))


class MediawikerProperties(object):
    settings_default = None
    settings_user = None

    props = {
        'site': {'text': 'Sites configurations'},
        'syntax': {'text': 'Preferred mediawiki syntax'},
        'syntax_lua': {'text': 'Preferred syntax for Lua'},
        'syntax_css': {'text': 'Preferred syntax for CSS'},
        'syntax_js': {'text': 'Preferred syntax for JS'},
        'site_active': {'text': 'Default site'},
        'summary_postfix': {'text': 'Postfix in post summary'},
        'skip_summary': {'text': 'Skip summary input'},
        'clipboard_as_defaultpagename': {'text': 'Use clipboard data as page name'},
        'newtab_ongetpage': {'text': 'Open pages in new tab'},
        'clearpagename_oninput': {'text': 'Automatic conversion of Url to page name'},
        'password_input_hide': {'text': 'Hide password on input'},
        'password_char': {'text': 'Password character'},
        'snippet_char': {'text': 'Snippet character'},
        'pagelist_maxsize': {'text': 'History size'},
        'files_extension': {'text': 'Extensions of wiki files'},
        'category_root': {'text': 'Root category for CategoryTree'},
        'mark_as_minor': {'text': 'By default, changes are minor'},
        'csvtable_delimiter': {'text': 'CVS data delimiter'},
        'search_namespaces': {'text': 'Namespaces to search'},
        'search_results_count': {'text': 'Max count of search result'},
        'image_prefix_min_length': {'text': 'Minimal required image prefix for search'},
        'wiki_instead_editor': {'text': 'Save to page post'},
        'show_image_in_popup': {'text': 'Show images in popups'},
        'validate_revision_on_post': {'text': 'Check server page revision on post'},
        'linkstopage_limit': {'text': 'Max count of links to page'},
        'preview_lang': {'text': 'Default language for preview'},
        'fold_tags': {'text': 'Fold tags list'},
        'preview_head': {'text': 'HTML head lines for preview'},
        'notifications_show_all': {'text': 'Show all notifications'},
        'notifications_read_sign': {'text': 'Character for read notifications'},
        'wikitable_properties': {'text': 'Default mediawiki table properties'},
        'wikitable_cell_properties': {'text': 'Default mediawiki table cell properties'},
        'use_status_messages_panel': {'text': 'Use separate panel instead status line'},
        'firefox_cookie_files': {'text': 'Custom path to Firefox cookies'},
        'chrome_cookie_files': {'text': 'Custom path to Chrome cookies'},
        'config_icon_checked': {'text': 'Configurator: checked item character'},
        'config_icon_unchecked': {'text': 'Configurator: unchecked item character'},
        'config_icon_radio_checked': {'text': 'Configurator: checked radio item character'},
        'config_icon_radio_unchecked': {'text': 'Configurator: unchecked radio item character'},
        'config_icon_edit': {'text': 'Configurator: edit item character'},
        'config_icon_back': {'text': 'Configurator: back item character'},
        'config_icon_unnumbered_list': {'text': 'Configurator: list item character'},
        'css_html': {'text': 'Custom html css'},
        'panel': {'text': 'Edit panel items list'},
        'pagelist': {'text': 'Pages history'},
        'favorites': {'text': 'Favorite pages'},
        'popup_image_size': {'text': 'Max image size in preview popups'},
        'red_link_icon': {'text': 'Red links mark icon'},
        'debug': {'text': 'Advanced logging mode'},
        'popup_type': {'text': 'Popup type (manual/auto/off)'},
        'show_gutters': {'text': 'Show gutters'},
        'show_favorites_and_history_by_site_host': {'text': 'Show history and favorites pages by host'},
        'offline_mode': {'text': 'Offline mode'}
    }

    props_dependencies = {
        'popup_type': {
            'dep_property': 'offline_mode',
            'dep_value': True,
            'value': 'off'
        }
    }

    props_autoremove = [
    ]

    props_view = {
        'is_here': {'text': 'Mediawiker is enabled', 'default': False, 'type': bool},
        'wiki_instead_editor': {'text': 'Save to page post', 'default': False, 'type': bool},
        'autoreload': {'text': 'Generate a preview after each Nth change', 'default': 0, 'type': int},
        'site': {'text': 'Mediawiki site in view', 'default': '', 'type': str},
        'page_revision': {'text': 'Page revision number', 'default': 0, 'type': int},
        'is_changed': {'text': 'Page has changes', 'default': False, 'type': bool},
        'popups_off': {'text': 'Turn off popups', 'default': False, 'type': bool},
        'preview_cmd': {'text': 'Command for page preview', 'default': 'preview', 'type': str},
        'section': {'text': 'Page section', 'default': 0, 'type': int}
    }

    props_site = {
        'name': {'text': 'Site name', 'type': str, 'default': ''},
        'host': {'text': 'Site Url address', 'type': str, 'default': ''},
        'https': {'text': 'HTTPS protocol instead of HTTP', 'type': bool, 'default': True},
        'is_ssl_cert_verify': {'text': 'Verify server SSL certificates', 'type': bool, 'default': True},
        'path': {'text': 'API path', 'type': str, 'default': '/w/'},
        'pagepath': {'text': 'Pages path', 'type': str, 'default': '/wiki/'},
        'domain': {'text': 'Domain for corp. wikies', 'type': str, 'default': ''},
        'username': {'text': 'Username', 'type': str, 'default': ''},
        'password': {'text': 'Password', 'type': str, 'default': ''},
        'use_http_auth': {'text': 'HTTP authorization', 'type': bool, 'default': False},
        'http_auth_login': {'text': 'HTTP authorization login', 'type': str, 'default': ''},
        'http_auth_password': {'text': 'HTTP authorization password', 'type': str, 'default': ''},
        'proxy_host': {'text': 'Proxy server', 'type': str, 'default': ''},
        'oauth_access_secret': {'text': 'OAuth access secret', 'type': str, 'default': ''},
        'oauth_access_token': {'text': 'OAuth access token', 'type': str, 'default': ''},
        'oauth_consumer_secret': {'text': 'OAuth consumer secret', 'type': str, 'default': ''},
        'oauth_consumer_token': {'text': 'OAuth consumer token', 'type': str, 'default': ''},
        'authorization_type': {'text': 'Authorization type', 'type': str, 'default': 'login'},
        'cookies_browser': {'text': 'Browser for cookies', 'type': str, 'default': 'chrome'},
        'is_wikia': {'text': 'Is a Wikia site', 'type': bool, 'default': False},
        'retry_timeout': {'text': 'Requests timeout', 'type': int, 'default': 30},
        'preview_custom_head': {'text': 'Custom html head tags for preview', 'type': list, 'default': []},
        'preview_sandbox': {'text': 'Special rewritable page for preview', 'type': str, 'default': ''},
        'show_red_links': {'text': 'Mark red links in page text', 'type': bool, 'default': False}
    }

    def __init__(self):
        self.reload_settings()
        self.deprecated = self.get_deprecated()
        # self.autoremove_deprecated()
        self.autoconvert_settings()

        # settings for plugin's panel
        panel_settings_file_name = '%sPanel.sublime-settings' % PM
        if not os.path.exists(from_package(panel_settings_file_name, name='User', posix=False, is_abs=True)):
            panel_settings = sublime.load_settings(panel_settings_file_name)
            panel_settings.set('font_size', 10)
            sublime.save_settings(panel_settings_file_name)

    def reload_settings(self):
        self.settings_default = sublime.decode_value(sublime.load_resource(from_package('Mediawiker.sublime-settings')))
        self.settings = sublime.load_settings('Mediawiker.sublime-settings')
        try:
            self.settings_user = sublime.decode_value(sublime.load_resource(from_package('Mediawiker.sublime-settings', name='User')))
        except IOError:
            self.settings_user = {}

    def autoconvert_settings(self):
        need_update = False
        for key in self.settings_user.copy().keys():
            if key.startswith(PML):
                try:
                    if self.prop(key) not in self.settings_default:
                        print("Unknown option in user configuration: %s" % key)
                    else:
                        need_update = True
                        self.settings.set(self.prop(key), self.settings_user.get(key))
                        self.settings.erase(key)
                except Exception as e:
                    print("Exception while processing settings key %s: %s" % (key, e))

        if need_update:
            sublime.save_settings('Mediawiker.sublime-settings')

    def autoremove_deprecated(self):
        for key in self.settings_user:
            if self.is_deprecated(key):
                self.set_setting(self.deprecated[key], self.get_setting(key))
                self.del_setting(key)

        for key in self.props_autoremove:
            self.del_setting(key)

    def prop(self, key):
        if key.startswith(PML):
            return key.split('_', 1)[1]
        elif key in self.props:
            return key
        return key

    def get_name(self, name):
        return '%s_%s' % (PML, name)

    def remove_prefix(self, name):
        return name[len(PML) + 1:]

    def get_deprecated(self):
        return {self.props[k].get('deprecated'): self.get_name(k) for k in self.props.keys() if self.props[k].get('deprecated', None)}

    def is_deprecated(self, key):
        if key in self.deprecated:
            return True
        return False

    def get_dependency_value(self, key):
        ''' Dependencies between settings - overrides real value '''
        try:
            dep_property = self.props_dependencies.get(key, {}).get('dep_property', None)
            if dep_property is not None and self.get_setting(dep_property) == self.props_dependencies[key]['dep_value']:
                return self.props_dependencies.get(key, {}).get('value')
        except:
            pass
        return None

    def get_setting(self, key, default_value=None):
        '''
        supports:
        * key as "mediawiker_option_name"
        * key as "option_name"
        '''
        self.reload_settings()

        dep_value = self.get_dependency_value(key)
        if dep_value is not None:
            return dep_value

        key = self.prop(key)
        # return self.settings.get(key, default_value)
        view = sublime.active_window().active_view()
        val = None
        if view is not None:
            val = sublime.active_window().active_view().settings().get('%s.%s' % (PROJECT_SETTINGS_PREFIX, key), None)
        return self.settings.get(key, default_value) if val is None else val

    def set_setting(self, key, value):

        key = self.prop(key)
        self.settings.set(key, value)
        sublime.save_settings('Mediawiker.sublime-settings')

    def del_setting(self, key):

        key = self.prop(key)
        self.settings.erase(key)
        sublime.save_settings('Mediawiker.sublime-settings')

    def get_default_setting(self, key):
        self.reload_settings()
        key = self.prop(key)
        return self.settings_default.get(key)

    def get_view_setting(self, view, key, default_value=None, plugin=True):
        ''' plugin: False - for non Mediawiker properties '''

        if key.startswith(PML):
            key = self.remove_prefix(key)

        if plugin:
            assert key in self.props_view, 'Unknown property for view: %s' % key

            default_value = self.props_view[key]['default'] if default_value is None else default_value
            key_type = self.props_view[key]['type']

            key = self.get_name(key)
            return key_type(view.settings().get(key, default_value))
        else:
            return view.settings().get(key, default_value)

    def set_view_setting(self, view, key, value, plugin=True):
        if key.startswith(PML):
            key = self.remove_prefix(key)

        if plugin:
            assert key in self.props_view, 'Unknown property for view: %s' % key
            assert isinstance(value, self.props_view[key]['type']), 'Incorrect type value for %s: %s instead of %s' % (key, type(value), self.props_view[key]['type'])
            key = self.get_name(key)

        view.settings().set(key, value)

    def get_site_setting(self, site, key, default_value=None):

        assert key in self.props_site, 'Unknown property for site: %s' % key

        default_value = self.props_site[key]['default'] if default_value is None else default_value
        key_type = self.props_site[key]['type']
        return key_type(self.get_setting('site').get(site).get(key, default_value))

    def set_site_setting(self, site, key, value):

        assert key in self.props_site, 'Unknown property for site: %s' % key
        key_type = self.props_site[key]['type']
        assert isinstance(value, key_type), 'Incorrect type value for %s: %s instead of %s' % (key, type(value), key_type)

        settings = self.get_setting('site')
        settings[site][key] = value
        self.set_setting('site', settings)
