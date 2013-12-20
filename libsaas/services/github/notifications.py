from libsaas import http, parsers
from libsaas.services import base

from . import resource


class Notifications(resource.GitHubResource):

    path = 'notifications'

    @base.apimethod
    def get(self, reason=None, unread=True):
        """
        For details on the meanings and allowed values for each parameter, see
        http://developer.github.com/v3/activity/notifications/
        """
        url = self.get_url()
        params = base.get_params(
            ('all', 'participating', 'since', 'page', 'per_page'), locals())

        headers = resource.mimetype_accept(format)

        return http.Request('GET', url, params, headers), parsers.parse_json

# TODO Repo specific notifications
# TODO Mark as read
# TODO Threading/ Subscriptions
