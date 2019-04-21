class ProductStates(object):

    def __init__(self, states, states_tags, states_fr):
        self.States = states
        self.StatesTags = states_tags
        self.StatesFr = states_fr

    def __str__(self):
        return self.States
