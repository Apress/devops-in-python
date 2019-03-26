class DivisibleBy(hamcrest.core.base_matcher.BaseMatcher):

    def __init__(self, factor):
        self.factor = factor

    def _matches(self, item):
        return (item % self.factor) == 0

    def describe_to(self, description):
        description.append_text('number divisible by')
        description.append_text(repr(self.factor))

def divisible_by(num):
    return DivisibleBy(num)