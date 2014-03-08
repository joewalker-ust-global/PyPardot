class Lists():
    """
    A class to query and use Pardot lists.
    List field reference: http://developer.pardot.com/kb/api-version-3/object-field-references#list
    """

    def __init__(self, client):
        self.client = client

    def query(self, **kwargs):
        """
        Returns the lists matching the specified criteria parameters.
        Supported search parameters: http://developer.pardot.com/kb/api-version-3/querying-lists
        ex: client.Lists.query(created_after='yesterday', limit=100)
        """
        result = self._get(path='/do/query', params=kwargs)
        return result

    def read(self, id):
        """
        Returns the data for the list specified by id
        id is the Pardot ID of the target list
        """
        result = self._get(path='/do/read/id/{id}'.format(id=id))
        return result

    def _get(self, path=None, params={}):
        """GET requests for the List object"""
        result = self.client._get(object='list', path=path, params=params)
        return result

    def _post(self, path=None, params={}):
        """POST requests for the List object"""
        result = self.client._post(object='list', path=path, params=params)
        return result

