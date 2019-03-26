class LookupModule(LookupBase):

    def run(self, terms, variables=None, **kwargs):
        return os.path.commonpath(terms)